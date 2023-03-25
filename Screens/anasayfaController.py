from PyQt5.QtWidgets import *

from MyConstants.enum import prgoramProcess
from Screens.anasayfa import Ui_Anasayfa
from Screens.genelayarlarController import genelAyarlarPage
from Screens.mypageController import myPage
from MyConstants.errorMessage import GibProcessHandler

class anasayfaPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.anasayfaForm = Ui_Anasayfa()
        self.anasayfaForm.setupUi(self)
        self.genelayar = genelAyarlarPage()
        self.mypag = myPage()
        self.anasayfaForm.pushButton.clicked.connect(self.goToGenelAyarlar)
        self.anasayfaForm.mainHasancanButton.clicked.connect(self.goToMyPage)


    def goToGenelAyarlar(self):
        self.genelayar.show()

    def goToMyPage(self):
        GibProcessHandler.set_process_handler(prgoramProcess.Start)
        self.mypag.show()
