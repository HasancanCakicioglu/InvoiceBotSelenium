from time import sleep

from MyConstants.enum import waitSecond, withIDorXPATH, webDriverWaitEnum, scroolPosition
from Utility.scroolPage import scroolCount
from Utility.waiters import waitCode



def gelir_StopajCheckbox_FUNC(driver):
    giveError = False
    while True:
        StopajCheckbox = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.presence_of_element_located,
                             withIDorXPATH.by_id, "isStopajliSatisVar", "isStopajliSatisVar", giveError)
        if StopajCheckbox is not None:
            break
        else:
            scroolCount(driver, 5, scroolPosition.DOWN.value)

    while StopajCheckbox.get_attribute("value") =="true":
        if StopajCheckbox.get_attribute("value")=="true":
            StopajCheckbox.click()
            sleep(0.1)