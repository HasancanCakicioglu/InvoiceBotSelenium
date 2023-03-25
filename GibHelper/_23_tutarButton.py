from time import sleep

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from MyConstants.enum import scroolPosition, waitSecond, webDriverWaitEnum, withIDorXPATH
from Utility.scroolPage import scroolCount
from Utility.waiters import waitCode


def gelir_tutarButton_FUNC(driver,price:str):
    wait = WebDriverWait(driver, 3)

    left_price = price.split(".")[0]
    right_price = price.split(".")[1]
    giveError = False
    while True:
        tutarButton = waitCode(driver, waitSecond.low.value, webDriverWaitEnum.element_to_be_clickable,
                                       withIDorXPATH.by_xpath, "/html/body/div/main/div[2]/div/div[1]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div[2]/form/div[1]/div[2]/div[3]/div/div/input", "tutar button", giveError)
        #tutarButton = wait.until(EC.element_to_be_clickable((By.XPATH,
        #                                                  "/html/body/div/main/div[2]/div/div[1]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div[2]/form/div[1]/div[2]/div[3]/div/div/input")))
        if tutarButton is not None:
            break
        else:
            scroolCount(driver, 5, scroolPosition.DOWN.value)

    while tutarButton.get_attribute("value") != left_price+","+right_price:
        ActionChains(driver).move_to_element(tutarButton).click().key_down(Keys.CONTROL).send_keys("a").key_up(
            Keys.CONTROL).send_keys(left_price).send_keys(Keys.ARROW_RIGHT).send_keys(Keys.ARROW_RIGHT).send_keys(
            right_price).perform()



