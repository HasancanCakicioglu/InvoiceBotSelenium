from selenium.webdriver.common.by import By

from MyConstants.enum import waitSecond, withIDorXPATH, webDriverWaitEnum, scroolPosition
from Utility.scroolPage import scroolCount
from Utility.waiters import waitCode


def gelir_faturaNoButton_FUNC(driver,fatura_no:str):



    giveError = False
    while True:
        faturaNoButton = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.presence_of_element_located,
                                  withIDorXPATH.by_id, "siraNo", "belgeTur ",giveError)
        if faturaNoButton is not None:
            break
        else:
            scroolCount(driver, 5, scroolPosition.UP.value)

    while True:
        faturaNoButton.clear()
        faturaNoButton.send_keys(fatura_no)
        if faturaNoButton.get_attribute("value") == fatura_no:
            break
