from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.implicitly_wait(10)
driver.get('https://jqueryui.com/resources/demos/slider/range.html')
driver.maximize_window()

#findind min and Max slider:
min_slider=driver.find_element(by=By.XPATH, value='//*[@id="slider-range"]/span[1]')
max_slider=driver.find_element(by=By.XPATH, value='//*[@id="slider-range"]/span[2]')

#Location of sliders:
print("Location after performing opertions")
print("min_location :",min_slider.location) #{'x': 219, 'y': 47}
print("max_location :",max_slider.location) #{'x': 878, 'y': 47}

 
#Performing actions:
act=ActionChains(driver)
time.sleep(2)
act.drag_and_drop_by_offset(min_slider,100,0).perform()
time.sleep(2)
act.drag_and_drop_by_offset(max_slider,-78,0).perform()

print("Location after performing opertions")
print("min_location :",min_slider.location) #min_location : {'x': 318, 'y': 47}
print("max_location :",max_slider.location) #max_location : {'x': 799, 'y': 47}

time.sleep(3)

# Note: Incase of Vertical Rnage of prices, then change the y axis range and keep xaxis range as same.