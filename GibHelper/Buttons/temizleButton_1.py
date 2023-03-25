from time import sleep

from MyConstants.enum import waitSecond, withIDorXPATH, webDriverWaitEnum, scroolPosition
from Utility.scroolPage import scroolCount
from Utility.waiters import waitCode


def gelir_temizle_1_Button_FUNC(driver):
    giveError = False
    while True:
        temizle_1_Button = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.element_to_be_clickable,
                            withIDorXPATH.by_xpath, '//button[contains(text(), "Temizle")]', "soyad ",giveError)


        if temizle_1_Button is not None:
            driver.execute_script("arguments[0].click();", temizle_1_Button)
            break
        else:
            scroolCount(driver,20, scroolPosition.UP.value)
            sleep(1)
