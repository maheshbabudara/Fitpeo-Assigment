from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.implicitly_wait(10)
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()


driver.find_element(by=By.XPATH, value='/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a').click()

outer_frame=driver.find_element(by=By.XPATH, value='//*[@id="Multiple"]/iframe')
driver.switch_to.frame(outer_frame)   #swicthing the frame with webelemnt which is created by finding an XPATH


inner_frame=driver.find_element(by=By.XPATH, value="/html/body/section/div/div/iframe")
driver.switch_to.frame(inner_frame)
driver.find_element(by=By.XPATH, value="/html/body/section/div/div/div/input").send_keys('mahesh Babu')

#In Selenium4, we have an CMD to switch from inner frame to parent frame:
driver.switch_to.parent_frame()
time.sleep(3)

