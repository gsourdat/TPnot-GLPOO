from vue.user.search import SearchUserQt
from PySide6.QtWidgets import QListWidget, QGridLayout,  QVBoxLayout, QPushButton, QHBoxLayout

#from vue.user.search import SearchUserQt
from vue.window import BasicWindow
from controller.rec_controller import RecetteController
from controller.user_controller import UserController
from vue.recette.delete import DeleteRecQt
from vue.recette.add import AddRecQt
from vue.recette.edit import EditRecQt
from vue.recette.afficher import AffRecQt
from vue.recette.search import SearchRecQt
from vue.recette.search2 import SearchRecAliQt
class ListAllRecQt(BasicWindow):

    def __init__(self):
        super().__init__()
        

        self.searchRecWindow = None
        self.searchRecAliWindow = None
        self.affRecWindow = None
        self.deleteRecWindow = None

        self.layout = QHBoxLayout()

        self.listlayout = QGridLayout()
        self.listwidget = QListWidget()

        self.btn_search_rec = QPushButton('Rechercher par le nom', self)
        self.btn_search_rec_ali = QPushButton('Rechercher par un aliment', self)
        self.btn_show = QPushButton('Afficher',self)
        if(UserController.get_user(BasicWindow.idUser)[5]==1):
            self.btn_del_rec = QPushButton('Supprimer',self)


        self.member_mapping = {}

        self.list()
        self.side_menu()
        self.setLayout(self.layout)

    def list(self):

        self.listwidget.clear()
        index = 0
        for member in RecetteController.list_recettes():
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

        self.btn_search_rec.resize(self.btn_search_rec.sizeHint())
        self.btn_search_rec.move(60, 60)
        self.btn_search_rec.setEnabled(True)
        self.btn_search_rec.clicked.connect(self.search_user)

        self.btn_search_rec_ali.resize(self.btn_search_rec_ali.sizeHint())
        self.btn_search_rec_ali.move(60, 60)
        self.btn_search_rec_ali.setEnabled(True)
        self.btn_search_rec_ali.clicked.connect(self.search_user_ali)

        self.btn_show.resize(self.btn_show.sizeHint())
        self.btn_show.move(60, 60)
        self.btn_show.setEnabled(False)
        self.btn_show.clicked.connect(self.afficher)

        if(UserController.get_user(BasicWindow.idUser)[5]==1):
            self.btn_del_rec.resize(self.btn_show.sizeHint())
            self.btn_del_rec.move(60, 60)
            self.btn_del_rec.setEnabled(False)
            self.btn_del_rec.clicked.connect(self.suppr)


        btn_quit = QPushButton('Close', self)
        btn_quit.clicked.connect(self.close)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(90, 100)

        buttonlayout = QVBoxLayout()
        buttonlayout.addWidget(self.btn_search_rec)
        buttonlayout.addWidget(self.btn_search_rec_ali)
        
        buttonlayout.addWidget(self.btn_show)
        if(UserController.get_user(BasicWindow.idUser)[5]==1):
            buttonlayout.addWidget(self.btn_del_rec)

        buttonlayout.addWidget(btn_quit)

        self.setGeometry(100, 100, 200, 150)
        self.setWindowTitle('Les Recettes')
        self.layout.addLayout(buttonlayout)

    def clicked(self):
        item = self.listwidget.currentItem()
        self.btn_show.setEnabled(True)
        self.btn_del_rec.setEnabled(True)
        print(item.text())

    def refresh(self):
        self.list()
        self.show()

    def afficher(self):
        if self.affRecWindow is None:
            user = self.member_mapping[self.listwidget.currentRow()]
            print(user)
            self.affRecWindow = AffRecQt(user[0], self)
        self.affRecWindow.show()

    
    def search_user_ali(self):
        if self.searchRecAliWindow is None:
            self.searchRecAliWindow = SearchRecAliQt(self)
        self.searchRecAliWindow.show()

    def search_user(self):
        if self.searchRecWindow is None:
            self.searchRecWindow = SearchRecQt(self)
        self.searchRecWindow.show()
    
    def suppr(self):
        if self.deleteRecWindow is None:
            user = self.member_mapping[self.listwidget.currentRow()]
            print(user)
            self.deleteRecWindow = DeleteRecQt(user[0], self)
        self.deleteRecWindow.show()

