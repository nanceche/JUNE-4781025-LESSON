from statistics import mean


value1=int(input("What is your mark for maths? "))
value2=int(input("What is your mark for english? "))
value3=int(input("What is your mark for ICT ?"))

if mean([value1,value2,value3])>= 65:
    print ("Pass")
else:
    print ("Fail")

