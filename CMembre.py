class CMember:
    """""
    Classe des Membres
    """""

    nb_id = 0

    def __init__(self, nom, prenom, email, tel, mdp, m_type):
        self.mname = nom
        self.mprenom = prenom
        self.memail = email
        self.mtel = tel
        self.mmdp = mdp
        self.mtype = m_type #user/admin
        CMember.nb_id += 1
        self.mid = str(self.nb_id)