from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
ops=webdriver.ChromeOptions()
ops.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj, options=ops)
driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

source=WebDriverWait(driver,10).until(
    e.presence_of_element_located((By.XPATH, "//div[@id='draggable']"))
)
target=WebDriverWait(driver,10).until(
    e.presence_of_element_located((By.XPATH,"//div[@id='droppable']"))
)


action=ActionChains(driver)

action.drag_and_drop(source,target).perform()
sleep(3)

driver.close()



