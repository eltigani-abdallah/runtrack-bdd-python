import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

mycursor=mydb.cursor()

mycursor.execute("USE laplateforme")
mycursor.execute("SELECT SUM(superficie) FROM etage")

result=mycursor.fetchone()[0]

print(f"la superficie de LaPlateforme est {result} m2")

