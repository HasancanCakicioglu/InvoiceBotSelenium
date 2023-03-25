from MyConstants.enum import waitSecond, webDriverWaitEnum, withIDorXPATH
from Utility.waiters import waitCode


def login_sifre_lineEdit_FUNC(driver,myDB,data):
    sifre_lineEdit = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.presence_of_element_located,
                              withIDorXPATH.by_id, "password", "GibHelper şifre ")

    sifre_lineEdit.send_keys(myDB.get(data.gib_sifre))