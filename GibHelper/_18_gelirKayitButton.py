from time import sleep

from selenium.webdriver.common.by import By

from MyConstants.enum import waitSecond, withIDorXPATH, webDriverWaitEnum, scroolPosition
from Utility.scroolPage import scroolCount
from Utility.waiters import waitCode


def gelir_gelirKayit_FUNC(driver):
    giveError = False
    while True:
        gelirKayitTuruButton = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.element_to_be_clickable,
                                        withIDorXPATH.by_id, "gelirKayitTuru_input", "satisTuru_input", giveError)
        if gelirKayitTuruButton is not None:
            gelirKayitTuruButton.click()
            break
        else:
            scroolCount(driver, 5, scroolPosition.DOWN.value)
    sleep(0.3)
    while True:
        gelirKayitTuruSelect = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.element_to_be_clickable,
                                        withIDorXPATH.by_id, "gelirKayitTuru_listbox", "gelirKayitTuru_listbox ", giveError)
        if gelirKayitTuruSelect is not None:
            break
        else:
            scroolCount(driver, 5, scroolPosition.DOWN.value)

    options = gelirKayitTuruSelect.find_elements(By.TAG_NAME, "li")
    while gelirKayitTuruButton.text != "Mal Satışı":
        for option in options:
            if option.text == " " or "":
                gelirKayitTuruButton.click()
                sleep(0.3)
            if option.text == "Mal Satışı":
                option.click()
                sleep(0.3)
                break


