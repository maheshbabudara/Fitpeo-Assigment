# string = "mahesh bruthday is today"
# for i in range(len(string) - 1):
#     print(i)
#
# print(string[3:23:3])

from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
import time

# service = Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service=service )

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
time.sleep(3)
driver.find_element(by=By.ID, value="email").clear()
driver.find_element(by=By.ID, value="email").send_keys("mahesh")
time.sleep(3)
driver.find_element(by=By.ID, value="pass").clear()
driver.find_element(by=By.ID, value="pass").send_keys("test@123")
time.sleep(3)

login_btn = WebDriverWait(driver, 5).until(
    e.element_to_be_clickable((By.NAME, "login"))
)
login_btn.click()

time.sleep(10)f

driver.quit()  #quit command will close all the browsers at once
# driver.close()  #close command will close only current browser
