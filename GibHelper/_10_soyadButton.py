from selenium.webdriver import Keys

from MyConstants.enum import waitSecond, withIDorXPATH, webDriverWaitEnum, scroolPosition
from Utility.scroolPage import scroolCount
from Utility.waiters import waitCode


def gelir_soyadButton_FUNC(driver,firma_unavi:str):

    giveError = False
    while True:
        soyadButton = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.presence_of_element_located,
                               withIDorXPATH.by_id, "soyad", "soyad ",giveError)
        if  soyadButton is not None:
            break
        else:
            scroolCount(driver, 5, scroolPosition.UP.value)

    while True:
        soyadButton.clear()
        soyadButton.send_keys(firma_unavi.split(" ")[-1])
        if soyadButton.get_attribute("value") == firma_unavi.split(" ")[-1]:
            break
