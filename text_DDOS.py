spam = input('What is the number')
spam = int(spam)
while spam < 7:
    spam += 1
    if spam == 3:
        continue
    elif spam == 6:
        continue
    print('spam is ' + str(spam))
