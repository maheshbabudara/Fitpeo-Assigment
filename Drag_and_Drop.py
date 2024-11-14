from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.implicitly_wait(10)
driver.get('https://ui.vision/demo/webtest/dragdrop/')
driver.maximize_window()

#Source element:
source=driver.find_element(by=By.XPATH, value='//*[@id="one"]')

#Target:
target=driver.find_element(by=By.XPATH, value='//*[@id="bin"]')



#Classs:
act=ActionChains(driver)

#Drag and Drop:
act.drag_and_drop(source,target).perform()
time.sleep(2)

#source2:
source2=driver.find_element(by=By.XPATH, value='//*[@id="two"]')

act.drag_and_drop(source2,target).perform()
time.sleep(2)