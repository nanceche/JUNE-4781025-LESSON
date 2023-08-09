


import random
testvar = True
while testvar:
    countvarin = input('how many random numbers? ')
    if countvarin.isdigit():
        countvar = int(countvarin)
        testvar = False
    else:
        print('No letters only numbers!')


for i in range(countvar):
    print(random.randint(1,10))

import string


print(string.ascii_uppercase)

# password maker

rangevar = int(input('How long password? '))

alphabet = string.ascii_uppercase
pw = ''
for i in range(rangevar):
    randnum = random.randint(0,25)
    pw = pw + alphabet[randnum]
print(pw)


