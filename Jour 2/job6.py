import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

mycursor=mydb.cursor()

mycursor.execute("USE laplateforme")
mycursor.execute("SELECT SUM(capacite) FROM salle")

result=mycursor.fetchone()[0]

print(f"la capacite de toutes les salles est de: {result}")

