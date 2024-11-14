from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

option=webdriver.ChromeOptions()  #ChomeOption for getting settings of browser and we can varios setting in ChromeOptions
option.add_argument("--disable-Notifications")  #Adding an parameter to ChromOptions

serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")  #creating service object

driver=webdriver.Chrome(service=serv_obj,options=option)

driver.get("https://whatmylocation.com/where-ami-now.htm")
driver.maximize_window()
time.sleep(3)

driver.close()

