from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.implicitly_wait(10)
driver.get("https://www.google.co.in/")
driver.maximize_window()
driver.find_element(by=By.XPATH, value='//*[@id="APjFqb"]').send_keys('mahesh')
time.sleep(5)
driver.find_element(by=By.XPATH, value='//*[@id="Alh6id"]/div[1]/div/ul/li[1]').click()
time.sleep(3)




