from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

def setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
    driver=webdriver.Chrome(service=serv_obj)
    return driver

my_driver=setup()

my_driver.get("https://demo.nopcommerce.com/")
my_driver.maximize_window()

#Capture no of cookies and cookies from browser:
cookies_list=my_driver.get_cookies()
print("no of cookies:",len(cookies_list))

#print details of all cookies information:
for i in cookies_list:
    # print(i)  # information of all cookies
    # print(i.get("name")) #Name of all cookies
    print(i.get("domain"))  #specific value
    # print(i.get("name"),"&",i.get("value"))  #by contatination getting 2 attribute values at once.

#Add New Cookie to browser:
my_driver.add_cookie({"name":"mahesh","value":"1234","age":"3"})  #Adding new cookie
cookies_new_list=my_driver.get_cookies()  #After adding new cookies, we have get or capture all cookies again to get all cookies information
print("no of cookies aftering adding new cookie:",len(cookies_new_list))

for j in cookies_new_list:
    print(j.get("name"))


#Delete specifc Cookie from browser:
my_driver.delete_cookie("mahesh")  #To delete  cookie specify "name value"
delete_cookies=my_driver.get_cookies()
print("no of Cookies adfter Deletion:",len(delete_cookies))


#Delete All the Cookies:
my_driver.delete_all_cookies()
deletion_all_cookies= my_driver.get_cookies()
print("No of cookies after deleting all cookies:", len(deletion_all_cookies))

# Note: If Count of cookies is same after adding/deletion, then browser is not allowing to do operation


