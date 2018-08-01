from random import randint
def choosee():
    magic_number = randint(0,10)
    user_input = input("Pick a number between 0 & 10: ")
    if magic_number == user_input:
        print("You have won!!")
    else:
        print(magic_number)
        print("Run the program again. sorry!")

choosee()
