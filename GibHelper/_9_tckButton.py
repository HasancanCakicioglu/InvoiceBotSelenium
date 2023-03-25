from selenium.webdriver import Keys

from MyConstants.enum import waitSecond, withIDorXPATH, webDriverWaitEnum, scroolPosition
from Utility.scroolPage import scroolCount
from Utility.waiters import waitCode
from Utility.rulesPath.tcControl import tcKontrolFunc

def gelir_tckButton_FUNC(driver,tc :str):

    giveError = False
    tc = tc.split(".")[0]
    while True:

        tckButton = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.presence_of_element_located,
                             withIDorXPATH.by_id, "tcknVkn", "tck ",giveError)
        if tckButton is not None:
            break
        else:
            scroolCount(driver, 5, scroolPosition.UP.value)

    while True:
        tckButton.clear()
        if not tcKontrolFunc(tc):# eğer 1111111 ise buraya gir
            tckButton.clear()
        else:
            tckButton.send_keys(tc)

        if not tcKontrolFunc(tc):
            if tckButton.get_attribute("value") == "":
                break
        else:
            if tckButton.get_attribute("value") == tc:
                break


