from time import sleep

from MyConstants.constantShelve import GoogleTextController
from MyConstants.enum import waitSecond, webDriverWaitEnum, withIDorXPATH
from Utility.waiters import waitCode


def login_resimkod_FUNC(driver):
    resimKod = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.presence_of_element_located,
                        withIDorXPATH.by_id, "captcha1", "GibHelper Resim Kod ")
    while (True):
        sleep(1)
        if GoogleTextController.get_google_login_text() != "":
            resimKod.send_keys(GoogleTextController.get_google_login_text())
            break

    GoogleTextController.set_google_login_text("")