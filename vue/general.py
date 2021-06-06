from PySide6.QtWidgets import QListWidget, QGridLayout,  QVBoxLayout, QPushButton, QHBoxLayout

from vue.window import BasicWindow
from controller.user_controller import UserController
<<<<<<< HEAD

=======
from vue.listerecettes import listerecettes
from vue.user.show import ListUserQt
from vue.recette.show import ListRecQt
from vue.recette.show2 import ListAllRecQt
>>>>>>> ba18cf895ac0a658a13cd6984568745dccb464bf

class general(BasicWindow):

    def __init__(self):
        super().__init__()
<<<<<<< HEAD
=======
        self.listeRec = None
        self.listeUser = None
>>>>>>> ba18cf895ac0a658a13cd6984568745dccb464bf
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
<<<<<<< HEAD
        #btn_list.clicked.connect(self.testConnect)
=======
        btn_list.clicked.connect(self.recMesRecette)
>>>>>>> ba18cf895ac0a658a13cd6984568745dccb464bf

        btn_list2 = QPushButton('Rechercher Recette', self)
        btn_list2.resize(btn_list2.sizeHint())
        btn_list2.move(0, 0)
<<<<<<< HEAD
        #btn_list2.clicked.connect(self.list_user)

        Layout.addWidget(btn_list)
        Layout.addWidget(btn_list2)

        self.setGeometry(100, 100, 200, 150)
        self.setWindowTitle('Menu de connexion')
        self.setLayout(Layout)
        self.show()

=======
        btn_list2.clicked.connect(self.recRecette)

        if(UserController.get_user(BasicWindow.idUser)[5]==1):
            btn_list3 = QPushButton('Gestion Utilisateurs', self)
            btn_list3.resize(btn_list2.sizeHint())
            btn_list3.move(0, 0)
            btn_list3.clicked.connect(self.list_user)
        #btn_list4.clicked.connect(self.list_user)

        btn_quit = QPushButton('Close', self)
        btn_quit.clicked.connect(self.close)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(90, 100)

        Layout.addWidget(btn_list)
        Layout.addWidget(btn_list2)
        if(UserController.get_user(BasicWindow.idUser)[5]==1):
            Layout.addWidget(btn_list3)
        Layout.addWidget(btn_quit)

        self.setGeometry(100, 100, 200, 150)
        self.setWindowTitle('Menu')
        self.setLayout(Layout)
        self.show()

    def recMesRecette(self):
        self.listeRec = ListRecQt()
        self.listeRec.show()
    def recRecette(self):
        self.listeRec = ListAllRecQt()
        self.listeRec.show()
    def list_user(self):
        self.listeUser = ListUserQt()
        self.listeUser.show()


    

>>>>>>> ba18cf895ac0a658a13cd6984568745dccb464bf
