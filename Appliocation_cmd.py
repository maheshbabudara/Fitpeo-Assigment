# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
# serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
# driver=webdriver.Chrome(service=serv_obj)
# driver.get("https://www.facebook.com/")
#
#
# #Application cmd's:
# print(driver.title)
# print(driver.current_url)
# print(driver.page_source)
#
#
# driver.quit()


#Practise purpose:
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.bigbasket.com/?utm_source=google&utm_medium=cpc&utm_campaign=Brand-T1&gad_source=1&gclid=EAIaIQobChMIldXawuOZhwMVVahmAh2lpwI1EAAYASAAEgJttvD_BwE")
driver.maximize_window()
print(driver.title)
sleep(1)
print(driver.current_url)
sleep(1)
print(driver.page_source)
sleep(2)

driver.close()