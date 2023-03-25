
from MyConstants.enum import waitSecond, webDriverWaitEnum, withIDorXPATH
from Utility.waiters import waitCode


def login_girisButton_FUNC(driver):
    giris_button = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.presence_of_element_located,
                            withIDorXPATH.by_id, "loginButton1", "GibHelper giriş button ")
    giris_button.click()