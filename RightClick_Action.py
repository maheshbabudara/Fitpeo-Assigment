from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")

driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
#launching app:
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
#maximize window:
driver.maximize_window()

#find element:
button=driver.find_element(by=By.XPATH, value="//span[@class='context-menu-one btn btn-neutral']")


#Action class:
act=ActionChains(driver)

act.context_click(button).perform()   #context_click() will right click

time.sleep(2)

driver.find_element(by=By.XPATH, value="/html/body/ul/li[4]").click()  #paste option
alert_window=driver.switch_to.alert
alert_window.accept()
time.sleep(2)

# driver.find_element(by=By.XPATH, value='/html/body/ul/li[7]').click()  #Delete option
# time.sleep(3)
