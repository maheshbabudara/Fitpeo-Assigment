import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.support.select import Select
from time import sleep

location=os.getcwd()
serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
preferences={"dowload.default_directory":location, "plugins.always_open_externally_pdf":True}
option=webdriver.ChromeOptions()
option.add_argument("--disable-Notifications")
option.add_experimental_option("detach", True)
option.add_experimental_option("prefs", preferences)

driver= webdriver.Chrome(service=serv_obj, options=option)
driver.get("https://wynk.in/music/song/demons/hu_1607476")
driver.maximize_window()
driver.implicitly_wait(15)

driver.find_element(by=By.XPATH, value="//a[@title='Radioactive']").click()
sleep(5)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.switch_to.new_window("window")
driver.get("https://testautomationpractice.blogspot.com/")
sleep(5)
driver.close()