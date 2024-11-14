from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os


def setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    return driver

my_driver = setup()
my_driver.get("https://demo.nopcommerce.com/")
my_driver.maximize_window()

# my_driver.save_screenshot(os.getcwd()+"home.png")  #to save screenshot in current directory
# my_driver.save_screenshot("C:\\Users\\MAHESH\\Pictures\\Screenshots\\home.png")  #To save screemshot in specified directory
my_driver.get_screenshot_as_file("home1.png")   #if there is no path , then image will be stored in current directory.

# my_driver.get_screenshot_as_png()    #will save image as binary format
# my_driver.get_screenshot_as_base64()  #will save image as binary format s

time.sleep(3)

my_driver.close()