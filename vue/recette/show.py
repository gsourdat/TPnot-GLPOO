from vue.user.search import SearchUserQt
from PySide6.QtWidgets import QListWidget, QGridLayout,  QVBoxLayout, QPushButton, QHBoxLayout

#from vue.user.search import SearchUserQt
from vue.window import BasicWindow
from controller.rec_controller import RecetteController
from vue.recette.delete import DeleteRecQt
from vue.recette.add import AddRecQt
from vue.recette.edit import EditRecQt

class ListRecQt(BasicWindow):

    def __init__(self):
        super().__init__()
        
        self.addRecWindow = None
        self.editRecWindow = None
        self.deleteRecWindow = None
        #self.searchRecWindow = None
        self.layout = QHBoxLayout()

        self.listlayout = QGridLayout()
        self.listwidget = QListWidget()

        self.btn_add_rec = QPushButton('Ajouter', self)
        self.btn_edit_rec = QPushButton('Editer', self)
        self.btn_delete_rec = QPushButton('Supprimer', self)
        #self.btn_search_rec = QPushButton('Rechercher', self)

        self.member_mapping = {}

        self.list()
        self.side_menu()
        self.setLayout(self.layout)

    def list(self):

        self.listwidget.clear()
        index = 0
        for member in RecetteController.search_recettefromAuteur(BasicWindow.idUser):
            self.listwidget.insertItem(index, "%d - %s" % (
                member[0],
                member[1],))
            self.member_mapping[index] = member
            index += 1

        self.listwidget.clicked.connect(self.clicked)
        self.listwidget.resize(self.listwidget.sizeHint())
        self.listwidget.move(0, 60)
        self.listlayout.addWidget(self.listwidget)
        self.layout.addLayout(self.listlayout)

    def side_menu(self):

        self.btn_delete_rec.resize(self.btn_delete_rec.sizeHint())
        self.btn_delete_rec.move(60, 60)
        self.btn_delete_rec.setEnabled(False)
        self.btn_delete_rec.clicked.connect(self.delete_user)

        self.btn_add_rec.resize(self.btn_delete_rec.sizeHint())
        self.btn_add_rec.move(60, 60)
        self.btn_add_rec.setEnabled(True)
        self.btn_add_rec.clicked.connect(self.add_user)

        self.btn_edit_rec.resize(self.btn_delete_rec.sizeHint())
        self.btn_edit_rec.move(60, 60)
        self.btn_edit_rec.setEnabled(False)
        self.btn_edit_rec.clicked.connect(self.edit_user)

        #self.btn_search_rec.resize(self.btn_delete_rec.sizeHint())
        #self.btn_search_rec.move(60, 80)
        #self.btn_search_user.clicked.connect(self.search_user)

        btn_quit = QPushButton('Close', self)
        btn_quit.clicked.connect(self.close)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(90, 100)

        buttonlayout = QVBoxLayout()
        buttonlayout.addWidget(self.btn_add_rec)
        buttonlayout.addWidget(self.btn_edit_rec)
        buttonlayout.addWidget(self.btn_delete_rec)
        buttonlayout.addWidget(btn_quit)

        self.setGeometry(100, 100, 200, 150)
        self.setWindowTitle('Mes Recettes')
        self.layout.addLayout(buttonlayout)

    def clicked(self):
        item = self.listwidget.currentItem()
        self.btn_delete_rec.setEnabled(True)
        self.btn_edit_rec.setEnabled(True)
        print(item.text())

    def refresh(self):
        self.list()
        self.show()

    def delete_user(self):
        if self.deleteRecWindow is None:
            user = self.member_mapping[self.listwidget.currentRow()]
            print(user)
            self.deleteRecWindow = DeleteRecQt(user[0], self)
        self.deleteRecWindow.show()

    def add_user(self):
        if self.addRecWindow is None:
            print("ee")
            self.addRecWindow = AddRecQt(self)
        self.addRecWindow.show()
    
    def edit_user(self):
        if self.editRecWindow is None:
            user = self.member_mapping[self.listwidget.currentRow()]
            print(user)
            self.editRecWindow = EditRecQt(user[0], self)
        self.editRecWindow.show()

    def search_user(self):
        if self.searchUserWindow is None:
            self.searchUserWindow = SearchUserQt(self)
        self.searchUserWindow.show()
