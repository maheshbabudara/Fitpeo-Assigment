# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.support.select import Select
#
# serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
# driver=webdriver.Chrome(service=serv_obj)
#
# driver.implicitly_wait(10)
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
#
# drp=Select(driver.find_element(by=By.XPATH, value='//*[@id="country"]'))
# # drp.select_by_visible_text("Brazil")
#
# value=drp.options
# for i in value:
#     if i.text=="Brazil":
#         i.click()
# time.sleep(3)
#
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
option=webdriver.ChromeOptions()
option.add_argument("--disable-Notifications")
driver=webdriver.Chrome(service=serv_obj,options=option)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)
dropdown=driver.find_element(by=By.CSS_SELECTOR, value="select[id='country']")
country=Select(dropdown)

# country.select_by_index(0)
# country.select_by_value("germany")
# country.select_by_visible_text("Australia")
#


#By options:
opt=country.options
for i in opt:
    print(i.text)
    #select sepcific by options :
    if i.text=="China":
        i.click()

#first selected option:
print(country.first_selected_option.text)

#All selected option:
many=country.all_selected_options
for item in many:
    print(item.text)

#is Multiple:
v=country.is_multiple
print(v)

time.sleep(5)




