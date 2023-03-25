from selenium.webdriver import Keys

from MyConstants.enum import waitSecond, withIDorXPATH, webDriverWaitEnum, scroolPosition
from Utility.scroolPage import scroolCount
from Utility.waiters import waitCode


def gelir_soyadButton_FUNC(driver,aciklama:str):

    giveError = False
    while True:
        aciklamaButton = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.presence_of_element_located,
                               withIDorXPATH.by_id, "aciklama", "aciklama ",giveError)
        if  aciklamaButton is not None:
            break
        else:
            scroolCount(driver, 5, scroolPosition.UP.value)

    while True:
        aciklamaButton.clear()
        aciklamaButton.send_keys(aciklama)
        if aciklamaButton.get_attribute("value") == aciklama:
            break
