from random import *

compdata = randint(0,10)

userdata = input("Enter a number between 0 and 10: ")

def random_stuff():
    count = 0
    while count < 3:
        if userdata == compdata:
            print ("You win old man")

        else:
            print ("Loser; Re-enter the digits again")

    

random_stuff()

