from MyConstants.enum import waitSecond, withIDorXPATH, webDriverWaitEnum, scroolPosition
from Utility.scroolPage import scroolCount
from Utility.waiters import waitCode


def gelir_temizle_2_Button_FUNC(driver):
    giveError = False
    while True:
        temizle_2_Button = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.element_to_be_clickable,
                            withIDorXPATH.by_className, "btn btn-warning pull-right mr-15 eButton", "soyad ",giveError)
        if temizle_2_Button[1] is not None:
            temizle_2_Button[1].click()
            break
        else:
            scroolCount(driver, 5, scroolPosition.UP.value)
