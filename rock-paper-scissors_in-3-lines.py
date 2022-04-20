import random
while input("Select [R]ock, [P]aper or [S]cissors: ") in ("R", "P", "S"):
    print(random.choice(("You won.", "You lost.", "You lost.")))