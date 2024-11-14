from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e

service = Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)
time.sleep(3)
driver.get("https://www.facebook.com/")

# time.sleep()
action_title = driver.title
fb_title = "Facebook – log in or sign up"

"""Browsing Validation:"""
# if  (action_title==fb_title) :
#     print('Test Case Passed');
# else:
#     print("Test case is Failed")

time.sleep(3)
driver.find_element(by=By.ID, value="email").clear()
driver.find_element(by=By.ID, value="email").send_keys('maheshdara13@gmail.com')
time.sleep(3)
driver.find_element(by=By.ID, value="pass").clear()
driver.find_element(by=By.ID, value="pass").send_keys('Ronyrani@1201')
time.sleep(3)

driver.find_element(by=By.NAME, value="login").click()

'''Can be used below way as well'''
# login_btn = WebDriverWait(driver, 3).until(
#     e.element_to_be_clickable((By.NAME, "login"))
# )
# login_btn.click();

#Not working as expected Need to check with SHASHANK:
# login_btn= WebDriverWait(driver,3).until(
#     e.element_to_be_clickable((By.ID,"loginbutton"))
# )
# login_btn.click()


time.sleep(10);
driver.quit();
