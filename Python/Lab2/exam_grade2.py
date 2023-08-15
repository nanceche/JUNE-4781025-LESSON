grade=int(input ("What mark have you recieved?"))
level= int (input("Which level are you on ?"))

if level ==1 and grade < 1 or grade > 100:
   print ("Error: marks must be between 1 and 100")

if level ==1 and grade < 50:
    print ("Fail")

if level ==1 and 50 < grade < 60:
    print ("Pass")

if level ==1 and  61 < grade < 70:
    print ("Merit")

if level ==1 and 71 < grade < 100:
    print ("Distinction")

if level ==2 and grade < 40:
    print ("Fail")

if level ==2 and 40 < grade < 50:
    print ("Pass")

if level ==2 and  51 < grade < 65:
    print ("Merit")

if level ==2 and 66 < grade < 100:
    print ("Distinction")
