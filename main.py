import sys

from controller.user_controller import UserController
from PySide6.QtWidgets import QApplication
from vue.menu import MenuWindow

#https://realpython.com/python-pyqt-layout/
#https://www.learnpyqt.com/tutorials/creating-multiple-windows/


def run():
    # Init db
    #admin_controller = UserController()
<<<<<<< HEAD
=======
    
>>>>>>> ba18cf895ac0a658a13cd6984568745dccb464bf
    app = QApplication(sys.argv)

    menu = MenuWindow()

    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
