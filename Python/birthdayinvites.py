person = input('Who is comiong to your birthday? ')

birthdaypeople = open('Python/Birthdaylist.txt','a')
birthdaypeople.write(person + '\n')
birthdaypeople.close()