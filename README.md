# FromMyToilet

We've all been there.  
On the toilet, or having a shower, and thinking... "hey, what if I could code the smallest Rock-Paper-Scissors game ever?".  
Well, this repository is for that purpose, for the most stupid and useless shit (pun intended) I can think off (and code).

## Rock-Paper-Scissors in 3 lines of code - [`rock-paper-scissors_in-3-lines.py`](rock-paper-scissors_in-3-lines.py)

Yeah, that's pretty much it. The idea, based on a post I saw on Reddit (but a bit more developed, this game is infinite), was "How small can I make the code for Rock-Paper-Scissors?".  
The answer is 3 lines:

```python
import random
while input("Select [R]ock, [P]aper or [S]cissors: ") in ("R", "P", "S"):
    print(random.choice(("You won.", "You lost.", "You lost.")))
```

_Note: if you enter something that is not one of the three options, it ends the program, which is the only way to do it without `KeyboardInterrupt`._

## Vim, but you can only quit Vim - [`vim-but-you-can-only-quit.vimrc`](vim-but-you-can-only-quit.vimrc)

Tired of people not knowing how to quit Vim? No? Anyway, here's a Vim config file that _only_ allows you to quit Vim.  
No moving, no saving, no nothing. Just quitting (like in life).

How to use it? You have to copy the file to your home directory, and call it `.vimrc`:

```bash
cp vim-but-you-can-only-quit.vimrc ~/.vimrc
```

_Note: It gives error `E35: No previous regular expression` when trying to do anything, but I don't know what causes that or how to fix it._

## Alternate `sl` - [`alternate-sl.c`](alternate-sl.c)

Typing `sl` instead of `ls` is something that happens to us terminal users when we're in a hurry.  
Toyoda Masashi tried to help us fix this by adding a command that plays a small train animation when we run it ([link here](https://github.com/mtoyoda/sl)).  
But I'm no nice japanese man, I want to see people suffer. So my alternate version of this command is to drop a fork bomb.

If you want to use it, run:

```bash
sudo gcc alternate-sl.c -o /usr/local/bin/sl
sudo cmod +x /usr/local/bin/sl
```

_Note: I haven't tested this, so it might not work._


## Backup - [`backup.py`](backup.py)

Python script to backup the current (inside `Documents/`) subfolder to Onedrive, allowing for ignore patterns with Unix filename pattern matching, although it can be used for any folder.

It requires Python 3.10+, and the [`hurry.filesize`](https://pypi.org/project/hurry.filesize/) module[^requirements].

To run it on the default settings (OneDrive backup)[^mod]:
```shell
python3 backup.py
```

It also allows to input specific folders:
```shell
python3 backup.py -s <source folder> -o <output folder> -i <pattern>, ...
```

E.g.:
```shell
python3 backup.py -s . -o ../Backup/ -i *.git* test.txt
```

You can always see all available options with `-h`:
```powershell
PS C:\Users\rajayonin\Documents\GitHub\FromMyToilet> python .\backup.py -h
```
```
usage: python backup.py [OPTIONS]

Copies the contents of a source folder to a target folder, allowing to ignore files and folders matching some patterns.
If executed without options, uses the current default configuration (see epilog).

options:
  -h, --help            show this help message and exit
  -s SOURCE_DIR, --source_dir SOURCE_DIR
                        Source directory.
  -o TARGET_DIR, --target_dir TARGET_DIR
                        Target directory.
  -i IGNORE_PATTERNS [IGNORE_PATTERNS ...], --ignore-patterns IGNORE_PATTERNS [IGNORE_PATTERNS ...]
                        Patterns to ignore, using Unix filename pattern matching (basic glob).

current default configuration:
  source_dir:
                        C:\Users\rajayonin\Documents\GitHub\FromMyToilet\
  target_dir:
                        C:\Users\rajayonin\OneDrive\Documentos\GitHub\FromMyToilet\
  ignore_patterns:
                        ('__pycache__', 'venv*', '.git*', '.vscode', 'Mis *', 'Mi *')
```



[^requirements]: You could probably adapt it to an older version of python, just delete the `raise SystemExit()` line and see what breaks.  
You can also prevent the use of the `hurry.filesize` module, it's basically for formatting.

[^mod]: Change the global variables `DEFAULT_SOURCE_DIR`, `DEFAULT_TARGET_DIR` and `DEFAULT_IGNORE_PATTERNS` to change default values.

_Note: This took me soooo fucking long..._


## Max
How many ways are there to compute the maximum of three numbers? Well...
