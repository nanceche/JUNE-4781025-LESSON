number_1= float(input ("Choose a number?"))
number_2= int (input ("Choose a whole number?"))
calculation = input ("Choose which math calculation to do? + , - , * , /, s")
print (calculation)

if calculation == "+":
    print(number_1+number_2)
elif calculation == "-":
    print(number_1-number_2)
elif calculation == "*":
    print(number_1*number_2)
elif calculation == "/":
    print (number_1/number_2)
elif calculation == "s":
    print (number_1**number_2)

