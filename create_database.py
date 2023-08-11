import pyodbc  # We need the module to connecto the db

# We set up an object to describe how to connect to the DB
connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'

# We open the connection to the database (like opening a file)
# This creates an intermediate DB object
conn = pyodbc.connect(connectionString)

# We use our new object to create another object called a cursor
# They cursor can send SQL commands to the DB
cur = conn.cursor()

create_table= "CREATE TABLE STUDENTS1 (ID int PRIMARY KEY, FNAME varchar (255), SNAME varchar (255), COURSE varchar (255) DEFAULT ('General'))"
insert_value=["INSERT INTO STUDENTS1 (ID,FNAME,SNAME,COURSE) VALUES (4,'Susan','Delfino','English')","INSERT INTO STUDENTS1 (ID,FNAME,SNAME,COURSE) VALUES (5,'Gabby','Solis','Fashion')","INSERT INTO STUDENTS1 (ID,FNAME,SNAME,COURSE) VALUES (6,'Lynette','Scavo','Business')"]
update_value= "UPDATE STUDENTS1 SET COURSE = 'Maths' WHERE ID = 2"
# conn.execute(insert_value)
conn.execute(update_value)

conn.commit()



result = cur.execute('SELECT * FROM STUDENTS1').fetchall()
# We display the result we saved
for row in result:
    print(row)


conn.close()