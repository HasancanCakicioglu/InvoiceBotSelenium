from MyConstants.constantShelve import GoogleTextController
from PyQt5.QtWidgets import *
from Screens.resiminput import Ui_resiminput



class resiminputPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.resiminputForm = Ui_resiminput()
        self.resiminputForm.setupUi(self)

        self.resiminputForm.gonderButton.clicked.connect(self.gonderButtonFunc)

    def gonderButtonFunc(self):
        GoogleTextController.set_google_login_text(self.resiminputForm.lineEdit1.text())
