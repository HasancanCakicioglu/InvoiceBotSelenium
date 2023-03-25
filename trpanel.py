from MyConstants.constantShelve import *
from Utility.waiters import *
from databaseDB.shelveDB import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Utility.time import *
from selenium.webdriver.common.action_chains import ActionChains
from PyQt5.QtWidgets import QMessageBox
from Utility.folder import getLastDownloadedFile
from MyConstants.enum import webDriverWaitEnum, withIDorXPATH, waitSecond


def trendyolPanel(tarih1,tarih2,Firma_kisa_kod,Kullanici_adi,sifre,myCallbackFixer):
    myDB = SingletonDB.getInstance()
    data = constantData()
    trendyolPanelLink = myDB.get(data.trendyol_panel_link)

    try:
        if myDB.get(data.browser) == browsers.Google_Chrome.value:
            chromePath = myDB.get(data.chrome_driver_path)
            driver_service = Service(executable_path=chromePath)
            driver = webdriver.Chrome(service=driver_service)
        elif myDB.get(data.browser) == browsers.Microsoft_Edge.value:
            edgePath = myDB.get(data.edge_driver_path)
            driver_service = Service(executable_path=edgePath)
            driver = webdriver.Edge(service=driver_service)
        else :
            driver = None

    except :
        QMessageBox.critical(None, "Error", "Hata! Genel Ayarlar Bölümünde Edge Driver Path Hatalı!")
        return

    driver.get(trendyolPanelLink)


    kod_button = waitCode(driver,waitSecond.low.value,webDriverWaitEnum.presence_of_element_located,withIDorXPATH.by_id,"txtCorporateCode","Trendyol Şirket Kısa Kodu ")
    kod_button.send_keys(Firma_kisa_kod)

    userName_Button = waitCode(driver,waitSecond.low.value,webDriverWaitEnum.presence_of_element_located,withIDorXPATH.by_id,"txtLoginName","Trendyol kullanıcı adı ")

    userName_Button.send_keys(Kullanici_adi)

    password_Button = waitCode(driver,waitSecond.low.value,webDriverWaitEnum.presence_of_element_located,withIDorXPATH.by_id,"txtLoginPassword","Trendyol şifre ")

    password_Button.send_keys(sifre)

    login_Button = waitCode(driver,waitSecond.low.value,webDriverWaitEnum.element_to_be_clickable,withIDorXPATH.by_id,"btnLogin","Trendyol giriş butonu")
    login_Button.click()

    login_Control = driver.find_element(By.ID, "divResult")

    if( login_Control.text == "Hatalı kullanıcı adı veya şifre." or login_Control.text=="Lütfen giriş bilgilerinizi giriniz"):
        QMessageBox.critical(None, "Error", "Hata! Trendyol Panele Girerken Kullanıcı adı Şifre veya Kod YANLIŞ")
        return

    rapor_Edilen_faturalar = waitCode(driver,waitSecond.long.value,webDriverWaitEnum.presence_of_element_located,withIDorXPATH.by_id,"tvMainMenu_N0_1_1","Trendyol panel rapor edilen faturalar sekmesi")
    #rapor_Edilen_faturalar = driver.find_element(By.ID, "tvMainMenu_N0_1_1")
    rapor_Edilen_faturalar.click()

    click_down_arrow_datepicker = waitCode(driver,waitSecond.low.value,webDriverWaitEnum.element_to_be_clickable,withIDorXPATH.by_id,"InvoiceFilterBeginDate_B-1","Trendyol başlangıç tarihi DownArrow ")
    #click_down_arrow_datepicker = driver.find_element(By.ID, "InvoiceFilterBeginDate_B-1")
    click_down_arrow_datepicker.click()

    sleep(1)
    month_year_text = waitCode(driver,waitSecond.low.value,webDriverWaitEnum.element_to_be_clickable,withIDorXPATH.by_id,"InvoiceFilterBeginDate_DDD_C_T","Trendyol ay yıl tarih")
    #month_year_text = driver.find_element(By.ID, "InvoiceFilterBeginDate_DDD_C_T")

    month_year_left_button = waitCode(driver,waitSecond.low.value,webDriverWaitEnum.element_to_be_clickable,withIDorXPATH.by_id,"InvoiceFilterBeginDate_DDD_C_PMC","Trendyol 1. tarih sol buton")
    #month_year_left_button = driver.find_element(By.ID, "InvoiceFilterBeginDate_DDD_C_PMC")

    month_year_right_button = waitCode(driver,waitSecond.low.value,webDriverWaitEnum.element_to_be_clickable,withIDorXPATH.by_id,"InvoiceFilterBeginDate_DDD_C_NMC","Trendyol 1. tarih sağ buton ")
    #month_year_right_button = driver.find_element(By.ID, "InvoiceFilterBeginDate_DDD_C_NMC")


    while month_year_text.text != format_date(tarih1):

        if compare_dates(tarih1, convert_dateTo_Number(month_year_text.text)) == -1:
            month_year_left_button.click()
        else:
            month_year_right_button.click()


    day_XPATH_1 = False
    for i in range(2, 8):
        for k in range(2, 9):

            #day_XPATH = waitCode(driver,waitSecond.low.value,webDriverWaitEnum.element_to_be_clickable,withIDorXPATH.by_xpath,f"/html/body/form/table[5]/tbody/tr[3]/td/div/table/tbody/tr/td[3]/div/div/div[3]/div[1]/table/tbody/tr[1]/td[3]/div[2]/div/div/div/table[2]/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr[{i}]/td[{k}]")

            day_XPATH = driver.find_element(By.XPATH,
                                            f"/html/body/form/table[5]/tbody/tr[3]/td/div/table/tbody/tr/td[3]/div/div/div[3]/div[1]/table/tbody/tr[1]/td[3]/div[2]/div/div/div/table[2]/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr[{i}]/td[{k}]")
            if day_XPATH.get_attribute("class") == "dxeCalendarDay_Metropolis dxeCalendarOtherMonth_Metropolis":
                continue

            if (day_XPATH.text == get_day(tarih1)):
                day_XPATH.click()
                day_XPATH_1 = True


    if day_XPATH_1 == False:
        QMessageBox.critical(None, "Error", "Tarih günü bulunamadı! | 1")
    # //////////////////////////////////////////////////////////////////////////////////////////////

    click_down_arrow_second_datepicker = waitCode(driver,waitSecond.low.value,webDriverWaitEnum.element_to_be_clickable,withIDorXPATH.by_id,"InvoiceFilterEndDate_B-1","Trendyol 2. tarih DownArrow ")
    #click_down_arrow_second_datepicker = driver.find_element(By.ID, "InvoiceFilterEndDate_B-1")
    click_down_arrow_second_datepicker.click()

    sleep(1)
    month_year_text_second = waitCode(driver,waitSecond.low.value,webDriverWaitEnum.element_to_be_clickable,withIDorXPATH.by_id,"InvoiceFilterEndDate_DDD_C_T","Trendyol 2. tarih ay yıl")
    #month_year_text_second = driver.find_element(By.ID, "InvoiceFilterEndDate_DDD_C_T")

    month_year_left_button_second = waitCode(driver,waitSecond.low.value,webDriverWaitEnum.element_to_be_clickable,withIDorXPATH.by_id,"InvoiceFilterEndDate_DDD_C_PMC","Trendyol 2. tarih sol buton")
    #month_year_left_button_second = driver.find_element(By.ID, "InvoiceFilterEndDate_DDD_C_PMC")

    month_year_right_button_second = waitCode(driver,waitSecond.low.value,webDriverWaitEnum.element_to_be_clickable,withIDorXPATH.by_id,"InvoiceFilterEndDate_DDD_C_NMC","Trendyol 2. tarih sağ buton ")
    #month_year_right_button_second = driver.find_element(By.ID, "InvoiceFilterEndDate_DDD_C_NMC")

    while month_year_text_second.text != format_date(tarih2):

        if compare_dates(tarih2, convert_dateTo_Number(month_year_text_second.text)) == -1:
            month_year_left_button_second.click()
        else:
            month_year_right_button_second.click()

    day_XPATH_2 = False
    for i in range(2, 8):
        for k in range(2, 9):
            #day_XPATH_second = waitCode(driver,waitSecond.low.value,webDriverWaitEnum.element_to_be_clickable,withIDorXPATH.by_xpath,f"/html/body/form/table[5]/tbody/tr[3]/td/div/table/tbody/tr/td[3]/div/div/div[3]/div[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/div[2]/div/div/div/table[2]/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr[{i}]/td[{k}]")
            day_XPATH_second = driver.find_element(By.XPATH,
                                                   f"/html/body/form/table[5]/tbody/tr[3]/td/div/table/tbody/tr/td[3]/div/div/div[3]/div[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/div[2]/div/div/div/table[2]/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr[{i}]/td[{k}]")
            if day_XPATH_second.get_attribute("class") == "dxeCalendarDay_Metropolis dxeCalendarOtherMonth_Metropolis":
                continue

            if day_XPATH_second.text == get_day(tarih2):
                day_XPATH_second.click()
                day_XPATH_2 = True
    if day_XPATH_2 == False:
        QMessageBox.critical(None, "Error", "Tarih günü bulunamadı! | 2 ")

    # /////////////////////////////////////////////////////////////////////////////////////////////////////

    sorgula_Button =waitCode(driver,waitSecond.low.value,webDriverWaitEnum.element_to_be_clickable,withIDorXPATH.by_id,"btnRefresh","Trendyol sorgula buton")
    #sorgula_Button = driver.find_element(By.ID, "btnRefresh")
    sorgula_Button.click()

    try:

        sleep(5)
        #first_bill = waitCode(driver,waitSecond.long.value,webDriverWaitEnum.visibility_of_element_located,withIDorXPATH.by_xpath,"/html/body/form/table[5]/tbody/tr[3]/td/div/table/tbody/tr/td[3]/div/div/table[2]/tbody/tr/td/table[1]/tbody/tr[4]/td[2]")
        stopTheCode()
        try:

            first_bill = driver.find_element(By.XPATH,
                                             "/html/body/form/table[5]/tbody/tr[3]/td/div/table/tbody/tr/td[3]/div/div/table[2]/tbody/tr/td/table[1]/tbody/tr[4]")
        except:
            sleep(5)
            first_bill = driver.find_element(By.XPATH,
                                             "/html/body/form/table[5]/tbody/tr[3]/td/div/table/tbody/tr/td[3]/div/div/table[2]/tbody/tr/td/table[1]/tbody/tr[4]")


        action = ActionChains(driver)
        action.context_click(first_bill).perform()
        sleep(2.5)
        stopTheCode()
        #secim = waitCode(driver,waitSecond.middle.value,webDriverWaitEnum.element_to_be_clickable,withIDorXPATH.by_xpath,"/html/body/form/table[5]/tbody/tr[3]/td/div/table/tbody/tr/td[3]/div/div/div[5]/div/div[1]/div/ul/li[7]/div[1]")
        secim = driver.find_element(By.XPATH,
                                   "/html/body/form/table[5]/tbody/tr[3]/td/div/table/tbody/tr/td[3]/div/div/div[5]/div/div[1]/div/ul/li[7]/div[1]")

        action.move_to_element(secim)
        action.perform()
        sleep(2.5)
        stopTheCode()
        #tum_kayitlari_sec =waitCode(driver,waitSecond.middle.value,webDriverWaitEnum.element_to_be_clickable,withIDorXPATH.by_xpath,"/html/body/form/table[5]/tbody/tr[3]/td/div/table/tbody/tr/td[3]/div/div/div[5]/div/div[3]/div/ul/li[1]/div")
        tum_kayitlari_sec = driver.find_element(By.XPATH,
                                               "/html/body/form/table[5]/tbody/tr[3]/td/div/table/tbody/tr/td[3]/div/div/div[5]/div/div[3]/div/ul/li[1]/div")

        action.click(tum_kayitlari_sec)
        action.perform()
    except NoSuchElementException:
        QMessageBox.critical(None, "Error", "Trendyol Panel Faturalar Bulunamadı !!")
        exit()

    sleep(3)
    xls_download_Button = waitCode(driver,waitSecond.middle.value,webDriverWaitEnum.element_to_be_clickable,withIDorXPATH.by_id,"exportToXLSButton")
    #csv_download_Button = driver.find_element(By.ID, "exportToCSVButton")
    xls_download_Button.click()

    myCallbackFixer()
    sleep(10)
















