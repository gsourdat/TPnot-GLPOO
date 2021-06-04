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
        recette = fct.AjouterRecette(liste_recette, current_user)
        liste_recette.append(recette)
        input()


    if value == "end":
        stop = 0


