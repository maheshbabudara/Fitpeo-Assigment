# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from time import sleep
#
# serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
# driver=webdriver.Chrome(service=serv_obj)
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
#
# cookies_list=driver.get_cookies()
# print("no of cookies:",len(cookies_list))
#
# sleep(3)
#
# driver.add_cookie({'name':'mahesh','age':"22", 'value':'44'})
# new_cookies=driver.get_cookies()
# print(len(new_cookies))
#
# for c in new_cookies:
#     # print(c.get("value")
#     print(c.get("name"))
#
# driver.add_cookie({'name':'rony','value':'33'})
# new=driver.get_cookies()
# print(len(new))
# for i in new:
#     print(i.get("name"))
#
# driver.delete_all_cookies()
# list=driver.get_cookies()
# print(len(list))
#
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys,ActionChains
from time import sleep

obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
option=webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
option.add_argument("--disable-Notifications")
driver=webdriver.Chrome(service=obj, options=option)
driver.get("https://wynk.in/music/song/party-in-the-usa/hu_1940170?q=party+in+us")
driver.maximize_window()
driver.implicitly_wait(10)

#List of cookies:
cookies=driver.get_cookies()
print('All_Cookies:',len(cookies))
print("Cookies_details",cookies)
for item in cookies:
    print(item.get("name"))

#Add New cookies:
driver.add_cookie({"name":"mahesh", "value":"33"})
latest_cookies=driver.get_cookies()
print(len(latest_cookies))
print("After adding cookies:",latest_cookies)
for item in latest_cookies:
    print(item.get("name"))

#delete cookies:
driver.delete_cookie('mahesh')
delete_cookie=driver.get_cookies()
print("After deleting specific cookies count:", len(delete_cookie))
print('After deleting cookies:',delete_cookie)

#Deleting all cookies:
driver.delete_all_cookies()
all=driver.get_cookies()
print("After deleting all cookies:", len(all))


driver.close()