from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.instagram.com/")
driver.get("https://www.facebook.com/")
driver.maximize_window()

driver.back()  #goes backwards direction
time.sleep(5)
driver.forward()
time.sleep(3)
driver.refresh()

driver.quit()


