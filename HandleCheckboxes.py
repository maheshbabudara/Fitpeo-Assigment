from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time as t

serv_obj = Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#To Scroll down the webpage:
driver.execute_script("window.scrollBy(0,500)", "")

#1.Select specific CheckBox :
# driver.find_element(by=By.XPATH, value="//input[@id='monday']").click()
# t.sleep(5)



# 2.Selecting Multiple Checkboxes :
# Checkboxes = driver.find_elements(by=By.XPATH, value="//input[@type='checkbox' and contains(@value,'day')]") #find_elements returns List output
#
# # simple Approach:
# for i in Checkboxes:
#     i.click()

#Using range():
# for i in range(len(Checkboxes)):
#     Checkboxes[i].click()
# t.sleep(5)



#3.Select Multiple checkboxes by choice :
Checkboxes=driver.find_elements(by=By.XPATH, value="//input[@type='checkbox' and contains(@value,'day')]")

for i in Checkboxes:
    weekname= i.get_attribute('value')
    if weekname == 'sunday' or weekname == 'friday' or weekname=='saturday':
        i.click()
    t.sleep(3)


#4.Select Last 2 Checkboxes:
# Checkboxes=driver.find_elements(by=By.XPATH, value="//input[@type='checkbox' and contains(@value,'day')]")

# for i in range(len(Checkboxes)-2,len(Checkboxes)):   #range(5,7) => (total no of elements(7)-2(last 2 elements want to check), total no.of elements(7)) and range starts from 0, ---
#     Checkboxes[i].click()
#     t.sleep(3)

#5.Select First 2 checkboxes:
# Checkboxes=driver.find_elements(by=By.XPATH, value="//input[@type='checkbox' and contains(@value,'day')]")
# for i in range(len(Checkboxes)):
#     if i<2:   #since range start from '0'(0,1), we took 2 as an end point
#         Checkboxes[i].click()
#         t.sleep(3)

#6.Clearing all Check boxes:
# t.sleep(3)
# Checkboxes=driver.find_elements(by=By.XPATH, value="//input[@type='checkbox' and contains(@value,'day')]")
# for checkbox in Checkboxes:
#     if checkbox.is_selected():
#         checkbox.click();