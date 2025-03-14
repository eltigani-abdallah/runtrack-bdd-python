import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

dbhost=os.getenv("HOST")
dbuser=os.getenv("USER")
dbpass=os.getenv("PASS")

mydb=mysql.connector.connect(
    host=dbhost,
    user=dbuser,
    password=dbpass
)
mycursor=mydb.cursor()

mycursor.execute("USE laplateforme")
mycursor.execute("SELECT SUM(capacite) FROM salle")

result=mycursor.fetchone()[0]

print(f"la capacite de toutes les salles est de: {result}")

