import os

import xlrd
from PyQt5.QtWidgets import *
from pandas import DataFrame
from Screens.mypage import Ui_My
from gib import gibFunc
from trpanel import *
import threading
from MyConstants.enum import prgoramProcess
from MyConstants.errorMessage import ProgramProcessHandler
from Screens.resiminputController import resiminputPage
from PyQt5.QtCore import Qt
import pandas as pd
#################################


class myPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.myPageForm = Ui_My()
        self.myPageForm.setupUi(self)
        self.resimP = resiminputPage()

        self.myPageForm.BaslatButton.clicked.connect(self.BaslatButtonTrendyolPanel)
        self.myPageForm.BaslatButtonBaslatGib.clicked.connect(self.BaslatButtonGib)
        self.myPageForm.pushButtonFolderSelecter.clicked.connect(self.FolderSelecter)
        self.myPageForm.pushButtonTest.clicked.connect(self.testButton)
        self.myPageForm.BaslatButtonBaslatGib.setEnabled(True)
        self.myPageForm.pushButtonTest.setEnabled(True)

    def testButton(self):
        self.myPageForm.BaslatButtonBaslatGib.setEnabled(False)
        if GibProcessHandler.get_process_handler() == prgoramProcess.Stop.value:

            self.myPageForm.BaslatButtonBaslatGib.setText("GibHelper Durdur")
            GibProcessHandler.set_process_handler(prgoramProcess.Continue)
            return None

        if GibProcessHandler.get_process_handler() == prgoramProcess.Continue.value:

            self.myPageForm.BaslatButtonBaslatGib.setText("GibHelper Devam Et")
            GibProcessHandler.set_process_handler(prgoramProcess.Stop)
            return None
        if GibProcessHandler.get_process_handler() == prgoramProcess.Start.value:

            def callbackFixer():
                GibProcessHandler.set_process_handler(prgoramProcess.Stop)
                self.myPageForm.BaslatButtonBaslatGib.setText("GibHelper Devam Et")

            self.myPageForm.BaslatButtonBaslatGib.setText("GibHelper Durdur")
            GibProcessHandler.set_process_handler(prgoramProcess.Continue)

            self.openResimPanel()
            df = self.getDataAsDataFrameFromQTableWidget()
            g = threading.Thread(target=gibFunc,args=(callbackFixer,df,True))
            g.start()
    def closeTheWindow(self,thread):
        if thread:
            cc = threading.Thread(target=self.close(), name="error", daemon=True)
            cc.start()
        else:
            self.close()

    def FolderSelecter(self):

        file_filter = 'Data File (*.xlsx *.csv *.dat);; Excel File (*.xlsx *.xls)'
        file, _ = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a data file',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='Excel File (*.xlsx *.xls)'
        )

        self.lineEditSetText(file)
        self.writeToQTableWidget(self.getPDdata())



    def writeToQTableWidget(self,df:DataFrame):

        try:
            for row in range(len(df)):
                for col in range(len(df.columns)):
                    if col % len(df.columns) == 0:
                        item = QTableWidgetItem(str(df.iloc[row, col]))
                        item.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
                        item.setCheckState(Qt.CheckState.Checked)
                        self.myPageForm.tableWidgetFaturalar.setItem(row, col, item)
                    else:
                        self.myPageForm.tableWidgetFaturalar.setItem(row, col, QTableWidgetItem(str(df.iloc[row, col])))


            for i, column_name in enumerate(df.columns):
                item = QTableWidgetItem(column_name)
                self.myPageForm.tableWidgetFaturalar.setHorizontalHeaderItem(i, item)
        except:
            pass

    def getDataAsDataFrameFromQTableWidget(self)->DataFrame:
        rows = self.myPageForm.tableWidgetFaturalar.rowCount()
        cols = self.myPageForm.tableWidgetFaturalar.columnCount()
        checked = False
        data = []
        for row in range(rows):
            row_data = []
            checked = False
            for col in range(cols):
                item = self.myPageForm.tableWidgetFaturalar.item(row, col)
                if item.checkState() == Qt.CheckState.Checked:
                    checked = True
                row_data.append(item.text())

            if checked:
                data.append(row_data)
        df = pd.DataFrame(data,columns=[self.myPageForm.tableWidgetFaturalar.horizontalHeaderItem(i).text() for i in range(cols)])

        return df

    def lineEditSetText(self,path):
        self.myPageForm.lineEditFolderName.setText(path)


    def getPDdata(self):

        df = None
        try:
            file_name = self.myPageForm.lineEditFolderName.text()
            wb = xlrd.open_workbook(file_name, logfile=open(os.devnull, 'w'))
            df = pd.read_excel(io=wb,engine='xlrd')
        except Exception as e:
            print("hata = " + str(e))

        self.myPageForm.tableWidgetFaturalar.setRowCount(len(df)-1)
        self.myPageForm.tableWidgetFaturalar.setColumnCount(len(df.columns))
        df['Rapor Oluşturulma Tarihi'] = pd.to_datetime(df['Rapor Oluşturulma Tarihi'], format='%d.%m.%Y %H:%M:%S')
        df = df.sort_values(by='Rapor Oluşturulma Tarihi')

        return df



    def BaslatButtonGib(self):
        self.myPageForm.pushButtonTest.setEnabled(False)
        if GibProcessHandler.get_process_handler() == prgoramProcess.Stop.value:

            self.myPageForm.BaslatButtonBaslatGib.setText("GibHelper Durdur")
            GibProcessHandler.set_process_handler(prgoramProcess.Continue)
            return None

        if GibProcessHandler.get_process_handler() == prgoramProcess.Continue.value:

            self.myPageForm.BaslatButtonBaslatGib.setText("GibHelper Devam Et")
            GibProcessHandler.set_process_handler(prgoramProcess.Stop)
            return None
        if GibProcessHandler.get_process_handler() == prgoramProcess.Start.value:

            def callbackFixer():
                GibProcessHandler.set_process_handler(prgoramProcess.Stop)
                self.myPageForm.BaslatButtonBaslatGib.setText("GibHelper Devam Et")

            self.myPageForm.BaslatButtonBaslatGib.setText("GibHelper Durdur")
            GibProcessHandler.set_process_handler(prgoramProcess.Continue)

            self.openResimPanel()
            df = self.getDataAsDataFrameFromQTableWidget()
            g = threading.Thread(target=gibFunc,args=(callbackFixer,df,False))
            g.start()


    def fillQTableWidget(self):
        for row in range(3):
            for col in range(3):
                if col % 3 == 0:
                    item = QTableWidgetItem("Item {0}-{1}".format(row, col))
                    item.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
                    item.setCheckState(Qt.CheckState.Unchecked)
                    self.myPageForm.tableWidgetFaturalar.setItem(row, col, item)
                else:
                    self.myPageForm.tableWidgetFaturalar.setItem(row, col,
                                                                 QTableWidgetItem("Item {0}-{1}".format(row, col)))

    def openResimPanel(self):
        self.resimP.show()



    def BaslatButtonTrendyolPanel(self):

        if ProgramProcessHandler.get_process_handler() == prgoramProcess.Stop.value:

            self.myPageForm.BaslatButton.setText("Durdur")
            ProgramProcessHandler.set_process_handler(prgoramProcess.Continue)
            return None

        if ProgramProcessHandler.get_process_handler() == prgoramProcess.Continue.value:

            self.myPageForm.BaslatButton.setText("Devam Et")
            ProgramProcessHandler.set_process_handler(prgoramProcess.Stop)
            return None

        if ProgramProcessHandler.get_process_handler() == prgoramProcess.Start.value:

            startTime = self.myPageForm.lineEditStartTime.text()
            finisTime = self.myPageForm.lineEditFinishTime.text()
            trendyolkod = self.myPageForm.lineEditKod.text()
            trendyolKullaniciAdi = self.myPageForm.lineEditKullaniciAdi.text()
            trendyolSifre = self.myPageForm.lineEditSifre.text()

            self.myPageForm.BaslatButton.setText("Durdur")
            ProgramProcessHandler.set_process_handler(prgoramProcess.Continue)


            def callbackFixer():
                ProgramProcessHandler.set_process_handler(prgoramProcess.Start)
                self.myPageForm.BaslatButton.setText("Başlat")

            t = threading.Thread(target=trendyolPanel,
                                 args=(startTime,finisTime,trendyolkod, trendyolKullaniciAdi,trendyolSifre,callbackFixer))
            t.start()

            return None
        return None









