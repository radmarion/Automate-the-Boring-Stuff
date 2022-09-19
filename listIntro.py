#List are values that contain values and the inner values agve orders to them
#Items in a list are comma delimited 


#List of Lists

spam = [ 0, 1, ['cat','bat'], [10,20,30,[True,False]], 'tunmise']

print(spam[2][0])
print(spam[3][3][0])
print(spam[-2][1])


#List Slices

slice_1 = spam[1:3]

print(slice_1) # Slice creates new list value


spam_1 = [3,'Man','Woman',[3,True,'Does not Matter'],4,5]
print(spam_1)

spam_1[2] = 'Lady'
print(spam_1)

spam_1[0:2] = [4,'boy']
print(spam_1) 