from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def gelir_waiter_FUNC(driver):
    wait = WebDriverWait(driver, 6)
    while (True):
        element = wait.until(EC.presence_of_element_located((By.XPATH, "//html")))
        if element is not None:
            break