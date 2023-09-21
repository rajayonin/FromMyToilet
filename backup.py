# Copies documents from one directory to another, allowing for ignored files and directories


__author__ = "Luis Daniel Casais Mezquida <luis-daniel.casais@ext.prosegur.com>"


import sys
if sys.version_info < (3, 10):
    raise SystemExit("Python 3.10+ required")


import os, sys, shutil
import fnmatch
import argparse
import pathlib
import difflib

from typing import Iterable

from hurry.filesize import size as toHumanSize  # pip install hurry.filesize
from hurry.filesize import si, iec



# defaults: backup current folder inside Documents folder to Documents folder in OneDrive

SOURCE_BACKUP_FOLDER = "Documents"
ONEDRIVE_FOLDER = "OneDrive"
TARGET_BACKUP_FOLDER = "Documentos"

# compute subdirectory from cwd
relative_path = ''.join(difflib.restore([li for li in difflib.ndiff(os.getcwd(), f"C:\\Users\\{os.getlogin()}\\{SOURCE_BACKUP_FOLDER}\\") if li[0] != ' '], 1))

DEFAULT_SOURCE_DIR = f"C:\\Users\\{os.getlogin()}\\{SOURCE_BACKUP_FOLDER}\\{relative_path}\\"
DEFAULT_TARGET_DIR = f"C:\\Users\\{os.getlogin()}\\{ONEDRIVE_FOLDER}\\{TARGET_BACKUP_FOLDER}\\{relative_path}\\"

DEFAULT_IGNORE_PATTERNS = ('__pycache__','venv*','.git*','.vscode', 'Mis *', 'Mi *')



# parser
parser = argparse.ArgumentParser(
    description="Copies the contents of a source folder to a target folder, allowing to ignore files and folders matching some patterns.\nIf executed without options, uses the current default configuration (see epilog).",
    epilog=
f"""
current default configuration:
  source_dir:
                        {DEFAULT_SOURCE_DIR}
  target_dir:
                        {DEFAULT_TARGET_DIR}
  ignore_patterns:
                        {DEFAULT_IGNORE_PATTERNS}
""",
    usage='python %(prog)s [OPTIONS]',
    formatter_class=argparse.RawTextHelpFormatter
)

parser.add_argument(
    "-s", "--source_dir",
    help="Source directory.",
    type=pathlib.Path,
    required=False,
    default=DEFAULT_SOURCE_DIR
)

parser.add_argument(
    "-o", "--target_dir",
    help="Target directory.",
    type=pathlib.Path,
    required=False,
    default=DEFAULT_TARGET_DIR
)

parser.add_argument(
    "-i", "--ignore-patterns",
    help="Patterns to ignore, using Unix filename pattern matching (basic glob).",
    nargs="+",
    required=False,
    default=DEFAULT_IGNORE_PATTERNS
)



def in_pattern(string: str, patterns: Iterable[str]) -> bool:
    """
    Finds if a string matches some patterns.
    """
    for pattern in patterns:
        if fnmatch.fnmatch(string, pattern):
            return True

    return False


def count_files(source_dir: str, ignore_patterns: Iterable[str] = ()) -> tuple[int, int]:
    """
    Counts the number of files in a directory.
    """

    count = 0
    size = 0
    excluded_dirs = []

    for root, dirs, files in os.walk(source_dir):

        # count files and sizes
        for f in files:
            if not in_pattern(f, ignore_patterns):
                count += 1
                size += os.path.getsize(os.path.join(root, f))

        # find excluded dirs
        for d in dirs:
            if in_pattern(d, ignore_patterns):
                excluded_dirs.append(d)

        # remove excluded dirs
        dirs[:] = [d for d in dirs if d not in excluded_dirs]

    return count, size


def copy2_verbose(src, dst):
    # logs the copied files
    print(src)
    return shutil.copy2(src, dst)



if __name__ == "__main__":

    args = parser.parse_args()
    source_dir = args.source_dir
    target_dir = args.target_dir
    ignore_patterns = args.ignore_patterns


    print("Counting files...", end='\r')

    count, size = count_files(source_dir, ignore_patterns)

    formatted_count = toHumanSize(count, system=si)
    if count < 1000:  # delete last "B"
        formatted_count = formatted_count[:-1]

    formatted_size = toHumanSize(size, system=iec)

    sys.stdout.write("\033[K")  # clear line


    # prompt
    choice = input(f"Copy from {source_dir} to {target_dir} ({formatted_count} files - {formatted_size}B)? [y/N]: ").lower()
    if choice != "y":
        exit()


    if not os.path.exists(target_dir):
        choice = input(f"About to create folder {target_dir}, are you sure? [y/N]:").lower()
        if choice != "y":
            exit()

        os.makedirs(os.path.dirname(target_dir))


    shutil.copytree(source_dir, target_dir, ignore=shutil.ignore_patterns(*ignore_patterns), copy_function=copy2_verbose, dirs_exist_ok=True)


    print("\nDone!")


