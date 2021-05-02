import CMembre as mbr


def AjouterUtilisateur():
    print("\nCréation d'un membre.")
    print("Nom:")
    nom = input('-')
    print("Prénom:")
    prenom = input('-')
    print("E-mail:")
    email = input('-')
    print("Numéro de téléphone:")
    tel = input('-')
    print("Mot de passe de", nom, ":")
    mdp = input('-')

    membre = mbr.CMember(nom, prenom, email, tel, mdp, "user")
    return membre

def AjouterAdmin():
    print("\nCréation d'un membre.")
    print("Nom:")
    nom = input('-')
    print("Prénom:")
    prenom = input('-')
    print("E-mail:")
    email = input('-')
    print("Numéro de téléphone:")
    tel = input('-')
    print("Mot de passe de", nom, ":")
    mdp = input('-')

    membre = mbr.CMember(nom, prenom, email, tel, mdp, "Admin")
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
            print("Nouveau e-mail:")
            liste_m[value2].memail = input('-')
            print("Nouveau numéro de téléphone:")
            liste_m[value2].mtel = input('-')
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

