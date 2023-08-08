# Lists

listvar1 = ["Meat", "Vegetables", "Beer", "Eggs"]

print(listvar1)
#             0           1    2     3      4  
listvar2 = ['Stringitem', 23, True, None, 56.65]
print(listvar2)

print(listvar2[1])
print(listvar2[4])


listvar3 = [listvar1,listvar2,["Beach","Shops","Zoo","Gallery"]]

print(listvar3)
print(listvar3[0][0])
print(listvar3[1][4])

# Iterating over a list


for item in listvar1:  # iterate on items in a list
    print("At the shop I need to buy a " + item)
    for letter in item:  # iterate on letters in a strinf
        print(letter)

examplestr = "Here are letter"
print(examplestr[7])  # the 8th letter 


print( "There are ", len(listvar1), " items in the list")

# using len

invar1 = input("Type a word: ")
lettercount = len(invar1)
reverseword = ''   # set up an empty var
for indexitem in range(lettercount-1,-1,-1):   # we need to subtract one from len to use for the index
    reverseword = reverseword + invar1[indexitem]
print(reverseword)


# list functions

# list.append(object)

listvar1.append("melon")
# list.remove(value)
listvar1.remove("Vegetables")

# list.insert(index,object)
listvar1.insert(1,"Soup")
# list.count(object)
listvar2 = [2,2,4,5,6,7,7,7,8,9]
print(listvar2.count(7))

# creating a list from a string

listitems = "John.Mary.Jack.Belinda.Fred.Sharon"

print(listitems.split('.'))
# creating a string from a list
seperator = ':'
print(seperator.join(listvar1))

# using the 'in' test

drinks = ["tea","gin","squash","lassi"]
drinktest = input("What would you like to drink? ")
if drinktest in drinks:
    print("Have a " + drinktest )
else:
    print("We don't have a " + drinktest )



