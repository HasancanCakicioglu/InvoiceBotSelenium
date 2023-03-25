from time import sleep

from selenium.webdriver.common.by import By

from MyConstants.enum import waitSecond, withIDorXPATH, webDriverWaitEnum, scroolPosition
from Utility.scroolPage import scroolCount
from Utility.waiters import waitCode



def gelir_kdvOran_FUNC(driver):
    giveError = False
    while True:
        kdvOranButton = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.presence_of_element_located,
                                 withIDorXPATH.by_id, "kdvOrani_input", "satisTuru_input", giveError)
        if kdvOranButton is not None:
            kdvOranButton.click()
            break
        else:
            scroolCount(driver, 5, scroolPosition.UP.value)

    sleep(0.3)
    while True:
        kdvOranSelect = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.element_to_be_clickable,
                                 withIDorXPATH.by_id, "kdvOrani_listbox", "eArşivFatura ", giveError)
        if kdvOranSelect is not None:
            break
        else:
            scroolCount(driver, 5, scroolPosition.DOWN.value)

    options = kdvOranSelect.find_elements(By.TAG_NAME, "li")
    while kdvOranButton.text != "18":
        for option in options:
            if option.text == "18":
                option.click()
                sleep(0.1)



