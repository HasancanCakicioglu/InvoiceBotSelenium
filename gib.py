from time import sleep

from pandas import DataFrame

from MyConstants.enum import scroolPosition
from Utility.modelCreater import dataFrameToModel
from MyConstants.constantShelve import *
from databaseDB.shelveDB import *
from Utility.scroolPage import scroolCount
from Utility.try_excep_helper import tryExceptHelperFunc
from Utility.rulesPath.tcControl import tcKontrolFunc
from Utility.rulesPath.nihaiVision import isEfatura

from GibHelper._1_ChoseBrowser import choseBrowserForGib
from GibHelper._2_Login_Kullanici_adi_LineEdit import login_kullanici_adi_LineEdit_Func
from GibHelper._3_Login_Sifre_LineEdit import login_sifre_lineEdit_FUNC
from GibHelper._4_login_resimkod import login_resimkod_FUNC
from GibHelper._5_login_girisButton import login_girisButton_FUNC
from GibHelper._6_gelir_waiter import gelir_waiter_FUNC
from GibHelper._7_gelir_bugunTarihButton import gelir_bugunTarihButton_FUNC
from GibHelper._8_gelir_BelgeTarihButton import gelir_belgeTarihButton_FUNC
from GibHelper._9_tckButton import gelir_tckButton_FUNC
from GibHelper._10_soyadButton import gelir_soyadButton_FUNC
from GibHelper._11_adButton import gelir_adButton_FUNC
from GibHelper._12_belgeTur import gelir_belgeTurButton_FUNC
from GibHelper._13_eArsivListboxButton import gelir_eArsivListboxButton_FUNC
from GibHelper._14_faturaNoButton import gelir_faturaNoButton_FUNC
from GibHelper._15_vergiDairesiListbox import gelir_vergiDairesiListbox_FUNC
from GibHelper._16_nihaiTuketiciButton import gelir_nihaiTuketiciCheckbox_FUNC
from GibHelper._17_satisTurButton import gelir_satisTurButton_FUNC
from GibHelper._18_gelirKayitButton import gelir_gelirKayit_FUNC
from GibHelper._19_gelirKayitAltButton import gelir_gelirKayitAlt_FUNC
from GibHelper._20_kdvButton import gelir_kdvButton_FUNC
from GibHelper._21_ihracKayitButton import gelir_ihracKayitButton_FUNC
from GibHelper._22_kdvOranButton import gelir_kdvOran_FUNC
from GibHelper._23_tutarButton import gelir_tutarButton_FUNC
from GibHelper.Buttons.temizleButton_1 import gelir_temizle_1_Button_FUNC
from GibHelper.Buttons.kaydetVeDevamEt import gelir_kaydetVeDevamEtButton_FUNC
from GibHelper._20_5_stopajSatimCheckbox import gelir_StopajCheckbox_FUNC
from GibHelper.Buttons.satirEkle import gelir_satirEkleButton_FUNC

def sleepFunction():
    sleep(0.2)


def gibFunc(myCallBack,df:DataFrame,isTest:bool = False):

    faturaModel = dataFrameToModel(df)
    myDB = SingletonDB.getInstance()
    myDB.openDB()
    data = constantData()
    gibLink = myDB.get(data.gib_link)
    driver = choseBrowserForGib(myDB,data)
    driver.get(gibLink)
    driver.maximize_window()

    login_kullanici_adi_LineEdit_Func(driver,myDB,data)
    login_sifre_lineEdit_FUNC(driver,myDB,data)
    login_resimkod_FUNC(driver)
    login_girisButton_FUNC(driver)

    myCallBack()

    for i in range(len(df)):

        tryExceptHelperFunc(lambda:gelir_waiter_FUNC(driver))


        tryExceptHelperFunc(lambda: gelir_bugunTarihButton_FUNC(driver,faturaModel[i].rapor_olusturma_tarihi))
        tryExceptHelperFunc(lambda: gelir_belgeTarihButton_FUNC(driver, faturaModel[i].rapor_olusturma_tarihi))

        tryExceptHelperFunc(lambda: gelir_tckButton_FUNC(driver, faturaModel[i].alici_vkn))
        if not tcKontrolFunc(faturaModel[i].alici_vkn):
            tryExceptHelperFunc(lambda: gelir_soyadButton_FUNC(driver, faturaModel[i].firma_unvani))
            tryExceptHelperFunc(lambda: gelir_adButton_FUNC(driver, faturaModel[i].firma_unvani))
            tryExceptHelperFunc(lambda: gelir_vergiDairesiListbox_FUNC(driver))
        # gelir_belgeTurButton_FUNC(driver)
        tryExceptHelperFunc(lambda: gelir_eArsivListboxButton_FUNC(driver,faturaModel[i].fatura_no,faturaModel[i].alici_vkn))
        tryExceptHelperFunc(lambda: gelir_faturaNoButton_FUNC(driver, faturaModel[i].fatura_no))
        if isEfatura(faturaModel[i].fatura_no) and tcKontrolFunc(faturaModel[i].alici_vkn):
            pass
        else:
            tryExceptHelperFunc(lambda: gelir_nihaiTuketiciCheckbox_FUNC(driver,1))#nihai tüktici

        scroolCount(driver, 10, scroolPosition.DOWN.value)
        sleep(1.5)
        # driver.execute_script("window.scrollBy(0, window.innerHeight / 2);")

        tryExceptHelperFunc(lambda: gelir_satisTurButton_FUNC(driver))
        tryExceptHelperFunc(lambda: gelir_gelirKayit_FUNC(driver))
        tryExceptHelperFunc(lambda: gelir_gelirKayitAlt_FUNC(driver))
        tryExceptHelperFunc(lambda: gelir_kdvButton_FUNC(driver))
        if isEfatura(faturaModel[i].fatura_no) and tcKontrolFunc(faturaModel[i].alici_vkn):
            tryExceptHelperFunc(lambda :gelir_StopajCheckbox_FUNC(driver))
        tryExceptHelperFunc(lambda: gelir_ihracKayitButton_FUNC(driver))
        tryExceptHelperFunc(lambda: gelir_kdvOran_FUNC(driver))
        tryExceptHelperFunc(lambda: gelir_tutarButton_FUNC(driver, faturaModel[i].fatura_tutari))


        if isTest:
            sleep(2)
            tryExceptHelperFunc(lambda: gelir_temizle_1_Button_FUNC(driver))
            scroolCount(driver, 15, scroolPosition.UP.value)
            sleep(1)
        else:
            sleep(1)
            tryExceptHelperFunc(lambda:gelir_satirEkleButton_FUNC(driver))
            scroolCount(driver, 25, scroolPosition.DOWN.value)
            sleep(1)
            tryExceptHelperFunc(lambda: gelir_kaydetVeDevamEtButton_FUNC(driver))
            sleep(1)
            scroolCount(driver, 15, scroolPosition.UP.value)


    myCallBack()
    sleep(5)
    driver.quit()
    myDB.close()