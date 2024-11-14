from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

def setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
    driver=webdriver.Chrome(service=serv_obj)
    return driver
my_driver=setup()
my_driver.implicitly_wait(10)
my_driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
my_driver.maximize_window()


right=my_driver.find_element(by=By.XPATH, value='/html/body/div/section/div/div/div/p/span')

action=ActionChains(my_driver)

action.context_click(right).perform()
my_driver.find_element(by=By.XPATH, value='/html/body/ul/li[5]').click()
time.sleep(3)
alt=my_driver.switch_to.alert
time.sleep(3)
alt.accept()

time.sleep(3)