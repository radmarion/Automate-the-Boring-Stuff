#Number Guessing Game

from random import randint #randint module

name = str(input('What is your name ? '))
number = randint(1,21)
print('Well, ' + name + " I am thinking of a number between 1 and 21")
print('You are guessing Whole numbers only')
print('You have 7 Guesses')

#Code Test for Debug next line , Remove the comment # to debug
# print('DEBUG : THE SECRETE NUMBER IS ' + str(number))

#Guess Control Section
for guessesTaken in range(1,8):
  guess = int(input('Take a guess ')) # Come back to add a TRY phrase
  
  if guess < number:
     print('Your guess is too low')
  elif guess > number:
    print('Your guess is too high')
  else:
    break # This condition happens if the number is guessed correctly
  

  
if guess == number:
  print('Good job ' + name + ' You guessed the number in ' + str(guessesTaken)  + ' guesses')

else : 
  print('The correct answer is actually ' + str(number) )