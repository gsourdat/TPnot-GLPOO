from PySide6.QtWidgets import QListWidget, QGridLayout,  QVBoxLayout, QPushButton, QHBoxLayout

from vue.window import BasicWindow
from controller.user_controller import UserController
from vue.listerecettes import listerecettes
from vue.user.show import ListUserQt


class general(BasicWindow):

    def __init__(self):
        super().__init__()
        self.listeRec = None
        self.listeUser = None
        #self.principalWindow = None
        self.setup()

    def setup(self):
        # Create an outer layout
        # Create a form layout for the label and line edit
        Layout = QVBoxLayout()

        # Add a label and a line edit to the form layout

        

        btn_list = QPushButton('Mes Recettes', self)
        btn_list.resize(btn_list.sizeHint())
        btn_list.move(0, 0)
        btn_list.clicked.connect(self.recRecette)

        btn_list2 = QPushButton('Rechercher Recette', self)
        btn_list2.resize(btn_list2.sizeHint())
        btn_list2.move(0, 0)
        #btn_list2.clicked.connect(self.list_user)

        btn_list3 = QPushButton('Gestion Utilisateurs', self)
        btn_list3.resize(btn_list2.sizeHint())
        btn_list3.move(0, 0)
        btn_list3.clicked.connect(self.list_user)

        btn_list4 = QPushButton('Gestion Recettes', self)
        btn_list4.resize(btn_list2.sizeHint())
        btn_list4.move(0, 0)
        #btn_list4.clicked.connect(self.list_user)

        Layout.addWidget(btn_list)
        Layout.addWidget(btn_list2)
        Layout.addWidget(btn_list3)
        Layout.addWidget(btn_list4)

        self.setGeometry(100, 100, 200, 150)
        self.setWindowTitle('Menu de connexion')
        self.setLayout(Layout)
        self.show()

    def recRecette(self):
        self.listeRec = listerecettes()
        self.listeRec.show()
    def list_user(self):
        self.listeUser = ListUserQt()
        self.listeUser.show()
    

