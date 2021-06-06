from vue import recette
from PySide6.QtWidgets import QLabel, QVBoxLayout, QFormLayout, QLineEdit, QPushButton
from vue.window import BasicWindow
from controller.rec_controller import RecetteController


class AffRecQt(BasicWindow):
    def __init__(self,id: str, show_vue: BasicWindow = None):
        super().__init__()
        self.rec_id = id
        self.nom = QLabel()
        self.desc = QLabel()
        self.ing = QLabel()
        self.ing.setText("Ingrédients :")
        self.show_vue = show_vue
        self.setup()
        self.fillform()

    def setup(self):
        # Create an outer layout
        outerLayout = QVBoxLayout()
        # Create a form layout for the label and line edit
        Layout = QVBoxLayout()
        Layout.addWidget(self.nom)
        Layout.addWidget(self.desc)
        Layout.addWidget(self.ing)
        for i in range(len(RecetteController.getIngRec(self.rec_id))):
            
            ing = QLabel()
            ing.setText(RecetteController.getIngRec(self.rec_id)[i][1])
            Layout.addWidget(ing)
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

        outerLayout.addLayout(Layout)
        outerLayout.addLayout(ValidationLayout)
        # Set the window's main layout
        self.setWindowTitle('Recette')
        self.setLayout(outerLayout)


    def fillform(self):
        print(self.rec_id)
        user = RecetteController.get_recettes(self.rec_id)
        self.nom.setText(user[1])
        self.desc.setText(user[2])

