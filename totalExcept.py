numberCats = input('How many cats do you have? ')
try:
  if int(numberCats) >= 4:
    print('Well Hello, Cat lady.')
  else:
    print('So you do\'nt like cats ')

except ValueError:
  print("You did not enter a number")
