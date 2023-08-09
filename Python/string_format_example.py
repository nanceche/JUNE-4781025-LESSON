import string

var1 = "Leon"
var2 = True
var3 = 156

# print(var1 + var2 + var3)  # his wont work

# Set up an output template
outputstr  = "This var1: {}, This is var2: {}, this is var3: {} "
# substitute the variables in the template
print(outputstr.format(var1,var2,var3))


print(str.format(outputstr,var1,var2,var3))
