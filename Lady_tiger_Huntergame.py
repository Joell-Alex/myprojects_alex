import random
you_want_to_play = "y"

while you_want_to_play == "y":
    print("Welcome to Lady Tiger Hunter Game")
    print("Let's start the game")

    def GameWin(comp, you):
        print("Choice of computer is:", comp)  # print computer output only after user makes a choice

        if comp == you:
            return None
        elif comp == "L":
            if you == "H":
                return False
            elif you == "T":
                return True
        elif comp == "T":
            if you == "L":
                return False
            elif you == "H":
                return True
        elif comp == "H":
            if you == "T":
                return False
            elif you == "L":
                return True

    randomnum = random.randint(1, 3)  # helps generate a random number between 1 to 3 so the game is unbiased
    if randomnum == 1:
        comp = "L"
    elif randomnum == 2:
        comp = "T"
    elif randomnum == 3:
        comp = "H"

    print("Computer turn: (L) for Lady, (T) for Tiger, (H) for Hunter?")
    you = input("Your turn: (L) for Lady, (T) for Tiger, (H) for Hunter?").upper  # taking input from the user

    a = GameWin(comp, you)  # storing in a variable called "a"

    if a:
        print("You won")
    elif a is None:
        print("Game is tie")
    else:
        print("You lost")
  
    you_want_to_play = input("Do you want to play again? (y/n): ").lower()
