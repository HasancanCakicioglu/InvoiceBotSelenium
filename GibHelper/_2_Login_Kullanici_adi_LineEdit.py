from time import sleep

from MyConstants.enum import waitSecond, webDriverWaitEnum, withIDorXPATH
from Utility.waiters import waitCode



def login_kullanici_adi_LineEdit_Func(driver,myDB,data):
    kullanici_adi_lineEdit = waitCode(driver, waitSecond.long.value, webDriverWaitEnum.presence_of_element_located,
                                      withIDorXPATH.by_id, "username", "GibHelper kullanıcı adı ")
    kullanici_adi_lineEdit.send_keys(myDB.get(data.gib_kullanici_adi))