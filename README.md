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
