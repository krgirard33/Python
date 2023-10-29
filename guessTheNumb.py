# This is a guess the number game.

import random

secretNumber = random.randint(1, 20)

print("I am thinking of a number between 1 and 20")

for guessesTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())
    
    if guess < secretNumber:
        print('Guess is too low\n')
    elif guess > secretNumber:
        print('Guess is too high\n')
    else:
        break
        
if guess == secretNumber:
    print('You got the secret number in ' + str(guessesTaken) + ' guesses.')
else:
    print('Nope, the number was ' + str(secretNumber))