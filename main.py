<<<<<<< HEAD
import sys

from controller.user_controller import UserController
from PySide6.QtWidgets import QApplication
from vue.menu import MenuWindow

#https://realpython.com/python-pyqt-layout/
#https://www.learnpyqt.com/tutorials/creating-multiple-windows/


def run():
    # Init db
    #admin_controller = UserController()
    app = QApplication(sys.argv)

    menu = MenuWindow()

    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
=======
import Fonctions as fct

"""""
Main
"""""
liste_user = []
liste_admin = []
liste_ingredient = []
liste_recette = []
stop = 1


while stop:

    print("Que voulez vous faire ?")
    print("\t (0) - Ajouter un Utilisateur")
    print("\t (1) - Modifier un Utilisateur")
    print("\t (2) - Lister les Membres")
    print("\t (3) - Supprimer un Membre")
    print("\t (4) - Ajouter un Administrateur \n")
    print("\t (5) - Ajouter une recette \n")

    value = input('SELECTION: ')

    current_user = "Patrick" # utilisé pour la fonction d'ajout de recette

    if value == "0":
        membre = fct.AjouterUtilisateur()
        liste_user.append(membre)
        input()

    if value == "1":
        fct.ModifMember(liste_user)
        input()

    if value == "2":
        print("Utilisateur :")
        fct.listMember(liste_user)
        print("\nAdministrateur :")
        fct.listMember(liste_admin)
        input()

    if value == "3":
        fct.DelMember(liste_user)
        input()

    if value == "4":
        membre = fct.AjouterAdmin()
        liste_admin.append(membre)
        input()

    if value == "5":
       
        liste_recette.append(fct.AjouterRecette(liste_recette, current_user))
        input()


    if value == "end":
        stop = 0


>>>>>>> 58ec0176b7f498f3bc85d5ae0d9bb7bac43f7360
