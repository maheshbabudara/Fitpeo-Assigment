# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.select import Select
# from selenium.webdriver import Keys, ActionChains
# from time import sleep
#
# serv_obj=Service("C:/Python_Selenium/Drivers/chromedriver-win64/chromedriver.exe")
# driver=webdriver.Chrome(service=serv_obj)
# driver.get("https://demowebshop.tricentis.com/")
# driver.implicitly_wait(10)
# driver.maximize_window()
#
# driver.find_element(by=By.XPATH, value="//input[@class='search-box-text ui-autocomplete-input']").send_keys("shoes")
# sleep(1)
# driver.find_element(by=By.XPATH,value="//a[text()='Register']").click()
# sleep(1)
# driver.find_element(by=By.XPATH, value="//img[@alt='Tricentis Demo Web Shop']").click()
# # driver.close()
# sleep(5)
# driver.close()

#Parctise:
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from time import sleep
from selenium.webdriver import Keys, ActionChains
import os
location= os.getcwd()

serv_obj=Service("C:/Python_Selenium/Drivers/chromedriver-win64/chromedriver.exe")
preferences={"download.default_directory":location,"plugins.always_open_pdf_externally":True}
option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
option.add_argument("--disable-Notifications")
# option.add_argument("--headless")
# option.add_argument("--disable-gpu")
option.add_experimental_option("prefs",preferences)
driver=webdriver.Chrome(service=serv_obj,options=option)

driver.get("https://demowebshop.tricentis.com/")
driver.implicitly_wait(10)
driver.maximize_window()

driver.find_element(by=By.XPATH, value="//input[@value='Search store']").send_keys("dress")
sleep(1)
driver.find_element(by=By.XPATH,value="//a[text()='Register']").click()
sleep(2)
driver.back()
sleep(5)
driver.close()

