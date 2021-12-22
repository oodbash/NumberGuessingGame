import art
import random

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.choice(range(1,101))
print(f"Pssst, the correct answer is {number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
hit = False
if difficulty.lower() == "easy":
    guesses = 10
else:
    guesses = 5
while (guesses > 0):
    print(f"You have {guesses} attempts remaininng to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number:
        guesses = 0
        hit = True
    elif guess < number:
        print("Too low.\nGuess again.")
        guesses -= 1
    else:
        print("Too high.\nGuess again.")
        guesses -= 1

if hit == True:
    print(f"You got it! The answer was {number}.")
else:
    print("You've run out of guesses, you lose.")