import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.youtube.com/")
driver.implicitly_wait(10)
driver.maximize_window()

# driver.save_screenshot("youtube.png")
driver.get_screenshot_as_png()
time.sleep(5)




