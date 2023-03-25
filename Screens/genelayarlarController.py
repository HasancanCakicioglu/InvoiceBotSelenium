from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from Screens.genelayarlar import Ui_GenelAyarlar
from databaseDB.shelveDB import *
from MyConstants.constantShelve import *

class genelAyarlarPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.genelAyarlarForm = Ui_GenelAyarlar()
        self.genelAyarlarForm.setupUi(self)
        self.readyData()

        self.genelAyarlarForm.kaydetButton.clicked.connect(self.kaydetButton)
        self.setWindowIcon(QtGui.QIcon("icon/hackers.png"))


    def readyData(self):
        myDb = SingletonDB.getInstance()
        data = constantData()

        self.genelAyarlarForm.lineEditChrome.setText(myDb.get(data.chrome_driver_path))
        self.genelAyarlarForm.lineEditEdge.setText(myDb.get(data.edge_driver_path))
        self.genelAyarlarForm.lineEditGibKullaniciAdi.setText(myDb.get(data.gib_kullanici_adi) if myDb.get(data.gib_kullanici_adi) else "")
        self.genelAyarlarForm.lineEditGibSifre.setText(myDb.get(data.gib_sifre) if myDb.get(data.gib_sifre) else "")
        self.genelAyarlarForm.lineEditIndirilenPath.setText(myDb.get(data.indirilen_path))
        self.genelAyarlarForm.lineEditGibLink.setText(myDb.get(data.gib_link))
        self.genelAyarlarForm.lineEditTrendyolPanelLink.setText(myDb.get(data.trendyol_panel_link))
        self.genelAyarlarForm.browserComboBox.setCurrentText(myDb.get(data.browser))


    def kaydetButton(self):
        myDb = SingletonDB.getInstance()
        data = constantData()

        myDb.set(data.chrome_driver_path,self.genelAyarlarForm.lineEditChrome.text())
        myDb.set(data.edge_driver_path, self.genelAyarlarForm.lineEditEdge.text())
        myDb.set(data.gib_kullanici_adi, self.genelAyarlarForm.lineEditGibKullaniciAdi.text())
        myDb.set(data.gib_sifre, self.genelAyarlarForm.lineEditGibSifre.text())
        myDb.set(data.indirilen_path, self.genelAyarlarForm.lineEditIndirilenPath.text())
        myDb.set(data.gib_link, self.genelAyarlarForm.lineEditGibLink.text())
        myDb.set(data.trendyol_panel_link, self.genelAyarlarForm.lineEditTrendyolPanelLink.text())
        myDb.set(data.browser, self.genelAyarlarForm.browserComboBox.currentText())

        myDb.close()
        self.close()






