
from MyConstants.enum import waitSecond, withIDorXPATH, webDriverWaitEnum, scroolPosition
from Utility.scroolPage import scroolCount
from Utility.waiters import waitCode


def gelir_ihracKayitButton_FUNC(driver):
    giveError = False
    while True:
        IhracKayitliSatisButton = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.presence_of_element_located,
                                           withIDorXPATH.by_id, "isIhracKayitliSatisVar", "isKdvDahil ", giveError)
        if IhracKayitliSatisButton is not None:
            break
        else:
            scroolCount(driver, 5, scroolPosition.DOWN.value)
    while IhracKayitliSatisButton.get_attribute("value") == "true":

        if IhracKayitliSatisButton.get_attribute("value") == "true":
            IhracKayitliSatisButton.click()


# vardır