from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PySide6.QtGui import QCloseEvent


class BasicWindow(QWidget):
<<<<<<< HEAD

=======
    idUser = None
>>>>>>> ba18cf895ac0a658a13cd6984568745dccb464bf
    def quitEvent(self, event: QCloseEvent):
        reply = QMessageBox.question(self, 'Message', 'Are you sure you want to quit ?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.close()
        else:
            event.ignore()

    def refresh(self):
        pass
