import datetime

from selenium.webdriver import Keys

from MyConstants.enum import waitSecond, withIDorXPATH, webDriverWaitEnum, scroolPosition
from Utility.scroolPage import scroolCount
from Utility.waiters import waitCode


def gelir_belgeTarihButton_FUNC(driver,belge_tarihi : str):


    formatted_date = datetime.datetime.strptime(belge_tarihi, "%Y-%m-%d %H:%M:%S").strftime("%d.%m.%Y")
    giveError = False
    while True:
        belgeTarihButton = waitCode(driver, waitSecond.long.value, webDriverWaitEnum.presence_of_element_located,
                                    withIDorXPATH.by_id, "belgeTarihi", "belge Tarih ",giveError)
        if belgeTarihButton is not None:
            break
        else:
            scroolCount(driver, 5, scroolPosition.UP.value)

    while True:
        belgeTarihButton.clear()
        belgeTarihButton.send_keys(formatted_date)
        belgeTarihButton.send_keys(Keys.ENTER)
        if belgeTarihButton.get_attribute("value") == formatted_date:
            break