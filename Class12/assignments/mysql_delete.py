import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="24941315", database="mydb"
)

cursor = mydb.cursor()

# Prompt the user to enter the ID of the record to delete
delete_id = int(input("Enter the ID of the record to delete: "))

# SQL query to delete the record

query = "DELETE FROM t_emp WHERE empid = %s"
cursor.execute(query, (delete_id,))

# Commit the changes
mydb.commit()

print(f"Record with ID {delete_id} deleted successfully.")

# Show the updated records
cursor.execute("SELECT * FROM t_emp")
results = cursor.fetchall()

for row in results:
    print(row)

cursor.close()
mydb.close()

'''
>>> (1, 'Paula Ferguson', datetime.date(1975, 11, 22), 2, 10000)
>>> (3, 'Judin Yadav', datetime.date(1995, 2, 13), 4, 10000)
>>> (4, 'Suren Pal', datetime.date(1985, 11, 11), 2, 10000)
'''