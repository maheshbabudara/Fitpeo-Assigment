import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotSelectableException, ElementNotVisibleException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
    driver=webdriver.Chrome(service=serv_obj)
    return driver
my_driver=chrome_setup()
my_driver.get("https://testautomationpractice.blogspot.com/")
my_driver.maximize_window()


dbl=WebDriverWait(my_driver,10,ignored_exceptions=[NoSuchElementException,ElementNotSelectableException,ElementNotVisibleException]).until(
    e.presence_of_element_located((By.XPATH, '//button[text()="Copy Text"]'))
)

action= ActionChains(my_driver)

action.double_click(dbl).perform()
time.sleep(3)

my_driver.close()


