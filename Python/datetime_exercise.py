import datetime

indate = input('Type in a date in the format YYYY-MM-DD: ')
indate2 = input('Type in a date in the format YYYY-MM-DD: ')

userdate1 = datetime.datetime.strptime(indate,'%Y-%m-%d')
userdate2 = datetime.datetime.strptime(indate2,'%Y-%m-%d')

timedeltavar = userdate1 - userdate2


print(f"{userdate1} is {timedeltavar.days} days from {userdate2}")
