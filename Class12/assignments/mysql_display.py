# Display records using Python-MySQL connectivity

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="24941315", database="mydb"
)

cursor = mydb.cursor()

cursor.execute("SELECT * FROM t_emp")
results = cursor.fetchall()

for row in results:
    print(row)

mydb.close()

'''
(1, 'Karan Nath', datetime.date(1975, 11, 22), 2)
(2, 'Juginder Ram', datetime.date(1980, 5, 22), 1)
(3, 'Judin Yadav', datetime.date(1995, 2, 13), 4)
(4, 'Suren Pal', datetime.date(1985, 11, 11), 2)
'''