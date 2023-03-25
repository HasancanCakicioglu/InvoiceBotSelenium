from time import sleep
from selenium.webdriver.common.by import By
from MyConstants.enum import waitSecond, withIDorXPATH, webDriverWaitEnum, scroolPosition
from Utility.scroolPage import scroolCount
from Utility.waiters import waitCode
from Utility.rulesPath.nihaiVision import isEfatura
from Utility.rulesPath.tcControl import tcKontrolFunc
def gelir_eArsivListboxButton_FUNC(driver,fatura_no:str,tc:str):
    giveError = False
    while True:
        belgeTurButton = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.element_to_be_clickable,
                                  withIDorXPATH.by_id, "gelirBelgeTuru_input", "belgeTur ",giveError)
        if belgeTurButton is not None:
            belgeTurButton.click()
            break
        else:
            scroolCount(driver, 5, scroolPosition.UP.value)

    sleep(0.3)
    while True:
        eArsivButton = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.presence_of_element_located,
                                withIDorXPATH.by_id, "gelirBelgeTuru_listbox", "eArşivFatura ")
        if eArsivButton is not None:
            break
        else:
            scroolCount(driver, 5, scroolPosition.UP.value)

    options = eArsivButton.find_elements(By.TAG_NAME, "li")
    sayac = 0

    if isEfatura(fatura_no) and tcKontrolFunc(tc):
        eArsivOrFatura = "e-Fatura"
    else:
        eArsivOrFatura = "e-Arşiv Fatura"

    while belgeTurButton.text != eArsivOrFatura:

        for option in options:
            if option.text == eArsivOrFatura:
                option.click()
                sleep(0.3)
                break

            if sayac > len(options)+1:
                raise ValueError
            sayac += 1


