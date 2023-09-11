import random

while True:
    s2 = random.randrange(1, 16)
    # print(s2)
    s = int(input("Guess any integer value between 1 to 16: "))
    if s == s2:
        print("Congrulation! you win the game")
        break
    else:
        print("Sorry, you lost the game please try again")

