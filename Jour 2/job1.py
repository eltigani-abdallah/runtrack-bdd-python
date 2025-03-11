import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"
)

mycursor=mydb.cursor()

mycursor.execute("USE laplateforme")
mycursor.execute("SELECT * FROM etudiant")

for i in mycursor:
    print(i)

