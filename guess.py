# This is a guess the number game
import random

guessestaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number 1 and 20.')

while guessestaken < 6:
  print('Take a guess.')
  guess = input()
  guess = int(guess)
  
  guessestaken = guessestaken + 1
  
  if guess < number:
    print('Your guess is too low.')
    
  if guess > number:
    print('Your guess is too high.')
    
  if guess == number:
    break
  
if guess == number:
  guessestaken = str(guessestaken)
  print('Good job, ' + myName + '! You guessed my number in ' + guessestaken + ' guesses!')
  
if guess != number:
  number = str(number)
  print('Nope the number I was thinking of was ' + number)