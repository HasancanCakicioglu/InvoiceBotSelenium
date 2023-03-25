from PyQt5.QtWidgets import QApplication
from Screens.anasayfaController import anasayfaPage


app = QApplication([])
pencere = anasayfaPage()
pencere.show()
app.exec_()



