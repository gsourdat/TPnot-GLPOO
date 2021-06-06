from vue import recette
from PySide6.QtWidgets import QLabel, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QGridLayout, QListWidget,QHBoxLayout
from vue.window import BasicWindow
from controller.rec_controller import RecetteController


class AffListRecQt(BasicWindow):
    def __init__(self,ing: str, show_vue: BasicWindow = None):
        super().__init__()
        self.ing = ing
        self.outerLayout = QHBoxLayout()
        self.listlayout = QGridLayout()
        self.listwidget = QListWidget()
        self.member_mapping = {}
        self.show_vue = show_vue
        self.list()
        self.setup()

    def list(self):

        self.listwidget.clear()
        index = 0
        for member in  RecetteController.get_recettes_ing(self.ing):
            self.listwidget.insertItem(index, "%d - %s" % (
                member[1],
                member[2],))
            self.member_mapping[index] = member
            index += 1

        #self.listwidget.clicked.connect(self.clicked)
        self.listwidget.resize(self.listwidget.sizeHint())
        self.listwidget.move(0, 60)
        self.listlayout.addWidget(self.listwidget)
        self.outerLayout.addLayout(self.listlayout)


    def setup(self):
        # Create an outer layout
        # Create a form layout for the label and line edit


        # Add a label and a line edit to the form layout
        # Create a layout for the checkboxes
        ValidationLayout = QVBoxLayout()

        # Add some checkboxes to the layout
        btn_cancel = QPushButton('Quit', self)
        btn_cancel.clicked.connect(self.quitEvent)
        btn_cancel.resize(btn_cancel.sizeHint())
        btn_cancel.move(90, 100)
        ValidationLayout.addWidget(btn_cancel)
        # Nest the inner layouts into the outer layout
        self.outerLayout.addLayout(ValidationLayout)
        # Set the window's main layout
        self.setWindowTitle('Recette')
        self.setLayout(self.outerLayout)


