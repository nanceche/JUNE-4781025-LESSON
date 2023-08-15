grade=int(input ("What mark have you recieved?"))

if grade < 1 or grade > 100:
    print ("Error: marks must be between 1 and 100")

elif grade < 50:
    print ("Fail")

elif 50 < grade < 60:
    print ("Pass")

elif 61 < grade < 70:
    print ("Merit")

elif 71 < grade < 100:
    print ("Distinction")


