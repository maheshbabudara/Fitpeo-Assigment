from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")


driver=webdriver.Chrome(service=serv_obj)

driver.implicitly_wait(10)
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick")
driver.maximize_window()

#switching:

driver.switch_to.frame("iframeResult")

db_button=driver.find_element(by=By.XPATH, value="/html/body/button")

act=ActionChains(driver)   #object

act.double_click(db_button).perform()   #Double click action
time.sleep(3)