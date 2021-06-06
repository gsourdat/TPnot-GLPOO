import re

from model.bdd import utilisateurBDD
from exceptions import Error, InvalidData


class UserController:
    """
    Member actions
    """

        

    def list_users():
        user_data = utilisateurBDD.getAllUtilisateur()
        return user_data

    def get_user(user_id):
        user_data = utilisateurBDD.getUtilisateurFromId(user_id)
        return user_data

    def create_user(nom_U,prenom_U,pseudo_U,mdp_U):
        utilisateurBDD.setUtilisateur(nom_U,prenom_U,pseudo_U,mdp_U)
        
    #def update_user(self, member_id, member_data):


    def delete_user(user_id):
        print("fait")
        utilisateurBDD.delUtilisateur(user_id)


    def search_user(pseudo, mdp):

        # Query database
        user_data = utilisateurBDD.getUserFromPseudoMdp(pseudo,mdp)
        return user_data

    def search_userNP(nom, prenom):

        # Query database
        user_data = utilisateurBDD.getUserFromNP(nom,prenom)
        return user_data


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

