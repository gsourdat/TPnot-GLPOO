import mysql.connector
import mariadb
import sys

#mydb = mysql.connector.connect(user='sourdat', password='nh2m2494',
#                                 host='127.0.0.1',
#                                 database='recettes')




try:
        mydb = mariadb.connect(
            user="sourdat",
            password="nh2m2494",
            host="127.0.0.1",
            port=3306,
            database="recettes"

        )
except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)


mycursor = mydb.cursor()

#INGREDIENTS

class IngrédientBDD():

  def getAllIngrédients():
    mycursor.execute("SELECT * FROM ingrédients")
    myresult = mycursor.fetchall()
    return myresult


  def getIngrédient(val):
    mycursor.execute("SELECT id_I,nom_I FROM ingrédients WHERE nom_I=?", (val,))
    myresult = mycursor.fetchall()
    return myresult


  def setIngrédient(val):
    try:
      mycursor.execute("INSERT INTO ingrédients (nom_I) VALUES (?)", (val,))
      mydb.commit()
    except mariadb.Error as e:
      print(f"Error: {e}")

  def delIngrédient(val):
    try:
      mycursor.execute("DELETE FROM ingrédients WHERE ingrédients.nom_I=?",(val,))
      mydb.commit()
    except mariadb.Error as e:
      print(f"Error: {e}")


#RECETTES
class RecetteBDD():

  def setRecette(data):
    try:
      mycursor.execute("INSERT INTO recettes (Nom_R,Description_R,Auteur_R) VALUES (?,?,?)", (data.Nom_R,data.Description_R,data.Auteur_R,))
      mydb.commit()
    except mariadb.Error as e:
      print(f"Error: {e}")

  def getAllRecettes():
    mycursor.execute("SELECT * FROM recettes")
    myresult = mycursor.fetchall()
    return myresult

  def getRecetteFromId(id_R):
    mycursor.execute("SELECT * FROM recettes where id_R=?",(id_R,))
    myresult = mycursor.fetchall()
    return myresult[0]

  def getRecettesFromAuteur(id_A):
    mycursor.execute("SELECT * FROM recettes where Auteur_R=?",(id_A,))
    myresult = mycursor.fetchall()
    return myresult

  def delRecette(id_R):
    try:
      mycursor.execute("DELETE FROM recettes WHERE recettes.id_R=?",(id_R,))
      mydb.commit()
    except mariadb.Error as e:
      print(f"Error: {e}")

  def addIngrédientRecette(data):
    try:
      mycursor.execute("INSERT INTO quantitéingrédients (id_R,id_I,Quantité) VALUES (?,?,?)", (data.id_R,data.id_I,data.Quantité,))
    except mariadb.Error as e:
      print(f"Error: {e}")

  def delIngrédientRecette(id_I,id_R):
    try:
      mycursor.execute("DELETE FROM quantitéingrédients WHERE quantitéingrédients.id_R=? and quantitéingrédients.id_I=?",(id_R,id_I,))
      mydb.commit()
    except mariadb.Error as e:
      print(f"Error: {e}")

  def getIngrédientRecette(id_R):
    #mycursor.execute("SELECT (id_I,nom_I) FROM quantitéingrédients inner join ingrédients on quantitéingrédients.id_I = ingrédients.id_I where id_R=?",(id_R,))
    mycursor.execute("SELECT id_I,nom_I FROM quantitéingrédients natural join ingrédients where id_R=?",(id_R,))
    myresult = mycursor.fetchall()
    return myresult


#UTILISATEURS
class utilisateurBDD():


  def setUtilisateur(nom_U,prenom_U,pseudo_U,mdp_U):
    try:
      mycursor.execute("INSERT INTO utilisateur (Nom_U,prenom_U,pseudo_U,mdp_U,admin_U) VALUES (?,?,?,?,?)", (nom_U,prenom_U,pseudo_U,mdp_U,0))
      
      mydb.commit()
    except mariadb.Error as e:
      print(f"Error: {e}")

    

  def getUtilisateurFromId(id_U):
    mycursor.execute("SELECT * FROM utilisateur WHERE idUtilisateur=?", (id_U,))
    myresult = mycursor.fetchall()
    return myresult[0]

  def getAllUtilisateur():
    mycursor.execute("SELECT * FROM utilisateur")
    myresult = mycursor.fetchall()
    return myresult

  def delUtilisateur(id_U):
    try:
      mycursor.execute("DELETE FROM recettes WHERE recettes.Auteur_R=?",(id_U,))
      mycursor.execute("DELETE FROM utilisateur WHERE utilisateur.idUtilisateur=?",(id_U,))
      mydb.commit()
    except mariadb.Error as e:
      print(f"Error: {e}")

  def getUserFromPseudoMdp(pseudo,mdp):
    mycursor.execute("SELECT * FROM utilisateur WHERE pseudo_U=? and mdp_U=?", (pseudo,mdp,))
    myresult = mycursor.fetchall()
    return myresult

  def getUserFromNP(nom,prenom):
    mycursor.execute("SELECT * FROM utilisateur WHERE nom_U=? and prenom_U=?", (nom,prenom,))
    myresult = mycursor.fetchall()
    return myresult


#utilisateurBDD.setUtilisateur("azze","adzazd","abc","123")
#setRecette("Poulet Basquaise","on cuisine bien fort",1)
#print(getUtilisateurFromId(1))
#setRecette("qqsqsd","fsdfsdmfl",4)




mydb.commit()
