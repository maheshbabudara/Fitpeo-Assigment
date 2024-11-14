# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
#
#
# def setup():
#     from selenium.webdriver.chrome.service import Service
#     serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
#     driver=webdriver.Chrome(service=serv_obj)
#     return driver
#
# my_driver=setup()
#
# my_driver.implicitly_wait(10)
# my_driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
# my_driver.maximize_window()
#
# my_driver.find_element(by=By.XPATH, value='//*[@id="billing_country_field"]/span').click()  #field
#
# Countries_list=my_driver.find_elements(by=By.XPATH, value='//*[@id="billing_country"]/option')  #dropdown list
#
# print(len(Countries_list))
#
# for country in Countries_list:
#     if country.text=="Canada":
#         country.click()
#         break;
# # scroll=my_driver.find_element(by=By.XPATH, value='//*[@id="select2-billing_country-container"]')
# # my_driver.execute_script("arguments[0].scrollIntoView;",scroll)
# my_driver.execute_script("window.scrollBy(0,300)","")
# time.sleep(5)
# my_driver.close()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver import ActionChains,Keys
from time import sleep
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
option=webdriver.ChromeOptions()
option.add_argument("--disable-Notifications")
option.add_experimental_option("detach", True)
driver=webdriver.Chrome(service=serv_obj,options=option)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.implicitly_wait(10)

head=WebDriverWait(driver,10).until(
    e.presence_of_element_located((By.ID, "product_7441"))
)
head.click()
sleep(1)
select=Select(driver.find_element(by=By.ID, value="reasondummy"))
select.select_by_value("3")
sleep(2)
country=Select(driver.find_element(by=By.NAME, value="billing_country"))
country.select_by_visible_text("Angola")
sleep(2)

s=WebDriverWait(driver,10).until(
    e.presence_of_element_located((By.XPATH, "//select[@id='billing_state']"))
)
state=Select(s)
sleep(1)
state.select_by_visible_text("Benguela")
sleep(2)
driver.save_screenshot("Visa_screenshot.png")
sleep(3)
driver.close()