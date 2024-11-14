from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver import Keys, ActionChains
from time import sleep
import os
location=os.getcwd()

serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64/chromedriver.exe")
preferences={'download.default_directory':location,"plugins.always_open_pdf_externally":True}
option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
option.add_argument("--disable Notifications")
option.add_argument('--headless')
option.add_argument('--disable-gpu')
option.add_experimental_option('prefs',preferences)
driver=webdriver.Chrome(service=serv_obj,options=option)

driver.get("https://demoapps.qspiders.com/ui?scenario=1")
driver.implicitly_wait(10)
driver.maximize_window()

driver.find_element(by=By.XPATH,value='//input[@placeholder="Enter your name"]').send_keys("Mahesh Babu")
sleep(1)
driver.find_element(by=By.XPATH,value='//input[@placeholder="Enter Your Email"]').send_keys('mahesh@gmail.com')
sleep(1)
driver.find_element(by=By.XPATH,value='//input[@placeholder="Enter your password"]').send_keys('test@123')
sleep(1)
driver.find_element(by=By.XPATH,value="//button[contains(text(),'Register')]").click()
sleep(1)
driver.find_element(by=By.XPATH,value="//li[text()='Multiline Text Area']").click()
sleep(1)
driver.find_element(by=By.ID,value='name').send_keys('Rony')
sleep(1)
driver.find_element(by=By.ID,value='email').send_keys('Mahesh123@gmail.com')
sleep(1)
driver.find_element(by=By.ID,value='password').send_keys('test@123')
sleep(1)
driver.find_element(by=By.XPATH,value="//button[text()='Register']").click()
sleep(5)
