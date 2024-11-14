from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time as t
from selenium.webdriver.support.select import Select


serv_obj = Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")