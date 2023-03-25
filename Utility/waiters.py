import threading
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from MyConstants.enum import prgoramProcess,webDriverWaitEnum,withIDorXPATH
from MyConstants.errorMessage import ProgramProcessHandler, GibProcessHandler
from Threads.errorThreads import show_message_box


def stopTheCode():
    while ProgramProcessHandler.get_process_handler() == prgoramProcess.Stop.value:
        sleep(1)
    return None

def stopTheCodeGib():
    while GibProcessHandler.get_process_handler() == prgoramProcess.Stop.value:
        sleep(1)
    return None


def insideTryCatch(driver,second,webDriverWaitEnum,withIDorXPATH,id_or_xpath="") -> WebElement:
    wait = WebDriverWait(driver, second)
    element = None

    if webDriverWaitEnum == webDriverWaitEnum.presence_of_element_located:
        if withIDorXPATH == withIDorXPATH.by_id:
            element = wait.until(EC.presence_of_element_located((By.ID,id_or_xpath)))
        elif withIDorXPATH == withIDorXPATH.by_xpath:
            element = wait.until(EC.presence_of_element_located((By.XPATH,id_or_xpath)))
        elif withIDorXPATH == withIDorXPATH.by_className:
            element = wait.until(EC.presence_of_element_located((By.CLASS_NAME,id_or_xpath)))
    elif webDriverWaitEnum == webDriverWaitEnum.visibility_of_element_located:
        if withIDorXPATH == withIDorXPATH.by_id:
            element = wait.until(EC.visibility_of_element_located((By.ID,id_or_xpath)))
        elif withIDorXPATH == withIDorXPATH.by_xpath:
            element = wait.until(EC.visibility_of_element_located((By.XPATH,id_or_xpath)))
        elif withIDorXPATH == withIDorXPATH.by_className:
            element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,id_or_xpath)))


    elif webDriverWaitEnum ==  webDriverWaitEnum.element_to_be_clickable:

        if withIDorXPATH == withIDorXPATH.by_id:
            element = wait.until(EC.element_to_be_clickable((By.ID,id_or_xpath)))
        elif withIDorXPATH == withIDorXPATH.by_xpath:
            element = wait.until(EC.element_to_be_clickable((By.XPATH,id_or_xpath)))
        elif withIDorXPATH == withIDorXPATH.by_className:
            element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,id_or_xpath)))

    return element

def controlIsExist(driver,second,webDriverWaitEnum=webDriverWaitEnum.presence_of_element_located,withIDorXPATH=withIDorXPATH.by_id,id_or_xpath="",hataMesaj="Bilinmeyen bir hata!",giveException:bool=True) -> WebElement:
    element = None
    try:
      element =  insideTryCatch(driver,second,webDriverWaitEnum,withIDorXPATH,id_or_xpath)
    except Exception as e:
        if giveException:
            err = threading.Thread(target=show_message_box, name="error", daemon=False, args=(hataMesaj, id_or_xpath))
            err.start()

        print("Timed out waiting for the element:", e)

    return element

def waitCode(driver,second = 10,webDriverWaitEnum = webDriverWaitEnum.presence_of_element_located,withIDorXPATH=withIDorXPATH.by_id,id_or_xpath="",hataMesaj="Bilinmeyen Hata",giveException:bool = True) -> WebElement:
    stopTheCode()
    stopTheCodeGib()



    element = None
    if webDriverWaitEnum == webDriverWaitEnum.presence_of_element_located:
        element = controlIsExist(driver,second,webDriverWaitEnum.presence_of_element_located,withIDorXPATH,id_or_xpath,hataMesaj,giveException)
    elif webDriverWaitEnum == webDriverWaitEnum.visibility_of_element_located:

        element = controlIsExist(driver,second,webDriverWaitEnum.visibility_of_element_located,withIDorXPATH,id_or_xpath,hataMesaj,giveException)
    elif webDriverWaitEnum == webDriverWaitEnum.element_to_be_clickable:
        element = controlIsExist(driver,second,webDriverWaitEnum.element_to_be_clickable,withIDorXPATH,id_or_xpath,hataMesaj,giveException)
    else :
        pass
    return element
