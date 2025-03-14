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
mycursor.execute("SELECT * FROM etudiant")

for i in mycursor:
    print(i)

