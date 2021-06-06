from PySide6.QtWidgets import QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QMessageBox,QComboBox
from PySide6.QtGui import QCloseEvent
from vue.window import BasicWindow
from controller.rec_controller import RecetteController
from vue.user.delete import DeleteUserQt
from vue.recette.afficher import AffRecQt
from vue.recette.afficher2 import AffListRecQt

class SearchRecAliQt(BasicWindow):

    def __init__(self, show_vue: BasicWindow = None):
        super().__init__()
        ##
        #self.nom = QLineEdit()
        self.AffRecWindow = None
        self.ingrédients = QLineEdit()
        self.show_vue = show_vue
        self.setup()

    def setup(self):
        # Create an outer layout
        outerLayout = QVBoxLayout()
        # Create a form layout for the label and line edit
        Layout = QFormLayout()
        # Add a label and a line edit to the form layout

        Layout.addRow("Ingrédient", self.ingrédients)

        # Create a layout for the checkboxes
        ValidationLayout = QVBoxLayout()

        btn_search = QPushButton('Rechercher Recette', self)
        btn_search.clicked.connect(self.searchRec)
        btn_search.resize(btn_search.sizeHint())
        btn_search.move(90, 100)
        ValidationLayout.addWidget(btn_search)
        # Add some checkboxes to the layout
        btn_cancel = QPushButton('Close', self)
        btn_cancel.clicked.connect(self.quitEvent)
        btn_cancel.resize(btn_cancel.sizeHint())
        btn_cancel.move(90, 100)
        ValidationLayout.addWidget(btn_cancel)
        # Nest the inner layouts into the outer layout
        outerLayout.addLayout(Layout)
        outerLayout.addLayout(ValidationLayout)
        # Set the window's main layout
        self.setLayout(outerLayout)

    def quitEvent(self, event: QCloseEvent):
        reply = QMessageBox.question(self, 'Message', 'Are you sure you want to quit ?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.close()
        else:
            event.ignore()

    def get_user_id(self, userfromlist:str):
        for member in self.members:
            if "* " + member['firstname'] + " " + member['lastname'] + " (" + member['email'] + ") - " + member['type'] == userfromlist:
                print(member['id'])
                return member['id']

    def searchRec(self):
        #user = RecetteController.search_recettefromNom(self.ingrédients.text())
        #print(user)
        if self.AffRecWindow is None:
            self.AffRecWindow = AffListRecQt(self.ingrédients.text())
        self.AffRecWindow.show()
        if self.show_vue is not None:
            self.show_vue.refresh()
        self.close()
