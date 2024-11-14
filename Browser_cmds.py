from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.maximize_window()
time.sleep(8)
url=driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a').click()
# url= driver.find_element(by=By.LINK_TEXT, value='OrangeHRM, Inc')
# url.click()
time.sleep(15)

# driver.close()
driver.quit()