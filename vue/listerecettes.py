import sys
from vue.window import BasicWindow
from controller.user_controller import UserController
from PySide6.QtWidgets import QMainWindow, QApplication, QTextEdit, QPushButton, QHBoxLayout, QWidget, QVBoxLayout,QToolTip, QLineEdit, QLabel, QCheckBox, QComboBox



class listerecettes(BasicWindow):
  def __init__(self):
    super().__init__()
    self.setUI()
        
  def setUI(self):
    zoneTexte=QTextEdit()
    btnOK=QPushButton("OK", self)
    zoneLigne=QLineEdit()
    label=QLabel("Champ texte")
    case=QCheckBox("Case", self)
    combo=QComboBox(self)
                
    btnOK.resize(btnOK.sizeHint())
    btnOK.setToolTip("Ceci est un bouton <i>OK</i>")
                
    combo.addItem("Choix 1")
    combo.addItem("Choix 2")
    combo.addItem("Choix 3")
    combo.addItem("Choix 4")
                
    hbox=QHBoxLayout()
    hbox.addStretch(1)
    hbox.addWidget(label)
    hbox.addWidget(zoneLigne)
    hbox.addWidget(zoneTexte)
    hbox.addWidget(btnOK)
    hbox.addWidget(case)
    hbox.addWidget(combo)
    vbox=QVBoxLayout()
                
    w=QWidget()
    w.setLayout(hbox)
    vbox.addWidget(w)
    #self.setCentralWidget(w)
                
    #Définition des actions
    #exitAction=QAction('&Exit', self)
    #exitAction.setShortcut('Ctrl-Q')
    #exitAction.setStatusTip("Quitter l'application")
    #exitAction.triggered.connect(qApp.exit)
                
    #☻menu=self.menuBar()
    #fichierMenu=menu.addMenu("&Fichier")
    #fichierMenu.addAction(exitAction)
                
    #self.barreOutils=self.addToolBar('Quitter')
    #self.barreOutils.addAction(exitAction)
                
    self.setGeometry(300,300,500,250)
    self.setWindowTitle('Fenêtre principale')
    self.setLayout(vbox)
    #self.statusBar().showMessage('Barre de statut')
    self.show()
        

