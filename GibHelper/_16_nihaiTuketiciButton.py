from time import sleep

from MyConstants.enum import waitSecond, withIDorXPATH, webDriverWaitEnum, scroolPosition
from Utility.scroolPage import scroolCount
from Utility.waiters import waitCode


def gelir_nihaiTuketiciCheckbox_FUNC(driver,number:int):

    giveError = False
    while True:
        nihaiTuketiciCheckbox = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.presence_of_element_located,
                                  withIDorXPATH.by_id, "nihaiTuketici", "nihaiTuketici", giveError)
        if nihaiTuketiciCheckbox is not None:
            break
        else:
            scroolCount(driver, 5, scroolPosition.DOWN.value)
    if number == 1:
        textim = "true"
    else:
        textim = "false"

    while nihaiTuketiciCheckbox.get_attribute("value") != textim:
        if nihaiTuketiciCheckbox.get_attribute("value") != textim:
            nihaiTuketiciCheckbox.click()
            sleep(0.1)
# False -> Vergi Mükellefi
# True -> Nihai Tüketici