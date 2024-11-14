import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
location=os.getcwd()

serv_obj = Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# driver.save_screenshot("C:\\Users\\MAHESH\\Pictures\\Screenshots\\practise.png")
driver.get_screenshot_as_file("C:\\Users\\MAHESH\\Pictures\\Screenshots\\checking.png")
# driver.get_screenshot_as_png("C:\\Users\\MAHESH\\Pictures\\Screenshots\\checking.png")
# driver.get_screenshot_as_base64("C:\\Users\\MAHESH\\Pictures\\Screenshots\\checking.png")
sleep(3)
driver.close()




