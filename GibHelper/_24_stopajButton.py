from time import sleep

from selenium.webdriver.common.by import By

from MyConstants.enum import waitSecond, withIDorXPATH, webDriverWaitEnum, scroolPosition
from Utility.scroolPage import scroolCount
from Utility.waiters import waitCode



def gelir_kdvOran_FUNC(driver):
    giveError = False
    while True:
        stopajButton = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.presence_of_element_located,
                                 withIDorXPATH.by_id, "stopaj_input", "stopaj_input", giveError)
        if stopajButton is not None:
            stopajButton.click()
            break
        else:
            scroolCount(driver, 5, scroolPosition.UP.value)

    sleep(0.3)
    while True:
        stopajSelect = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.element_to_be_clickable,
                                 withIDorXPATH.by_id, "stopaj_listbox", "stopaj_listbox", giveError)
        if stopajSelect is not None:
            break
        else:
            scroolCount(driver, 5, scroolPosition.DOWN.value)

    options = stopajSelect.find_elements(By.TAG_NAME, "li")
    while stopajButton.text != "013-Kıdem Tazminatı":
        for option in options:
            if option.text == "013-Kıdem Tazminatı":
                option.click()
                sleep(0.1)



