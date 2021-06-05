class CRecette:
    """""
    Classe des Recettes
    """""

    nb_id = 0

    def __init__(self, nom, description, listingredient, auteur):
        self.rnom = nom
        self.rdescription = description
        self.rauteur = auteur
        self.rlistingredient = listingredient
        CRecette.nb_id += 1
        self.mid = str(self.nb_id)

class CIngredient:
    """""
    Classe des Ingrédients
    """""
    nb_id = 0

    def __init__(self, nom, quantité):
        self.inom = nom
        self.iquantité = quantité
        CIngredient.nb_id += 1
        self.mid = str(self.nb_id)
