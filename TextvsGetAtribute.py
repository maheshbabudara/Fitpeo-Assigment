from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")

driver.maximize_window()

ele=driver.find_element(by=By.XPATH, value="//input[@id='Email']")
ele.clear()
ele.send_keys('mahesh')

time.sleep(3)
print("result of text:",ele.text)  #since there is no inner text, returns nothing
print("result of get_attribute():",ele.get_attribute('value'))  #returns value of atrribute
print("result of get_attribute():",ele.get_attribute('type')) #returns type of attribute value
print("result of get_attribute():",ele.get_attribute('class'))  #returns class of attribute value

# driver.get("https://www.bigbasket.com/?utm_source=google&utm_medium=cpc&utm_campaign=Brand-T1&gad_source=1&gclid=EAIaIQobChMIldXawuOZhwMVVahmAh2lpwI1EAAYASAAEgJttvD_BwE")
# driver.maximize_window()
# driver.implicitly_wait(10)
# Domex=driver.find_element(by=By.XPATH, value="//img[@caption1='Domex']")
# print("Demox Text value:",Domex.text)
#
# time.sleep(5)
# print(Domex.get_attribute("alt"))
# time.sleep(5)
