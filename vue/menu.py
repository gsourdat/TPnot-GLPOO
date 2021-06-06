from re import search
from vue.general import general
from vue.window import BasicWindow
from PySide6.QtWidgets import QApplication, QVBoxLayout, QPushButton, QFormLayout, QLineEdit
from controller.user_controller import UserController
from vue.general import general
from vue.inscription import inscription

class MenuWindow(BasicWindow):
    
    def __init__(self):
        super().__init__()
        self.principalWindow = None
        self.inscriptionWindow = None
        self.pseudo = QLineEdit()
        self.mdp = QLineEdit()
        self.setup()

    def setup(self):
        # Create an outer layout
        # Create a form layout for the label and line edit
        Layout = QVBoxLayout()
        Layout2 = QFormLayout()

        # Add a label and a line edit to the form layout

        

        btn_list = QPushButton('Connexion', self)
        btn_list.resize(btn_list.sizeHint())
        btn_list.move(0, 0)
        btn_list.clicked.connect(self.testConnect)

        btn_list2 = QPushButton('Inscription', self)
        btn_list2.resize(btn_list2.sizeHint())
        btn_list2.move(0, 0)
        btn_list2.clicked.connect(self.testInsc)

        btn_quit = QPushButton('Quit', self)
        btn_quit.clicked.connect(QApplication.instance().quit)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(90, 100)

        Layout2.addRow("Pseudo", self.pseudo)
        Layout2.addRow("Mot de Passe", self.mdp)
        Layout.addLayout(Layout2)
        Layout.addWidget(btn_list)
        Layout.addWidget(btn_list2)
        Layout.addWidget(btn_quit)

        self.setGeometry(100, 100, 200, 150)
        self.setWindowTitle('Menu de connexion')
        self.setLayout(Layout)
        self.show()


    def testConnect(self):
        if(len(UserController.search_user(self.pseudo.text(),self.mdp.text()))!=0):
            BasicWindow.idUser = UserController.search_user(self.pseudo.text(),self.mdp.text())[0][0]
            self.principalWindow = general()
            self.principalWindow.show()

    def testInsc(self):
        self.inscriptionWindow = inscription()
        self.inscriptionWindow.show()


    