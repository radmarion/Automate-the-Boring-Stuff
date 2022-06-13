#Number Guessing Game

from random import randint #randint module

name = str(input('What is your name ? '))
number = randint(1,21)
print('Well, ' + name + " I am thinking of a number between 1 and 21")
print('You are guessing Whole numbers only')
print('You have 7 Guesses')

#Guess Control Section
for guessesTaken in range(1,8):
  try:
    guess = int(input('Take a guess '))
  except ValueError:
    print('Please enter a number')
  if guess < number:
     print('Your guess is too low')
  elif guess > number:
    print('Your guess is too high')
  else:
    break # This condition happens if the number is guessed correctly
  

  
if guess == number:
  print('Good job ' + name + 'You guessed the number in ' + str(guessesTaken) )

else : 
  print('The correct answer is actually ' + str(number) )