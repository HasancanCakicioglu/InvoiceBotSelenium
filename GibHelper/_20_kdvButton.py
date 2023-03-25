from time import sleep

from MyConstants.enum import waitSecond, withIDorXPATH, webDriverWaitEnum, scroolPosition
from Utility.scroolPage import scroolCount
from Utility.waiters import waitCode



def gelir_kdvButton_FUNC(driver):
    giveError = False
    while True:
        kdvButton = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.presence_of_element_located,
                             withIDorXPATH.by_id, "isKdvDahil", "isKdvDahil ", giveError)
        if kdvButton is not None:
            break
        else:
            scroolCount(driver, 5, scroolPosition.DOWN.value)
    while kdvButton.get_attribute("value") =="false":
        if kdvButton.get_attribute("value")=="false":
            kdvButton.click()
            sleep(0.1)

