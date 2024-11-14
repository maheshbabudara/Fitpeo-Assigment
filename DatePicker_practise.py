# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
#
# def setup():
#     from selenium.webdriver.chrome.service import Service
#     serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
#     driver=webdriver.Chrome(service=serv_obj)
#     return driver
#
# my_driver=setup()
# my_driver.implicitly_wait(10)
# my_driver.get("https://testautomationpractice.blogspot.com/")
# my_driver.maximize_window()
#
#
# my_driver.switch_to.frame("frame-one796456169")
# # Date=WebDriverWait(my_driver,10).until(
# #    EC.presence_of_element_located((By.XPATH, "//*[@id='RESULT_TextField-2']"))
# # )
# # Date.send_keys("06/06/1998")
# calender= WebDriverWait(my_driver,10).until((EC.presence_of_element_located((By.XPATH,"//span[@role='button']" ))))
# calender.click()
#
# month= "June"
# date="11"
#
# year_cal = Select(my_driver.find_element(by=By.XPATH, value='//*[@id="ui-datepicker-div"]/div/div/select'))
# year_cal.select_by_visible_text("2025")  # year values selection
#
# while True:
#     month_cal= WebDriverWait(my_driver,10).until(
#         EC.presence_of_element_located((By.XPATH,'//span[@class="ui-datepicker-month"]'))
#     )
#     data=month_cal.text
#     if month==data:
#         break
#     else:
#         btn=my_driver.find_element(by=By.XPATH, value='//*[@id="ui-datepicker-div"]/div/a[2]/span').click()
#
#
# Dates_cal=my_driver.find_elements(by=By.XPATH, value='//*[@id="ui-datepicker-div"]/table/tbody/tr/td/a')
# for d in Dates_cal:
#     if d.text==date:
#         d.click()
#         time.sleep(4)
#         break
# time.sleep(3)
# my_driver.close()
#


#Assignment Task:
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
option=webdriver.ChromeOptions()
option.add_argument("--disable-Notifications")

driver=webdriver.Chrome(service=serv_obj, options=option)
driver.get("https://www.globalsqa.com/demo-site/datepicker/#Simple%20Date%20Picker")
driver.maximize_window()
driver.implicitly_wait(10)
# frame=driver.find_element(by=By.XPATH, value="//iframe[@class='demo-frame lazyloaded']")
# driver.switch_to.frame(frame)
# driver.find_element(by=By.ID, value="datepicker").send_keys("07/22/2024")
sleep(3)
# driver.find_element(by=By.XPATH, value="//input[@class='hasDatepicker']").click()
# mon="July"
# yer="2024"
# dat="21"
#
# while True:
#     month=driver.find_element(by=By.XPATH, value="//span[@class='ui-datepicker-month']").text
#     year=driver.find_element(by=By.XPATH, value="//span[@class='ui-datepicker-year']").text
#     if mon==month and yer==year:
#         break
#     else:
#         driver.find_element(by=By.XPATH, value="//span[text()='Next']").click()  #Next
#         # driver.find_element(by=By.XPATH, value="//span[text()='Prev']").click() #Previous
#
# #Dates:
# Dates=driver.find_elements(by=By.XPATH, value="//table[@class='ui-datepicker-calendar']/tbody//td/a")
# for date in Dates:
#     if date.text==dat:
#         date.click()
#
# sleep(5)
#

#Dropdown date picker:
# driver.find_element(by=By.XPATH, value="//li[text()='DropDown DatePicker']").click()
# sleep(1)
# fram=driver.find_element(by=By.XPATH, value="//li[text()='DropDown DatePicker']/../../div/div/p//iframe[@data-src='../../demoSite/practice/datepicker/dropdown-month-year.html']")
# driver.switch_to.frame(fram)
# sleep(1)
# driver.find_element(by=By.XPATH, value="//head/title[text()='Selenium Practice Datepicker - Display month & year menus']/../../body//*[@id='datepicker']").click()
#
# while True:
#     mon = Select(driver.find_element(by=By.XPATH,
#                                      value="//head/title[text()='Selenium Practice Datepicker - Display month & year menus']/../../body//select[@class='ui-datepicker-month']"))
#     mon.select_by_value("5")
#     sleep(2)
#     yea = Select(driver.find_element(by=By.XPATH,
#                                      value="//head/title[text()='Selenium Practice Datepicker - Display month & year menus']/../../body//select[@class='ui-datepicker-year']"))
#     yea.select_by_visible_text("2024")
#     break
#
# else:
#     Next=driver.find_element(by=By.XPATH, value="//head/title[text()='Selenium Practice Datepicker - Display month & year menus']/../../body//span[text()='Next']").click()
#
#
# #Dates:
# dates=driver.find_elements(by=By.XPATH, value="//head/title[text()='Selenium Practice Datepicker - Display month & year menus']/../../body//table[@class='ui-datepicker-calendar']/tbody/tr//a")
# for date in dates:
#     # print(date.text)
#     if date.text == '23':
#         date.click()
#         print("clicked")
# sleep(5)


#Clender Icon:
driver.find_element(by=By.XPATH, value="//li[text()='Icon Trigger']").click()
sleep(1)
fram=driver.find_element(by=By.XPATH, value="//li[text()='Icon Trigger']/../..//iframe[@data-src='../../demoSite/practice/datepicker/icon-trigger.html']")
driver.switch_to.frame(fram)
sleep(1)
driver.find_element(by=By.XPATH, value="//img[@title='Select date']").click()
mo="August"
ye="2024"
da="9"
while True:
    mon=driver.find_element(by=By.XPATH, value="//span[@class='ui-datepicker-month']").text
    yea=driver.find_element(by=By.XPATH, value="//span[@class='ui-datepicker-year']").text
    if mo==mon and ye==yea:
        break
    else:
        Next=driver.find_element(by=By.XPATH, value="//span[@class='ui-icon ui-icon-circle-triangle-e']").click()
#Dates:
Dates=driver.find_elements(by=By.XPATH, value="//table[@class='ui-datepicker-calendar']//tbody/tr//a")
for date in Dates:
    if date.text==da:
        date.click()
sleep(3)


