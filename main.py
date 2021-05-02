import Fonctions as fct

"""""
Main
"""""
liste_user = []
liste_admin = []
stop = 1

while stop:

    print("Que voulez vous faire ?")
    print("\t (0) - Ajouter un Utilisateur")
    print("\t (1) - Modifier un Utilisateur")
    print("\t (2) - Lister les Membres")
    print("\t (3) - Supprimer un Membre")
    print("\t (4) - Ajouter un Administrateur \n")

    value = input('SELECTION: ')

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

    if value == "end":
        stop = 0


