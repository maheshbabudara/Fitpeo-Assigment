from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep


serv_obj=Service("C:/Python_Selenium/Drivers/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

#browser laucnh:
# driver.get("https://omayo.blogspot.com/")
# driver.maximize_window()
# sleep(10)

#Implicit wait cmd:
# driver.implicitly_wait(10)

# driver.find_element(by=By.XPATH, value="//button[text()='Check this']").click()
# sleep(15)
# driver.find_element(by=By.XPATH, value="//*[@value='Pen' and @id='dte']").click()
# sleep(4)

#qspiders demo apps:
driver.get("https://demoapps.qspiders.com/ui/progress/element?sublist=2")
driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element(by=By.XPATH, value="//input[@placeholder='Enter time in seconds']").send_keys("3")
# sleep(1)
driver.find_element(by=By.XPATH, value="//button[text()='Start']").click()
# sleep(4)
drp_down=driver.find_element(by=By.XPATH, value="//select[contains(@class,'placehold er-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow')]")
down=Select(drp_down)
down.select_by_value("yes")
sleep(5) 

