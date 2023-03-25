from time import sleep

from selenium.webdriver.common.by import By

from MyConstants.enum import waitSecond, withIDorXPATH, webDriverWaitEnum, scroolPosition
from Utility.scroolPage import scroolCount
from Utility.waiters import waitCode



def gelir_kdvOran_FUNC(driver):
    giveError = False
    while True:
        ihracKayitliSatisButton = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.presence_of_element_located,
                                 withIDorXPATH.by_id, "ihracKayitliSatis_input", "satisTuru_input", giveError)
        if ihracKayitliSatisButton is not None:
            ihracKayitliSatisButton.click()
            break
        else:
            scroolCount(driver, 5, scroolPosition.UP.value)

    sleep(0.3)
    while True:
        ihracKayitliSatisSelect = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.element_to_be_clickable,
                                 withIDorXPATH.by_id, "ihracKayitliSatis_listbox", "eArşivFatura ", giveError)
        if ihracKayitliSatisSelect is not None:
            break
        else:
            scroolCount(driver, 5, scroolPosition.DOWN.value)

    options = ihracKayitliSatisSelect.find_elements(By.TAG_NAME, "li")
    while ihracKayitliSatisButton.text != "701 - İHRACATI YAPILACAK NİHAİ ÜRÜNLERİN KANUNUN 11/1-c MADDESİ KAPSAMINDA TESLİMİ":
        for option in options:
            if option.text == "701 - İHRACATI YAPILACAK NİHAİ ÜRÜNLERİN KANUNUN 11/1-c MADDESİ KAPSAMINDA TESLİMİ":
                option.click()
                sleep(0.1)



