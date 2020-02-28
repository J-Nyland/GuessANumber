import random
min = 1
max = 6

number = random.randint(min,max)

input("Press Enter to roll the dice!")
print("rolling the dice!")
number = str(number)
print("you rolled a " + number)

roll_again = input("Do you want to roll again?")

if roll_again == "yes" or roll_again == "y":
    print("Rolling the dice again!")
    number = str(number)
    print("you rolled a " + number)

else:
    number = str(number)
    print("You rolled a " + number)
    print("Now take your turn!")