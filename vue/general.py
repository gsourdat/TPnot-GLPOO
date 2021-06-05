from PySide6.QtWidgets import QListWidget, QGridLayout,  QVBoxLayout, QPushButton, QHBoxLayout

from vue.window import BasicWindow
from controller.user_controller import UserController


class general(BasicWindow):

    def __init__(self):
        super().__init__()
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
        #btn_list.clicked.connect(self.testConnect)

        btn_list2 = QPushButton('Rechercher Recette', self)
        btn_list2.resize(btn_list2.sizeHint())
        btn_list2.move(0, 0)
        #btn_list2.clicked.connect(self.list_user)

        Layout.addWidget(btn_list)
        Layout.addWidget(btn_list2)

        self.setGeometry(100, 100, 200, 150)
        self.setWindowTitle('Menu de connexion')
        self.setLayout(Layout)
        self.show()

