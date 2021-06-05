class CMember:
    """""
    Classe des Membres
    """""

    nb_id = 0

    def __init__(self, nom, prenom, pseudo, email, mdp, m_type):
        self.mname = nom
        self.mprenom = prenom
        self.mpseudo = pseudo
        self.memail = email
        self.mmdp = mdp
        self.mtype = m_type # 0:user / 1:admin
        CMember.nb_id += 1
        self.mid = str(self.nb_id)
