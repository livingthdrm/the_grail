from random import randint


magic_number = randint(0,10)

user_input = input("Enter a number x between {} and {}:  "  .format(0,10))

def lottery_numbers():
            if user_input == magic_number:
                               print("You won the lottery")
#use else instead of elif, was just testing the program
            elif user_input != magic_number:
                               print("Run the program again")

print(magic_number)
lottery_numbers()
