from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

serv_obj= Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")

driver=webdriver.Chrome(service=serv_obj)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#finding origginla locations:

min_slider= WebDriverWait(driver,10, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,ElementNotSelectableException]).until(
    e.presence_of_element_located((By.XPATH, '//*[@id="slider"]/span'))
)

print("min_slider location:",min_slider.location)

action=ActionChains(driver)

action.drag_and_drop_by_offset(min_slider,100,0).perform()
sleep(3)
print("After changin slider location:",min_slider.location)

driver.close()
