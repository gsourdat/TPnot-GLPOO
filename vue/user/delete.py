from PySide6.QtWidgets import QLabel, QVBoxLayout, QFormLayout, QLineEdit, QPushButton
from vue.window import BasicWindow
from controller.user_controller import UserController


class DeleteUserQt(BasicWindow):
    def __init__(self,id: str, show_vue: BasicWindow = None):
        super().__init__()
        self.user_id = id
        self.nom = QLabel()
        self.prenom = QLabel()
        self.pseudo = QLabel()
        self.mdp = QLabel()
        self.admin = QLabel()

        self.show_vue = show_vue
        self.setup()
        self.fillform()

    def setup(self):
        # Create an outer layout
        outerLayout = QVBoxLayout()
        # Create a form layout for the label and line edit
        Layout = QVBoxLayout()
        Layout.addWidget(self.nom)
        Layout.addWidget(self.prenom)
        Layout.addWidget(self.pseudo)
        Layout.addWidget(self.admin)

        # Add a label and a line edit to the form layout
        # Create a layout for the checkboxes
        ValidationLayout = QVBoxLayout()

        btn_delete = QPushButton('Delete User', self)
        btn_delete.clicked.connect(self.deleteUser)
        btn_delete.resize(btn_delete.sizeHint())
        btn_delete.move(90, 100)
        ValidationLayout.addWidget(btn_delete)

        # Add some checkboxes to the layout
        btn_cancel = QPushButton('Quit', self)
        btn_cancel.clicked.connect(self.quitEvent)
        btn_cancel.resize(btn_cancel.sizeHint())
        btn_cancel.move(90, 100)
        ValidationLayout.addWidget(btn_cancel)
        # Nest the inner layouts into the outer layout
        outerLayout.addLayout(Layout)
        outerLayout.addLayout(ValidationLayout)
        # Set the window's main layout
        self.setLayout(outerLayout)

    def deleteUser(self):
        # Show subscription formular
        UserController.delete_user(self.user_id)
        print("fait")
        if self.show_vue is not None:
            self.show_vue.refresh()
        self.close()

    def fillform(self):
        print(self.user_id)
        user = UserController.get_user(self.user_id)
        self.nom.setText(user[1])
        self.prenom.setText(user[2])
        self.pseudo.setText(user[3])
        if(user[5]==1):
            self.admin.setText("Administrateur")
        else:
            self.admin.setText("Utilisateur")
