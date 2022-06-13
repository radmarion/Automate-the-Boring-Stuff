def divide(number):
  try:
    return 42/number
  except ZeroDivisionError:
    print("Error: You tried to divide by 0")

print(divide(2))
print(divide(33))
print(divide(12))
print(divide(0))
print(divide(5))