import mysql.connector
import mariadb
import sys

#mydb = mysql.connector.connect(user='sourdat', password='nh2m2494',
#                                 host='127.0.0.1',
#                                 database='recettes')



<<<<<<< HEAD
try:
    mydb = mariadb.connect(
        user="root",
        password="root",
        host="127.0.0.1",
        port=3306,
        database="recettes"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
=======

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
>>>>>>> ba18cf895ac0a658a13cd6984568745dccb464bf


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
<<<<<<< HEAD
=======
      mydb.commit()
>>>>>>> ba18cf895ac0a658a13cd6984568745dccb464bf
    except mariadb.Error as e:
      print(f"Error: {e}")

  def delIngrédient(val):
    try:
      mycursor.execute("DELETE FROM ingrédients WHERE ingrédients.nom_I=?",(val,))
<<<<<<< HEAD
=======
      mydb.commit()
>>>>>>> ba18cf895ac0a658a13cd6984568745dccb464bf
    except mariadb.Error as e:
      print(f"Error: {e}")


#RECETTES
class RecetteBDD():

<<<<<<< HEAD
  def setRecette(data):
    try:
      mycursor.execute("INSERT INTO recettes (Nom_R,Description_R,Auteur_R) VALUES (?,?,?)", (data.Nom_R,data.Description_R,data.Auteur_R,))
=======
  def setRecette(Nom_R,Description_R,Auteur_R):
    try:
      mycursor.execute("INSERT INTO recettes (Nom_R,Description_R,Auteur_R) VALUES (?,?,?)", (Nom_R,Description_R,Auteur_R,))
      mydb.commit()
>>>>>>> ba18cf895ac0a658a13cd6984568745dccb464bf
    except mariadb.Error as e:
      print(f"Error: {e}")

  def getAllRecettes():
    mycursor.execute("SELECT * FROM recettes")
    myresult = mycursor.fetchall()
    return myresult

<<<<<<< HEAD
=======
  def EditRecette(id_Rec, nom_Rec, desc_Rec):
    try:
      mycursor.execute("UPDATE recettes SET Nom_R=? and Description_R=? WHERE id_R=?",(nom_Rec,desc_Rec,id_Rec))
      mydb.commit()
    except mariadb.Error as e:
      print(f"Error: {e}")
      

>>>>>>> ba18cf895ac0a658a13cd6984568745dccb464bf
  def getRecetteFromId(id_R):
    mycursor.execute("SELECT * FROM recettes where id_R=?",(id_R,))
    myresult = mycursor.fetchall()
    return myresult[0]

  def getRecettesFromAuteur(id_A):
    mycursor.execute("SELECT * FROM recettes where Auteur_R=?",(id_A,))
    myresult = mycursor.fetchall()
    return myresult

<<<<<<< HEAD
  def delRecette(id_R):
    try:
      mycursor.execute("DELETE FROM recettes WHERE recettes.id_R=?",(id_R,))
=======
  def getRecettesFromNom(id_N):
    mycursor.execute("SELECT * FROM recettes where Nom_R=?",(id_N,))
    myresult = mycursor.fetchall()
    return myresult

  def getRecettesFromIngredient(ing):
    mycursor.execute("SELECT * FROM recettes.recettes natural join quantitéingrédients natural join ingrédients where nom_I=?;",(ing,))
    myresult = mycursor.fetchall()
    return myresult

  def delRecette(id_R):
    try:
      mycursor.execute("DELETE FROM recettes WHERE recettes.id_R=?",(id_R,))
      mydb.commit()
>>>>>>> ba18cf895ac0a658a13cd6984568745dccb464bf
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
<<<<<<< HEAD
=======
      mydb.commit()
>>>>>>> ba18cf895ac0a658a13cd6984568745dccb464bf
    except mariadb.Error as e:
      print(f"Error: {e}")

  def getIngrédientRecette(id_R):
    #mycursor.execute("SELECT (id_I,nom_I) FROM quantitéingrédients inner join ingrédients on quantitéingrédients.id_I = ingrédients.id_I where id_R=?",(id_R,))
    mycursor.execute("SELECT id_I,nom_I FROM quantitéingrédients natural join ingrédients where id_R=?",(id_R,))
    myresult = mycursor.fetchall()
    return myresult

<<<<<<< HEAD

=======
  def setIngRec(id_Ing,id_R):
    mycursor.execute("insert into quantitéingrédients (id_R,id_I,Quantité) values (?,?,?)",(id_R,id_Ing,1))
>>>>>>> ba18cf895ac0a658a13cd6984568745dccb464bf
#UTILISATEURS
class utilisateurBDD():


  def setUtilisateur(nom_U,prenom_U,pseudo_U,mdp_U):
<<<<<<< HEAD
    mycursor.execute("INSERT INTO utilisateur (Nom_U,prenom_U,pseudo_U,mdp_U,admin_U) VALUES (?,?,?,?,?)", (nom_U,prenom_U,pseudo_U,mdp_U,0))
    print("fait")

=======
    try:
      mycursor.execute("INSERT INTO utilisateur (Nom_U,prenom_U,pseudo_U,mdp_U,admin_U) VALUES (?,?,?,?,?)", (nom_U,prenom_U,pseudo_U,mdp_U,0))
      
      mydb.commit()
    except mariadb.Error as e:
      print(f"Error: {e}")

    
>>>>>>> ba18cf895ac0a658a13cd6984568745dccb464bf

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
<<<<<<< HEAD
=======
      mydb.commit()
>>>>>>> ba18cf895ac0a658a13cd6984568745dccb464bf
    except mariadb.Error as e:
      print(f"Error: {e}")

  def getUserFromPseudoMdp(pseudo,mdp):
    mycursor.execute("SELECT * FROM utilisateur WHERE pseudo_U=? and mdp_U=?", (pseudo,mdp,))
    myresult = mycursor.fetchall()
    return myresult

<<<<<<< HEAD
=======
  def getUserFromNP(nom,prenom):
    mycursor.execute("SELECT * FROM utilisateur WHERE nom_U=? and prenom_U=?", (nom,prenom,))
    myresult = mycursor.fetchall()
    return myresult

>>>>>>> ba18cf895ac0a658a13cd6984568745dccb464bf

#utilisateurBDD.setUtilisateur("azze","adzazd","abc","123")
#setRecette("Poulet Basquaise","on cuisine bien fort",1)
#print(getUtilisateurFromId(1))
#setRecette("qqsqsd","fsdfsdmfl",4)




mydb.commit()
