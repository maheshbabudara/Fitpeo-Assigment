from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service)
driver.get("https://www.facebook.com/")

#X-PATHS:

#Absolute X-path:
driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input").send_keys('mahesh')
time.sleep(3)



#Relative X-path:
driver.find_element(by=By.XPATH, value="//*[@id='pass']").send_keys('123')
time.sleep(5)

#AND & #OR:
# driver.find_element(by=By.XPATH, value="//*[@name='login' and @data-testid='royal_login_button']").click()
# driver.find_element(by=By.XPATH, value="//*[@id='u_0_5_Fu' or @name='login']").click()
time.sleep(10)

#contains() & starts-with():
driver.find_element(by=By.XPATH, value="//*[contains(@data-testid,'royal_login')]").click()
# driver.find_element(by=By.XPATH, value="//*[starts-with(@type,'submit')]").click()

#text():
# driver.find_element(by=By.XPATH,value="//button[text()='ಲಾಗ್ ಇನ್']").click()




