from selenium.webdriver import Keys

from MyConstants.enum import waitSecond, withIDorXPATH, webDriverWaitEnum, scroolPosition
from Utility.scroolPage import scroolCount
from Utility.waiters import waitCode


def gelir_adButton_FUNC(driver,firma_unavi:str):
    giveError = False
    while True:
        adButton = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.presence_of_element_located,
                            withIDorXPATH.by_id, "ad", "soyad ",giveError)
        if adButton is not None:
            break
        else:
            scroolCount(driver, 5, scroolPosition.UP.value)

    while True:
        adButton.clear()
        splitted_s = firma_unavi.split()
        joined_s = ' '.join(splitted_s[:-1])
        adButton.send_keys(joined_s)
        if adButton.get_attribute("value") == joined_s:
            break