# FromMyToilet

We've all been there.  
On the toilet, or having a shower, and thinking... "hey, what if I could code the smallest Rock-Paper-Scissors game ever?".  
Well, this repository is for that purpose, for the most stupid and useless shit (pun intended) I can think off (and code).

## Rock-Paper-Scissors in 3 lines of code

`rock-paper-scissors_in-3-lines.py`

Yeah, that's pretty much it. The idea, based on a post I saw on Reddit (but a bit more developed, this game is infinite), was "How small can I make the code for Rock-Paper-Scissors?".  
The answer is 3 lines:

```python
import random
while input("Select [R]ock, [P]aper or [S]cissors: ") in ("R", "P", "S"):
    print(random.choice(("You won.", "You lost.", "You lost.")))
```

_Note: if you enter something that is not one of the three options, it ends the program, which is the only way to do it without `KeyboardInterrupt`._

## Vim, but you can only quit Vim

`vim-but-you-can-only-quit.vimrc`

Tired of people not knowing how to quit Vim? No? Anyway, here's a Vim config file that _only_ allows you to quit Vim.  
No moving, no saving, no nothing. Just quitting (like in life).

How to use it? You have to copy the file to your home directory, and call it `.vimrc`:

```bash
cp vim-but-you-can-only-quit.vimrc ~/.vimrc
```

_Note: It gives error `E35: No previous regular expression` when trying to do anything, but I don't know what causes that or how to fix it._

## Alternate `sl`

`alternate-sl.c`

Typing `sl` instead of `ls` is something that happens to us terminal users when we're in a hurry.  
Toyoda Masashi tried to help us fix this by adding a command that plays a small train animation when we run it ([link here](https://github.com/mtoyoda/sl)).  
But I'm no nice japanese man, I want to see people suffer. So my alternate version of this command is to drop a fork bomb.

If you want to use it, run:

```bash
sudo gcc alternate-sl.c -o /usr/local/bin/sl
sudo cmod +x /usr/local/bin/sl
```

_Note: I haven't tested this, so it might not work._
