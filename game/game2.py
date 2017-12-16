import random
import time

def dice():
    player = random.randint(1,6)
    print("you rolled " + str(player))
    ai = random.randint(1,6)
    print("the ai rolls .....")
    time.sleep(2)
    print("ai rolled " + str(ai))

    if player>ai:
        print("you win")
    elif player==ai:
        print("Tie game ")
    else:
        print("you lose")

    print("Quit? Y/N")
    cont = input()
    if cont == "Y" or cont == "y":
       exit()
    elif cont == "N" or cont == "n":
        pass
    else:
        print("I did not understand that. Playing again.")
while True:
    print("Press return to roll your die.")
    roll = input()
    dice()
