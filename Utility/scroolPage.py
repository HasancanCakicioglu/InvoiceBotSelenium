from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from MyConstants.enum import scroolPosition

def scroolCount(driver,x:int,scrool=scroolPosition.DOWN.value):
    for i in range(x):
        if scrool == scroolPosition.DOWN.value:
            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ARROW_DOWN)
        else:
            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ARROW_UP)



def isBottomOfPage(driver) -> bool:
    scroll_position = driver.execute_script("return window.pageYOffset;")
    window_height = driver.execute_script("return window.innerHeight;")
    document_height = driver.execute_script("return document.body.scrollHeight;")
    if (scroll_position + window_height) == document_height:
        return True

    return False