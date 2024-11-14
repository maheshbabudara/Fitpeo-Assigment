# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time as t
# from selenium.webdriver.support.select import Select
#
#
# serv_obj = Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service=serv_obj)
#
# #syntax:
# # https://username:password@url
# #This process is called as "Injection"
#
#
# driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
# driver.maximize_window()
# t.sleep(3)
#
#
# driver.quit()
#
#
# #syntax:
# # https://admin:admin@the-internet.herokuapp.com/basic_auth
#

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

serv_obj = Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
option=webdriver.ChromeOptions()
option.add_argument("--disable-Notifications")
driver=webdriver.Chrome(service=serv_obj, options=option)
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()
sleep(5)

