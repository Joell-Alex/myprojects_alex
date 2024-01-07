import random
you_want_to_play = "y"

while you_want_to_play == "y":
    def gameWin(comp, you):
        print("Computer choice is:", comp)
        if comp == you:
            return None
        elif comp == "r":
            if you == "p":
                return False
            else:
                return True
        elif comp == "p":
            if you == "r":
                return False
            else:
                return True
        elif comp == "s":
            if you == "p":
                return False
            else:
                return True

    print("Computer turn: Enter (r) for rock, (p) for paper, and (s) for scissor: ")
    randomno = random.randint(1, 3)
    if randomno == 1:
        comp = "r"
    elif randomno == 2:
        comp = "p"
    elif randomno == 3:
        comp = "s"

    you = input("Your turn: Enter (r) for rock, (p) for paper, and (s) for scissor: ").lower()
    a = gameWin(comp, you)

    if a:
        print("You win")
    elif a is None:
        print("Game is a tie")
    else:
        print("You lose")

    you_want_to_play = input("Do you want to continue? (y/n): ").lower()
