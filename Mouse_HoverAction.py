from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.implicitly_wait(10)
driver.get("https://www.browserstack.com/guide/mouse-hover-in-selenium")
driver.maximize_window()

products=driver.find_element(by=By.XPATH, value='//*[@id="products-dd-toggle"]')  #products


autonation=driver.find_element(by=By.XPATH, value='//*[@id="products-dd-tabpanel-1-inner-1"]/div[2]/div[2]/a/div')  #automation


#MouserHover:_
action=ActionChains(driver)

action.move_to_element(products).move_to_element(autonation).click().perform()
#we have to use perform() or else Action will not be performed
time.sleep(3)