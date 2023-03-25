from selenium.webdriver import Keys

from MyConstants.enum import waitSecond, withIDorXPATH, webDriverWaitEnum, scroolPosition
from Utility.scroolPage import scroolCount
from Utility.waiters import waitCode


def gelir_kaydetButton_FUNC(driver):
    giveError = False
    while True:
        kaydetButton = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.element_to_be_clickable,
                            withIDorXPATH.by_className, "btn btn-primary mt-20 mr-20 eButton", "kaydet button",giveError)
        if kaydetButton is not None:
            kaydetButton.click()
            break
        else:
            scroolCount(driver, 5, scroolPosition.UP.value)
