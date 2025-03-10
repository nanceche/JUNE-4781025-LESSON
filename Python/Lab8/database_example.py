import pyodbc  # We need the module to connecto the db

# We set up an object to describe how to connect to the DB
connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
# We open the connection to the database (like opening a file)
# This creates an intermediate DB object
conn = pyodbc.connect(connectionString)

# We use our new object to create another object called a cursor
# They cursor can send SQL commands to the DB
cur = conn.cursor()

# We send a command to the DB and save the result
result = cur.execute('SELECT * FROM salesperson').fetchall()
justnames = cur.execute('SELECT company_name,county FROM company').fetchall()
contacttable = cur.execute('SELECT * FROM contact').fetchall()
addperson = cur.execute ("INSERT INTO company(company_no,company_name,tel,county,postcode) VALUES (4500,`QA`,`01234567890`,`London`,`W11AA`)")



# Gather a list of table
# tables = cur.tables()
#print('--- Tables ---')
#for i in tables:
#    print(i)

# Gather column names from a table
print('--- Company Columns ---')
colnames = cur.columns('salesperson')
for i in colnames:
    print(i)

# We close the connection
conn.close()
# We display the result we saved
for row in result:
    print(row)

for row in addperson:
    print(row)
#for row in justnames:
   # print(row)

#for row in contacttable:
    #print(row)
