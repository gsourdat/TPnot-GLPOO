from PySide6.QtWidgets import QTextEdit, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QComboBox, QHBoxLayout,QGridLayout,QListWidget
from vue.window import BasicWindow
from controller.rec_controller import RecetteController


class AddRecQt(BasicWindow):

    def __init__(self, show_vue: BasicWindow = None):
        super().__init__()
        ##
        self.index=0
        self.nom = QLineEdit()
        self.desc = QTextEdit()
        self.listlayout = QGridLayout()
        self.listwidget = QListWidget()
        self.listlayout2 = QGridLayout()
        self.listwidget2 = QListWidget()
        self.btn_addAli = QPushButton('Ajouter', self)
        self.HLayout = QHBoxLayout()
        self.member_mapping = {}
        self.member_mapping2 = {}
        self.show_vue = show_vue
        self.list()
        self.setup()

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

        btn_add = QPushButton('Ajouter', self)
        btn_add.clicked.connect(self.addRec)
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
        self.btn_addAli.clicked.connect(self.addAli)
        self.btn_addAli.resize(btn_add.sizeHint())
        self.btn_addAli.move(90, 100)

        self.HLayout.addWidget(self.btn_addAli)
        self.listlayout.addWidget(self.listwidget2)
        self.HLayout.addLayout(self.listlayout2)
        
        outerLayout.addLayout(Layout)
        outerLayout.addLayout(self.HLayout)
        outerLayout.addLayout(ValidationLayout)
        # Set the window's main layout
        self.setLayout(outerLayout)

    def list(self):

        self.listwidget.clear()
        index = 0
        for member in RecetteController.get_ing():
            self.listwidget.insertItem(index, "%d - %s" % (
                member[0],
                member[1],))
            self.member_mapping[index] = member
            index += 1

        self.listwidget.clicked.connect(self.clicked)
        self.listwidget.resize(self.listwidget.sizeHint())
        self.listwidget.move(0, 60)
        self.listlayout.addWidget(self.listwidget)
        self.HLayout.addLayout(self.listlayout)

    def clicked(self):
        item = self.listwidget.currentItem()
        self.btn_addAli.setEnabled(True)
        print(item.text())

    def addRec(self):
        print(self.desc.toPlainText())
        RecetteController.create_recette(self.nom.text(),self.desc.toPlainText(),BasicWindow.idUser)
        members = RecetteController.search_recettefromAuteur(BasicWindow.idUser)
        idRecette = RecetteController.search_recettefromNom(self.nom.text())[0]
        #for i in range(len(self.member_mapping)):
        #    print(self.member_mapping[i][0])
        #    RecetteController.addIngtoRec(int(self.member_mapping2[i][0]),idRecette)
            
        print("Members: ")
        for member in members:
            print("%s - %s" % (
                member[0],
                member[1]))
        if self.show_vue is not None:
            self.show_vue.refresh()
        self.close()

    def addAli(self):
        #user = self.member_mapping[]
        listItems = self.listwidget.selectedItems()
        for item in listItems:
            self.listwidget.takeItem(self.listwidget.row(item))
 
        for item in listItems:
            self.listwidget2.addItem(item)
