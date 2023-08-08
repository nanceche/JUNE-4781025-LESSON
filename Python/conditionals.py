# Control Flow

# Sequence

# The order in which steps run

# Selection

# Having a test and deciding what to run next

# Iteration

# Doing the same thing many times

## Selection

teststring = 'cat'
inputstring = input("Type in the word cat: ")

if teststring == inputstring:
    #this code will run if the test result is True
    print('this code will run if the test result is True')
else:
    print('This code will run if the test result is false')

print('This line will always print')

# Example string test using 'in'

if 'a' in inputstring:
    print('your input contained the letter a')
else:
    print('your input did not contained the letter a')


# Testing multiple things

inputnumbervar1 = input('Type in a number')
numbervar1 = int(inputnumbervar1)

if numbervar1 < 50:
    print('You have put in a number less than 50')
elif numbervar1 < 100:
    print('You have put in a number between 50 and 99')
elif numbervar1 < 500:
    print('You have put in a number between 100 and 499')
elif numbervar1 < 1200:
    print('You have put in a number between 500 and 1199')
else:
    print('your number is bigger than 1199')

# Nested if

if numbervar1 > 0:
    if numbervar1 < 50:
        print('your number is between 1 and 49')
    else:
        print('your number is big')
else:
    print('your number is less than 1')

# Logical operators

# if numbervar1 > 0 and < 50:  incorrect test.

if numbervar1 > 0 and numbervar1 < 50:
    print('Your number is in the correct range 1-49')
else:
    print('Your number is outside the range')

if (numbervar1 > 0 and numbervar1 < 50) or numbervar1 == 128:
    print('You win!')


