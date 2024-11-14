from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.implicitly_wait(10)
driver.get('https://www.worldometers.info/geography/flags-of-the-world/')
driver.maximize_window()

#1.Scroll page by pixels:
# driver.execute_script("window.scrollBy(0,3000)","")
# value=driver.execute_script("return window.pageYOffset;")
# print('Number of pixels moved:',value)  #3000
# time.sleep(3)

#2.Scroll page by element visibility:
# India_flag=driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[2]/div[1]/div/div/div/div[79]/div/a/img')
# driver.execute_script("arguments[0].scrollIntoView();",India_flag)   #arguments are change
# value=driver.execute_script("return window.pageYOffset;")   #To know how many pixexl it scrolled
# print('Number of pixels moved:',value)
# time.sleep(3)

#3.Scroll page completly Down:
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","")
value=driver.execute_script("return window.pageYOffset;")   #To know how many pixexl it scrolleddown
print('Number of pixels moved:',value)
time.sleep(3)

#4.Scrolling up to starting position:
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)","")
value=driver.execute_script("return window.pageYOffset;")   #To know how many pixexl it scrolledup
print('Number of pixels moved:',value)
time.sleep(3)
