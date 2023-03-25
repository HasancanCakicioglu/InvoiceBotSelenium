from selenium.webdriver import Keys

from MyConstants.enum import waitSecond, withIDorXPATH, webDriverWaitEnum, scroolPosition
from Utility.scroolPage import scroolCount
from Utility.waiters import waitCode


def gelir_satirEkleButton_FUNC(driver):
    giveError = False
    while True:
        satirEkleButton = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.element_to_be_clickable,
                            withIDorXPATH.by_xpath, "/html/body/div/main/div[2]/div/div[1]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div[2]/form/div[4]/div/button[1]", "btn btn-primary pull-right mr-15 eButton",giveError)
        if satirEkleButton is not None:
            satirEkleButton.click()
            break
        else:
            scroolCount(driver, 25, scroolPosition.DOWN.value)
