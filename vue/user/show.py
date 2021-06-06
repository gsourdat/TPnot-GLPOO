from vue.user.search import SearchUserQt
from PySide6.QtWidgets import QListWidget, QGridLayout,  QVBoxLayout, QPushButton, QHBoxLayout

from vue.user.delete import DeleteUserQt
#from vue.user.search import SearchUserQt
from vue.window import BasicWindow
from controller.user_controller import UserController
from vue.user.search import SearchUserQt


class ListUserQt(BasicWindow):

    def __init__(self):
        super().__init__()

        self.addUserWindow = None
        self.editUserWindow = None
        self.deleteUserWindow = None
        self.searchUserWindow = None
        self.layout = QHBoxLayout()

        self.listlayout = QGridLayout()
        self.listwidget = QListWidget()


        self.btn_delete_user = QPushButton('Delete user', self)
        self.btn_search_user = QPushButton('Search user', self)

        self.member_mapping = {}

        self.list()
        self.side_menu()
        self.setLayout(self.layout)

    def list(self):

        self.listwidget.clear()
        index = 0
        for member in UserController.list_users():
            self.listwidget.insertItem(index, "%d %s (%s %s)" % (
                member[0],
                member[1],
                member[2],
                member[3],))
            self.member_mapping[index] = member
            index += 1

        self.listwidget.clicked.connect(self.clicked)
        self.listwidget.resize(self.listwidget.sizeHint())
        self.listwidget.move(0, 60)
        self.listlayout.addWidget(self.listwidget)
        self.layout.addLayout(self.listlayout)

    def side_menu(self):

        self.btn_delete_user.resize(self.btn_delete_user.sizeHint())
        self.btn_delete_user.move(60, 60)
        self.btn_delete_user.setEnabled(False)
        self.btn_delete_user.clicked.connect(self.delete_user)

        self.btn_search_user.resize(self.btn_delete_user.sizeHint())
        self.btn_search_user.move(60, 80)
        self.btn_search_user.clicked.connect(self.search_user)

        btn_quit = QPushButton('Close', self)
        btn_quit.clicked.connect(self.close)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(90, 100)

        buttonlayout = QVBoxLayout()
        buttonlayout.addWidget(self.btn_delete_user)
        buttonlayout.addWidget(self.btn_search_user)
        buttonlayout.addWidget(btn_quit)

        self.setGeometry(100, 100, 200, 150)
        self.setWindowTitle('User menu')
        self.layout.addLayout(buttonlayout)

    def clicked(self):
        item = self.listwidget.currentItem()
        self.btn_delete_user.setEnabled(True)
        print(item.text())

    def refresh(self):
        self.list()
        self.show()

    def delete_user(self):
        if self.deleteUserWindow is None:
            user = self.member_mapping[self.listwidget.currentRow()]
            print(user)
            self.deleteUserWindow = DeleteUserQt(user[0], self)
        self.deleteUserWindow.show()

    def search_user(self):
        if self.searchUserWindow is None:
            self.searchUserWindow = SearchUserQt(self)
        self.searchUserWindow.show()
