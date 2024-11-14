from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj= Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
    driver= webdriver.Chrome(service=serv_obj)
    return  driver

my_driver= setup()

my_driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
my_driver.maximize_window()

# https://admin:admin@the-internet.herokuapp.com/basic_auth    #Authentication pops
my_driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/ul/li[3]/button').click()
alt=my_driver.switch_to.alert

print(alt.text)
alt.accept()

my_driver.close()



