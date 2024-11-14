from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from time import sleep
# #
# # def setup():
# #     from selenium.webdriver.chrome.service import Service
# #     serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
# #     driver=webdriver.Chrome(service=serv_obj)
# #     return driver
# #
# # my_driver=setup()
# # my_driver.get("file:///C:/Users/MAHESH/Downloads/demo.html")
# # my_driver.maximize_window()
# #
# # drp=Select(my_driver.find_element(by=By.XPATH, value="//select[@id='multiple_cars']"))
# #
# # drp.select_by_index(3)  #By Index
# # sleep(1)
# # drp.select_by_value("jgr")   #By Value
# # sleep(1)
# # drp.select_by_visible_text("Land Rover")  #By text
# # sleep(5)
# #
# # drp.deselect_by_index(3)
# # sleep(1)
# # drp.deselect_by_value("jgr")
# # sleep(1)
# # drp.deselect_by_visible_text("Land Rover")
# #
# # sleep(2)
# #
#
# from time import sleep
# from selenium import webdriver
# from selenium.common import NoSuchElementException
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as e
# from selenium.webdriver import Keys, ActionChains
# import os
# location=os.getcwd()
#
# driver=webdriver.Chrome()
# option=webdriver.ChromeOptions()
# option.add_experimental_option("detach",True)
# option.add_argument("--disable-Notifications")
# preferences={"download.default_directory":location,"plugins.always_open_pdf_externally":True}
# option.add_experimental_option('prefs',preferences)
# driver.get("https://demoapps.qspiders.com/ui/dropdown?sublist=0")
# driver.maximize_window()
# driver.implicitly_wait(10)
#
#
# phon_code=WebDriverWait(driver, 10, poll_frequency=2,ignored_exceptions=[Exception,NoSuchElementException]).until(
#     e.presence_of_element_located((By.XPATH,"//select[@id='select1']"))
# )
# drp=Select(phon_code)
# drp.select_by_visible_text("+92")
# sleep(1)
# gender=driver.find_element(By.XPATH,"//select[@id='select2']")
# gen_drp=Select(gender)
# gen_drp.select_by_value("others")
# count=driver.find_element(By.XPATH,"//select[@id='select3']")
# count_drp=Select(count)
# count_drp.select_by_visible_text("Germany")
# state=driver.find_element(By.XPATH,"//select[@id='select5']")
# state_drp=Select(state)
# state_drp.select_by_value("Hessen")
# city=driver.find_element(By.XPATH,"//label[text()='City']/../select")
# city_drp=Select(city)
# city_drp.select_by_visible_text("Select City")
# items=driver.find_element(By.XPATH,"//select[@id='select7']")
# items_drp=Select(items)
# items_drp.select_by_visible_text("3")
# sleep(1)
# driver.find_element(By.XPATH,"//button[.='Continue']").click()
# sleep(3)
# driver.find_element(By.XPATH,"//a[.='Multi Select']").click()
# sleep(1)
# country=Select(driver.find_element(By.ID,"select-multiple-native"))
# country.select_by_visible_text("Poland")
# sleep(1)
# state=Select(driver.find_element(By.XPATH,"//label[text()='State']/../div/select"))
# state.select_by_visible_text("Masovia")
# sleep(1)
# driver.find_element(By.XPATH,"//a[text()='Search With Select']").click()
# sleep(1)
# driver.find_element(By.XPATH,"//div[@class=' css-13cymwt-control']/div/div[@class=' css-1dimb5e-singleValue']").click()
# sleep(5)
# driver.close()
#

driver=webdriver.Chrome()
driver.get("https://demoapps.qspiders.com/ui/dropdown")
driver.implicitly_wait(10)
driver.maximize_window()

# mob=Select(driver.find_element(By.XPATH,"//select[@id='select1']"))
# m=mob.options
# for i in m:
#     if i.text=="+44":
#         i.click()
#         break
# sleep(5)

driver.close()
