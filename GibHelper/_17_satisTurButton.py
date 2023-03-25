from time import sleep

from MyConstants.enum import waitSecond, withIDorXPATH, webDriverWaitEnum, scroolPosition
from Utility.scroolPage import scroolCount
from Utility.waiters import waitCode
from selenium.webdriver.common.by import By

def gelir_satisTurButton_FUNC(driver):
    giveError = False
    while True:
        satisTuruButton = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.presence_of_element_located,
                                   withIDorXPATH.by_id, "satisTuru_input", "satisTuru_input",giveError)
        if satisTuruButton is not None:
            satisTuruButton.click()
            break
        else:
            scroolCount(driver, 5, scroolPosition.UP.value)
    sleep(0.3)
    while True:
        satisTuruSelect = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.presence_of_element_located,
                                   withIDorXPATH.by_id, "satisTuru_listbox", "satisTuruSelect ", giveError)
        if satisTuruSelect is not None:
            break
        else:
            scroolCount(driver, 5, scroolPosition.DOWN.value)

    options = satisTuruSelect.find_elements(By.TAG_NAME, "li")
    while satisTuruButton.text != "Normal Satışlar":
        for option in options:
            if option.text == " " or "":
                satisTuruButton.click()
                sleep(0.3)
            if option.text == "Normal Satışlar":
                option.click()
                sleep(0.3)
                break

