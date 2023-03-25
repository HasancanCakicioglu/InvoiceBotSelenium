from selenium.webdriver.common.by import By

from MyConstants.enum import waitSecond, withIDorXPATH, webDriverWaitEnum, scroolPosition
from Utility.scroolPage import scroolCount
from Utility.waiters import waitCode


def gelir_faturaSeriNoButton_FUNC(driver,seri_no:str):
    giveError = False
    while True:
        faturaSeriNoButton = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.presence_of_element_located,
                                  withIDorXPATH.by_id, "seriNo", "seriNo ",giveError)
        if faturaSeriNoButton is not None:
            break
        else:
            scroolCount(driver, 5, scroolPosition.UP.value)

    while True:
        faturaSeriNoButton.clear()
        faturaSeriNoButton.send_keys(seri_no)
        if faturaSeriNoButton.get_attribute("value") == seri_no:
            break
