from selenium.webdriver import Keys

from MyConstants.enum import waitSecond, withIDorXPATH, webDriverWaitEnum, scroolPosition
from Utility.scroolPage import scroolCount
from Utility.waiters import waitCode


def gelir_kaydetVeDevamEtButton_FUNC(driver):
    giveError = False
    while True:
        kaydetVeDevamEtButton = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.element_to_be_clickable,
                            withIDorXPATH.by_xpath, "/html/body/div/main/div[2]/div/div[1]/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/div[1]/div[4]/div/div/button", "kaydet ve devam et",giveError)
        if kaydetVeDevamEtButton is not None:
            kaydetVeDevamEtButton.click()
            break
        else:
            scroolCount(driver, 15, scroolPosition.DOWN.value)
