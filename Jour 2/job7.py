import mysql.connector
import os
from dotenv import load_dotenv
import decimal

load_dotenv()

dbhost=os.getenv("HOST")
dbuser=os.getenv("USER")
dbpass=os.getenv("PASS")


mydb=mysql.connector.connect(
    host=dbhost,
    user=dbuser,
    password=dbpass,
    database="enterprise"
)

mycursor=mydb.cursor()


class Employe:
    def __init__(self, nom= None, prenom=None, salaire=None, id_service=None):
        self.nom=nom
        self.prenom=prenom
        self.salaire=salaire
        self.id_service=id_service
        
    
    def creer_employe(self):
        
        insert_statement= "INSERT INTO employe (nom,prenom,salaire,id_service) VALUES (%s,%s,%s,%s)"
        insert_values=(self.nom, self.prenom, self.salaire, self.id_service)
        mycursor.execute(insert_statement, insert_values)
        mydb.commit()

        print(f"{self.nom} a été ajouté dans la table sans leur consentement")
    
    def affiche_employe(self):
        if not self.nom or not self.prenom:
            print("l'employé n'existe pas. regarde sous le lit")
        else:
            select_statement="SELECT id,nom, prenom, salaire, id_service FROM employe WHERE nom=%s and prenom=%s"
            select_values=(self.nom, self.prenom)
            mycursor.execute(select_statement,select_values)
            result=mycursor.fetchone()

            if result:
                result=tuple(float (x) if isinstance(x, decimal.Decimal) else x for x in result)
            print(result)

    def update_employe(self,champ, info):
        self.champ=champ
        self.info=info
        update_statement= f"UPDATE employe SET {self.champ}={self.info} WHERE nom='{self.nom}' AND prenom='{self.prenom}'"
        mycursor.execute(update_statement)
        mydb.commit()

        print("Table modifié. n'oublie pas de verifier les info avec affiche_employe()")

    def supprimer_employe(self):
        del_statement="DELETE FROM employe WHERE nom=%s AND prenom=%s"
        del_info = (self.nom, self.prenom)
        mycursor.execute(del_statement, del_info)
        mydb.commit()
        print(f"L'employé {self.prenom} {self.nom} a vu son abonnement à la vie se terminer plus tôt que prévu.")

employe1=Employe("blob","glob",50,4)

#employe1.creer_employe()

#employe1.affiche_employe()   

#employe1.update_employe("salaire", 10)


employe1.supprimer_employe()


