import CMembre as mbr
import CRecette as rct


def AjouterUtilisateur():
    print("\nCréation d'un membre.")
    print("Nom:")
    nom = input('-')
    print("Prénom:")
    prenom = input('-')
    print("Surnom:")
    pseudo = input('-')
    print("E-mail:")
    email = input('-')
    print("Mot de passe de", nom, ":")
    mdp = input('-')

    membre = mbr.CMember(nom, prenom,pseudo, email, mdp, "0")
    return membre

def AjouterAdmin():
    print("\nCréation d'un membre.")
    print("Nom:")
    nom = input('-')
    print("Prénom:")
    prenom = input('-')
    print("Surnom:")
    pseudo = input('-')
    print("E-mail:")
    email = input('-')
    print("Mot de passe de", nom, ":")
    mdp = input('-')

    membre = mbr.CMember(nom, prenom,pseudo, email, mdp, "1")
    return membre

def ModifMember(liste_m):
    if len(liste_m) == 0:
        print("Aucun membre dans la liste.")
    else:
        listMember(liste_m)
        print("Quel membre souhaitez-vous modifier ?")
        modif = input('Selection id: ')
        value2 = -1
        for k in range(len(liste_m)):
            if liste_m[k].mid == modif:
                value2 = k
        if value2 == -1:
            print("Personne non trouvée...")
            pass
        else:
            print("ID= ", liste_m[value2].mid,
                  " | NOM= ", liste_m[value2].mname,
                  " | PRENOM= ", liste_m[value2].mprenom)
            print("\nModification du membre.")
            print("Nouveau nom:")
            liste_m[value2].mname = input('-')
            print("Nouveau prénom:")
            liste_m[value2].mprenom = input('-')
            print("Nouveau surnom:")
            liste_m[value2].mpseudo = input('-')
            print("Nouveau e-mail:")
            liste_m[value2].memail = input('-')
            print("Nouveau mot de passe de", liste_m[value2].mname, ":")
            liste_m[value2].mdp = input('-')


def listMember(liste_m):
    if len(liste_m) == 0:
        print("Aucun membre dans la liste.")
    else:
        print("Il y a ", len(liste_m), " membre(s).\n")
        for obj in liste_m:
            print("ID:", obj.mid, "| NOM:", obj.mname, "| PRENOM:", obj.mprenom)

def DelMember(liste_m):
    if len(liste_m) == 0:
        print("Aucun membre dans la liste.")
    else:
        listMember(liste_m)
        print("Quelle membre voulez vous supprimer:")
        supp = input('Selection id: ')
        for k in range(len(liste_m)):
            if liste_m[k].mid == supp:
                position = k
                break
        print("Voulez vous vraiment supprimer",liste_m[position].mname,liste_m[position].mprenom)
        valeur = input('oui(o)/non(n) ?')
        if valeur == "oui" or valeur == "o":
            print(liste_m[position].mname, liste_m[position].mprenom, "vient d'être supprimé(e).")
            del liste_m[position]

def AjouterIngredient(liste_ingredient):
    print("\nAjout d'un ingrédient.")
    print("Ingrédient :")
    ingredient = input('-')
    ajout = 0
    for i in range(len(liste_ingredient)):
        if (liste_ingredient[i].inom == ingredient):
            liste_ingredient[i].inom += int(quantite)
            ajout = 1

    if (ajout == 0):
        ingredient_ajoute = rct.CIngredient(ingredient, quantite)
        listeliste_ingredient.append()



def AjouterRecette(liste_recette, auteur):
    print("\nCréation d'une recette.")
    print("Nom de la recette :")
    liste_ingredient = []
    
    i = 0
    while(i == 0):
        nom_recette = input('-')    # On entre le nom de la recette
        print(i)
        i=1
        for j in range(len(liste_recette)):
            if (liste_recette[j].rnom == recette):  # Si une recette de ce nom existe déjà on recommence
                print("\nCette recette est déjà créé veuillez réentrez un nom de recette :")
                i = 0;
                break;

    print("Description de la recette")
    description_recette = input('-')
    i = 0
    while(i == 0):
        print("Ajouter un ingrédient à la recette:")
        print("\t (1) - Oui")
        print("\t (2) - Non")
        decision = input('-')
        if (decision == "1"):
            print("Nom de l'ingrédient:")
            ningredient = input('-')
            print("Quantite :")
            qingredient = input('-')
            ingredient = rct.CIngredient(ningredient,qingredient)
            liste_ingredient.append(ingredient)
        elif (decision == "2"):
            i = 1
        else:
            print("Chaine non reconnu veuillez recommencez s'il vous plaît")
    
    print("Ajout de la recette " + nom_recette + " de " + auteur)
    recette = rct.CRecette(nom_recette,description_recette,liste_ingredient,auteur)
    return recette