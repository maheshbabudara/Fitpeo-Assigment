# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as e
# from time import sleep
# from selenium.webdriver import Keys, ActionChains
# import os
# location=os.getcwd()
#
#
# serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
# preferences={"download.default_directory":location,"plugins.always_open_pdf_externally":True}
# option=webdriver.ChromeOptions()
# option.add_experimental_option("detach", True)
# option.add_argument("--disable-Notifications")
# # option.add_argument("--headless")
# # option.add_argument("--disable-gpu")
# option.add_experimental_option('prefs',preferences)
#
# driver=webdriver.Chrome(service=serv_obj, options=option)
# driver.get("file:///C:/Users/MAHESH/Downloads/demo.html")
# driver.implicitly_wait(15)
# driver.maximize_window()
# sleep(1)
# links=driver.find_elements(by=By.XPATH, value="//a")
# for link in links:
#     print("linkName:",link.text)
#     link.click()
#     sleep(1)
# Multiple_windows=driver.window_handles
#
# for win in Multiple_windows:
#     driver.switch_to.window(win)
#     print("window Id:",win,"Title:",driver.title)
#     sleep(1)
#     if driver.current_url=="https://the-internet.herokuapp.com/basic_auth":
#         driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
#         sleep(1)
#         driver.close()
# driver.quit()
#

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver import Keys, ActionChains
import os
location=os.getcwd()

serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
option=webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
preferences={"download.default_directory":location, "plugins.always_open_pdf_externally":True}
option.add_argument("--disable-Notifications")
# option.add_argument("--headless")
# option.add_argument("--disable-gpu")
option.add_experimental_option("prefs", preferences)

driver=webdriver.Chrome(service=serv_obj, options=option)
driver.get("file:///C:/Users/MAHESH/Downloads/demo.html")
driver.implicitly_wait(10)
driver.maximize_window()

links=driver.find_elements(by=By.XPATH, value="//a")
for link in links:
    print("link:",link.text,link.click())
tabs=driver.window_handles

for tab in tabs:
    driver.switch_to.window(tab)
    print("id:",tab,"title:",driver.title)
    if driver.current_url =="https://the-internet.herokuapp.com/basic_auth":
        driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
        sleep(2)
        driver.close()
driver.quit()

