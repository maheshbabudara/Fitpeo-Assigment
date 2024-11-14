from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
    driver=webdriver.Chrome(service=serv_obj)
    return driver

my_driver=setup()

my_driver.implicitly_wait(10)

my_driver.get("https://practice.expandtesting.com/upload")
my_driver.maximize_window()
# my_driver.find_element(by=By.ID, value="fileSubmit").click()
#
# time.sleep(1)

my_driver.find_element(by=By.XPATH, value='//*[@id="fileInput"]').send_keys("D:\mahi\Credentials TCS.txt")
time.sleep(3)


my_driver.close()