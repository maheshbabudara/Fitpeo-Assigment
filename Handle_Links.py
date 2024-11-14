# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time as t
#
# serv_obj = Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service=serv_obj)
#
# driver.implicitly_wait(10)
# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()
#
# """Below code is used for both Internal and External Links:"""
#
# #Click on Link:
# driver.find_element(by=By.LINK_TEXT,value="Digital downloads").click()
# t.sleep(3)
#
# #Find Total Number of links on web page:
# Links= driver.find_elements(by=By.TAG_NAME, value="a")
# # Links= driver.find_elements(by=By.XPATH, value='//a')
# print("Total No of links:",len(Links))
# for link in Links:
#     print(link.text)
#     print(link.get_attribute('href'))


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from time import sleep


serv=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
option=webdriver.ChromeOptions()
option.add_argument("--disable-Notifications")
driver=webdriver.Chrome(service=serv, options=option)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

#link:
# driver.find_element(by=By.XPATH, value="//a[text()='open cart          ']").click()
# driver.back()
# sleep(1)
#External link:
# driver.find_element(by=By.XPATH, value="//a[text()='Posts (Atom)']").click()
# print("window id's:",driver.window_handles)
# windowids=driver.window_handles
# child=windowids[0]
# parent=windowids[1]
# sleep(3)
# driver.switch_to.window(parent)
# driver.close()
# for i in windowids:
#     page=driver.switch_to.window(i)
#     if page.title=="fb":
#         driver.close()

sleep(5)

#links:
links=driver.find_elements(by=By.XPATH, value="//a")

for link in links:
    print(link.get_attribute("href"))
sleep(3)




