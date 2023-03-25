from MyConstants.constantShelve import *
from databaseDB.shelveDB import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from PyQt5.QtWidgets import QMessageBox


def choseBrowserForGib(myDB : SingletonDB,data : constantData) ->webdriver:


    try:
        if myDB.get(data.browser) == browsers.Google_Chrome.value:
            chromePath = myDB.get(data.chrome_driver_path)
            driver_service = Service(executable_path=chromePath)
            driver = webdriver.Chrome(service=driver_service)

        elif myDB.get(data.browser) == browsers.Microsoft_Edge.value:
            edgePath = myDB.get(data.edge_driver_path)
            driver_service = Service(executable_path=edgePath)
            driver = webdriver.Edge(service=driver_service)
        else:
            driver = None

    except Exception as e:
        print("hata = "+str(e))
        QMessageBox.critical(None, "Error", "Hata! Genel Ayarlar Bölümünde Edge Driver Path Hatalı!")
        return

    return driver