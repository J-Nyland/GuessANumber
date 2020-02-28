import random

numberofGuesses = 0

#Randomly picks a number between 1&15
number = random.randint(1,15)

#Gets user's name
name = input("Please enter you're name")

print(name + ", I am thinking of a whole number between 1 & 15, can you guess it?")

#You are only given 5 guesses to pick the number
while numberofGuesses < 10: 
    guess = input("Have a guess!")
    guess = int(guess)

    numberofGuesses = numberofGuesses + 1
    guessesLeft = 10 - numberofGuesses

    if guess < number:
        guessesLeft=str(guessesLeft)
        print("Your guess is too low! You have " + guessesLeft + " guesses left")

    if guess > number:
        guessesLeft=str(guessesLeft)
        print("Your guess is too high! You have " + guessesLeft + " guesses left")  

    if guess ==number:
        break

if guess == number:
    numberofGuesses=str(numberofGuesses)
    print("Well done! You guessed the number in " + numberofGuesses + " attempts!")

else:
    number=str(number)
    print("Sorry, the number I was thinking of was "  + number + ". Better luck next time!")

