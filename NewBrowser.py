from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:/Python_Selenium/Drivers/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("file:///C:/Users/MAHESH/Downloads/demo.html")
# driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
sleep(2)
driver.find_element(by=By.XPATH, value="//table[@name='selenium']/tbody/tr[2]/td/input").click()
driver.find_element(By.XPATH,"//table[@name='selenium']/tbody/tr[2]/td/input").click()
sleep(2)
driver.find_element(By.LINK_TEXT, "Download").click()
# sleep(5)
driver.find_element(By.PARTIAL_LINK_TEXT, "Inbox").click()
sleep(5)
driver.find_element(by=By.XPATH, value="(//input[@class='first_row'])[1]").send_keys("Mahesh babu")
sleep(3)
driver.close()


