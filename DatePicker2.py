from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.maximize_window()
driver.get("https://www.dummyticket.com/")

driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/section[1]/div/div/div/div/div/div/a').click()

driver.find_element(by=By.XPATH, value='//*[@id="dob"]').click()  #Clicking on Date Picker


#Month Picker:
datepicker_month= Select(driver.find_element(by=By.XPATH, value='//*[@id="ui-datepicker-div"]/div[1]/div/select[1]'))  #Month is dropdown so stored in 'Select' class.
datepicker_month.select_by_visible_text("Jun") #selecting the Month by using Select methods()

#Year picker:
datepicker_year= Select(driver.find_element(by=By.XPATH, value='//*[@id="ui-datepicker-div"]/div[1]/div/select[2]'))
datepicker_year.select_by_visible_text("1998")


#Selecting Date:
Dates=driver.find_elements(by=By.XPATH, value='//*[@id="ui-datepicker-div"]/table/tbody/tr/td/a')

for i in Dates:
    if i.text==11:  #can use i.text==11
        i.click()
        break
time.sleep(3)






