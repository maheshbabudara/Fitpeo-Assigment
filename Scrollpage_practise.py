from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from time import sleep
from selenium.webdriver.chrome.service import Service

serv_obj=Service('C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe')
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

element=driver.find_element(by=By.XPATH, value="//a[@class='home-link']")
driver.execute_script("arguments[0].scrollIntoView()",element)
sleep(3)
driver.close()