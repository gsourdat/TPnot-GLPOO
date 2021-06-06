from model.bdd import RecetteBDD
from PySide6.QtWidgets import QTextEdit, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QComboBox
from vue.window import BasicWindow
from controller.rec_controller import RecetteController


class EditRecQt(BasicWindow):

    def __init__(self, id: str, show_vue: BasicWindow = None):
        super().__init__()
        ##
        self.rec_id = id
        self.nom = QLineEdit()
        self.desc = QTextEdit()

        self.show_vue = show_vue
        self.setup()
        self.fillform()

    def setup(self):
        # Create an outer layout
        outerLayout = QVBoxLayout()
        # Create a form layout for the label and line edit
        Layout = QFormLayout()
        # Add a label and a line edit to the form layout

        Layout.addRow("Nom", self.nom)

        Layout.addRow("Description", self.desc)

        # Create a layout for the checkboxes
        ValidationLayout = QVBoxLayout()

        btn_add = QPushButton('Editer', self)
        btn_add.clicked.connect(self.EditRec)
        btn_add.resize(btn_add.sizeHint())
        btn_add.move(90, 100)
        ValidationLayout.addWidget(btn_add)
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

    def EditRec(self):
        print(self.desc.toPlainText())
        RecetteController.edit_recette(self.rec_id, self.nom.text(),self.desc.toPlainText())
        members = RecetteController.search_recettefromAuteur(BasicWindow.idUser)

        print("Members: ")
        for member in members:
            print("%s - %s" % (
                member[0],
                member[1]))
        if self.show_vue is not None:
            self.show_vue.refresh()
        self.close()

    def fillform(self):
        user = RecetteController.get_recettes(self.rec_id)
        self.nom.setText(user[1])
        self.desc.setText(user[2])
