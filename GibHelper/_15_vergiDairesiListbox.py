from time import sleep

from selenium.webdriver.common.by import By

from MyConstants.enum import waitSecond, withIDorXPATH, webDriverWaitEnum, scroolPosition
from Utility.scroolPage import scroolCount
from Utility.waiters import waitCode


def gelir_vergiDairesiListbox_FUNC(driver):

    giveError = False
    while True:
        vergiDairesiButton = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.presence_of_element_located,
                                      withIDorXPATH.by_id, "vergiDairesi_input", "belgeTur ",giveError)
        if vergiDairesiButton is not None:
            vergiDairesiButton.click()
            break
        else:
            scroolCount(driver, 5, scroolPosition.UP.value)
    sleep(0.3)
    while True:
        vergiDairesiSelect = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.presence_of_element_located,
                                      withIDorXPATH.by_id, "vergiDairesi_listbox", "vergiDairesi_listbox ",giveError)
        if vergiDairesiSelect is not None:
            break
        else:
            scroolCount(driver, 5, scroolPosition.UP.value)
    options = vergiDairesiSelect.find_elements(By.TAG_NAME, "li")
    while vergiDairesiButton.text != "POTANSİYEL MÜKELLEF -1":
        for option in options:
            if option.text == " " or "":
                vergiDairesiButton.click()
                sleep(0.3)
            if option.text == "POTANSİYEL MÜKELLEF -1":
                option.click()
                sleep(0.3)
                break
