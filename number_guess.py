#Number guessing game
import random

secretNumber = random.randint(1,20)
numGuesses = 0
print('I am thinking of a number between 1 and 20.')

for guessesTaken in range(1,7):
    print('Take a guess')
    guess = int(input())
    if guess > secretNumber:
        print('Your guess is too high')
    elif guess < secretNumber:
        print('Your guess is too low')
    else:
        break
if guess == secretNumber:
    print(f"Good job! You guessed my number in {guessesTaken} guesses")
else:
    print(f"Nope. The number I was thinking of was {secretNumber}.")

