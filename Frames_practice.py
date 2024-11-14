from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
    driver=webdriver.Chrome(service=serv_obj)
    return driver

my_driver=setup()

my_driver.get("https://www.selenium.dev/selenium/docs/api/Java")
my_driver.maximize_window()
my_driver.minimize_window()


my_driver.switch_to.frame('packageListFrame')  #switch to frame
my_driver.find_element(by=By.LINK_TEXT, value='org.openqa.selenium').click()
my_driver.switch_to.default_content()  #come out of frame

my_driver.switch_to.frame('packageframe')
my_driver.find_element(by=By.LINK_TEXT, value="webdriver").click()
my_driver.switch_to.default_content()

my_driver.switch_to.frame("classframe")
my_driver.find_element(by=By.LINK_TEXT, value='').click()


my_driver.close()