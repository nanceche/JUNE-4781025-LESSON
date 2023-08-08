# Iteration

# While loop, useful if you don't know ahead of time h
# how many iterations you need

#  initialvar = x    # set a variable to test
#  while <test>:
#      code here
#      alter the initialvar   # otherwise it will loop forever 

initialvar1 = int(input('enter a number'))
while initialvar1 > 0:
    initialvar1 = initialvar1 - 1
    print('This is the value of initialvar1:',initialvar1 )        
    

print('end run')

# break ses the while condition to False and exits the loop

while initialvar1 > 0:
    initialvar1 = initialvar1 - 1
    if initialvar1 == 7:
        print('7 is a lucky number is some traditions')
        break
        
    print('This is the value of initialvar1:',initialvar1 )        
    

print('end run')

# continue, skipping the execution of a single loop

while initialvar1 > 0:
    initialvar1 = initialvar1 - 1
    if initialvar1 == 7:
        print('7 is a lucky number is some traditions')
        continue
    print('This is the value of initialvar1:',initialvar1 )        
    
print('end run')

# alternative maths

# take away 
# initialvar1 = initialvar1 - 1
# initialvar1 -= 1

# addidtion
# initialvar1 = initialvar1 + 1
# initialvar1 += 1

# for loop, if you know ahead of time how many iterations 
# you need

# for <number loops to run>:
#     code to run

# range()  iterator to set up the number of loops

# numbers from 0 -9

for loopvariable1 in range(10):
    print('this is a for loop, the loopvariable is currently:', loopvariable1)

for loopvariable2 in range(2,10):  # 2-9
    print('this is a for loop, the loopvariable is currently:', loopvariable2)

for loopvariable3 in range(10,0,-1):   # 10-1
    print('this is a for loop, the loopvariable is currently:', loopvariable3)

for i in range(7):
    print(i)
    if i == 5:
        break   # exits the loop



namevar = input('Type in you name: ')

for letter in namevar:
    print(letter)