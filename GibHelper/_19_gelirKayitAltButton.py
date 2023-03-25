from time import sleep

from selenium.webdriver.common.by import By

from MyConstants.enum import waitSecond, withIDorXPATH, webDriverWaitEnum, scroolPosition
from Utility.scroolPage import scroolCount
from Utility.waiters import waitCode



def gelir_gelirKayitAlt_FUNC(driver):


    giveError = False
    while True:
        gelirKayitAltTuruButton = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.presence_of_element_located,
                                           withIDorXPATH.by_id, "gelirKayitAltTuru_input", "satisTuru_input", giveError)
        if gelirKayitAltTuruButton is not None:
            gelirKayitAltTuruButton.click()
            break
        else:
            scroolCount(driver, 5, scroolPosition.DOWN.value)
    sleep(0.3)
    while True:
        gelirKayitAltTuruSelect = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.presence_of_element_located,
                                           withIDorXPATH.by_id, "gelirKayitAltTuru_listbox", "eArşivFatura ",
                                        giveError)
        if gelirKayitAltTuruSelect is not None:
            break
        else:
            scroolCount(driver, 5, scroolPosition.DOWN.value)

    options = gelirKayitAltTuruSelect.find_elements(By.TAG_NAME, "li")
    while gelirKayitAltTuruButton.text != "Mal Satışı":
        for option in options:
            if option.text == " " or "":
                gelirKayitAltTuruButton.click()
                sleep(0.3)
            if option.text == "Mal Satışı":
                option.click()
                sleep(0.3)
                break
