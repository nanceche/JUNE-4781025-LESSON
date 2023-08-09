# open file, create a textstream

openedfilevar = open("Python/paragraph.txt")


print(openedfilevar)

# read data from textstream to a string
fileasastring = openedfilevar.read()

# close the textstream
openedfilevar.close()

# Edit our Text
dogstory = fileasastring.replace('cat','dog')
carstory = dogstory.replace('plane','car')

print(carstory)
# Open file (deletes file contents)
editedfilevar = open("Python/paragraph.txt",'w')
# Write string to textstream
editedfilevar.write(carstory)
# close file
editedfilevar.close()



