from re import search
from vue.general import general
from vue.window import BasicWindow
from PySide6.QtWidgets import QApplication, QVBoxLayout, QPushButton, QFormLayout, QLineEdit
from controller.user_controller import UserController
from vue.general import general
from model.bdd import utilisateurBDD

class inscription(BasicWindow):
    
    def __init__(self):
        super().__init__()
        self.nom = QLineEdit()
        self.prenom = QLineEdit()
        self.pseudo = QLineEdit()
        self.mdp = QLineEdit()
        self.setup()

    def setup(self):
        # Create an outer layout
        # Create a form layout for the label and line edit
        Layout = QVBoxLayout()
        Layout2 = QFormLayout()

        # Add a label and a line edit to the form layout



        btn_list2 = QPushButton('Inscription', self)
        btn_list2.resize(btn_list2.sizeHint())
        btn_list2.move(0, 0)
        btn_list2.clicked.connect(self.add_user)

        btn_quit = QPushButton('Quit', self)
        btn_quit.clicked.connect(self.close)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(90, 100)

        Layout2.addRow("Nom", self.nom)
        Layout2.addRow("Prenom", self.prenom)
        Layout2.addRow("Pseudo", self.pseudo)
        Layout2.addRow("Mot de Passe", self.mdp)
        Layout.addLayout(Layout2)
        Layout.addWidget(btn_list2)
        Layout.addWidget(btn_quit)

        self.setGeometry(100, 100, 200, 150)
        self.setWindowTitle("Menu d'inscription")
        self.setLayout(Layout)
        self.show()


    def add_user(self):
        #if(self.nom.text() != "" and self.prenom.text() != "" and self.pseudo.text() != "" and self.mdp.text() != ""):
            UserController.create_user(self.nom.text(),self.prenom.text(),self.pseudo.text(),self.mdp.text())
            #print(UserController.get_user(4)[2])
            self.close()
            print("ajout d'utilisateur réussi")

    