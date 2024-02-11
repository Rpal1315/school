# Guess the no. game
# Imports
from random import randint as rd


def NumberGuesserV1(start: int, stop: int, attempts: int):
    # Point System Declaration
    pt = attempts
    vict = False

    # Random no. generation
    num = rd(start, stop)

    # Game input
    print(f"Guess the number between {start} and {stop}")
    for i in range(0, attempts):
        inp = int(input("Enter your guess"))

        # Game Check
        if inp == num:
            print("You have guessed it correctly")
            print(f"Points: {pt}")
            vict = True
            break
        elif inp > num:
            print(f"Incorrect. The no. is lesser than {inp}")
            pt -= 1
        elif inp < num:
            print(f"Incorrect. The no. is greater than {inp}")
            pt -= 1
        else:
            print("There was some internal problem")
    else:
        print(f"You are out of attempts. You lost. The number was {num}")
    if vict:
        return pt, vict
    else:
        return vict


def NumberGuesserV2(start: int, stop: int):
    num = rd(start, stop)
    print(f"Guess the number between {start} and {stop}")
    inp = int(input("Enter your guess"))
    loct = abs(num - inp)
    try:
        pt = 1 / loct
    except ZeroDivisionError:
        pt = 2
    print(f"You scored {pt} points. Your guess({inp}) was {loct} points to {num}")


NumberGuesserV2(1, 100)
