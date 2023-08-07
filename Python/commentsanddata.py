# Numbers, Integers & Floats
intvar = 123
floatvar = 12.3

# Text, String

stringvar1 = 'This is a string'
stringvar2 = "This is a string"

#  Boolean

truvar = True
falsevar = False

# putting vars into other code

print('Some Text')
print(stringvar1)
print(truvar)
print(intvar)

# Interactive programs

inputvar = input('Type something in here: ')

print(inputvar)

# Numerical Addition

print(intvar+2)     

# String Concatenation

print(inputvar + stringvar1)

# this will fail as we have different data types 
# print(intvar + inputvar)

# Casting

#str()  Takes date, and converts it to a string

convertedvar = str(intvar)
print(convertedvar + inputvar)



# int() converts to a integer

textvar2 = input("Type in a number: ")

convtoint = int(textvar2)

print(convtoint + 5)

# float() converts to a floating point
print(float(123))
print(float("123"))

# bool() converts to a boolean

print(bool('any text'))  # This is true
print(bool(''))          # empty string is false

print(bool(123))
print(bool(-123))
print(bool(12.3))
print(bool(0))

# Other maths function

# * mutiply
# - subtract
# / divide
# ** powerof
# %  modulo  show the remainder of a division calculation



print(3/2)
print(3%2)


# 3/2    two goes in to 3 once, 1 remainder 

print(10%5)   # 0
print(7%5)    # 2

# Other was of casting data

numvar = 56.5
textvar = "Hello, I am: "

print(textvar , numvar)
print(convertedvar , inputvar)


 