import re

from model.bdd import RecetteBDD,IngrédientBDD
from exceptions import Error, InvalidData


class RecetteController:
    """
    Member actions
    """

        

    def list_recettes():
        rec_data = RecetteBDD.getAllRecettes()
        return rec_data

    def get_recettes(rec_id):
        rec_data = RecetteBDD.getRecetteFromId(rec_id)
        return rec_data

    def getIngRec(id_R):
        rec_data =RecetteBDD.getIngrédientRecette(id_R)
        return rec_data

    def create_recette(nom_R,description_R,auteur_R):
        RecetteBDD.setRecette(nom_R,description_R,auteur_R)

    def edit_recette(id_Rec, nom_Rec, desc_Rec):
        RecetteBDD.EditRecette(id_Rec, nom_Rec, desc_Rec)
    #def update_user(self, member_id, member_data):


    def delete_recette(rec_id):
        RecetteBDD.delRecette(rec_id)


    def search_recettefromNom(nom):

        # Query database
        rec_data = RecetteBDD.getRecettesFromNom(nom)
        return rec_data

    def search_recettefromAuteur(auteur):

        # Query database
        rec_data = RecetteBDD.getRecettesFromAuteur(auteur)
        return rec_data

    def get_recettes_ing(ing):
        rec_data = RecetteBDD.getRecettesFromIngredient(ing)
        return rec_data


    def get_ing():
        rec_data = IngrédientBDD.getAllIngrédients()
        return rec_data

    def addIngtoRec(id_Ing,id_Rec):
        rec_data = RecetteBDD.setIngRec(id_Ing,id_Rec)
        return rec_data

    def _check_profile_data(self, data, update=False):
        name_pattern = re.compile("^[\S-]{2,50}$")
        type_pattern = re.compile("^(customer|seller)$")
        email_pattern = re.compile("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$")
        mandatories = {
            'firstname': {"type": str, "regex": name_pattern},
            'lastname': {"type": str, "regex": name_pattern},
            'email': {"type": str, "regex": email_pattern},
            'type': {"type": str, "regex": type_pattern}
        }
        for mandatory, specs in mandatories.items():
            if not update:
                if mandatory not in data or data[mandatory] is None:
                    raise InvalidData("Missing value %s" % mandatory)
            else:
                if mandatory not in data:
                    continue
            value = data[mandatory]
            if "type" in specs and not isinstance(value, specs["type"]):
                raise InvalidData("Invalid type %s" % mandatory)
            if "regex" in specs and isinstance(value, str) and not re.match(specs["regex"], value):
                raise InvalidData("Invalid value %s" % mandatory)

