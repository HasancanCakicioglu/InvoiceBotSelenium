from PyQt5.QtWidgets import *
from MyConstants import errorMessage
from Screens.errorPanel import Ui_errorPanel



class errorPanelPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.errorPanelForm = Ui_errorPanel()
        self.errorPanelForm.setupUi(self)
        self.errorPanelForm.hatamesaj.setText(errorMessage.errorMessageBox)









