import datetime
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Utility.scroolPage import isBottomOfPage,scroolCount
from MyConstants.enum import waitSecond, withIDorXPATH, webDriverWaitEnum, scroolPosition
from Utility.waiters import waitCode


def gelir_bugunTarihButton_FUNC(driver,belge_tarihi : str):
    giveError = False

    bugun = datetime.date.today()
    tarih_str = bugun.strftime("%d.%m.%Y")
    formatted_date = datetime.datetime.strptime(belge_tarihi, "%Y-%m-%d %H:%M:%S").strftime("%d.%m.%Y")
    while True:
        bugunTarihButton = waitCode(driver, waitSecond.long.value,
                                    webDriverWaitEnum.presence_of_element_located,
                                    withIDorXPATH.by_id, "kayitTarihi", "bugun Tarih ", giveError)
        if bugunTarihButton is not None:
            break
        else:
            scroolCount(driver, 10, scroolPosition.UP.value)

    while bugunTarihButton.get_attribute("value") != formatted_date:
        bugunTarihButton.clear()
        bugunTarihButton.send_keys(formatted_date)
        bugunTarihButton.send_keys(Keys.ENTER)

