from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e

service = Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)
time.sleep(3)
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()


#1. By send_keys() updated the date:
# driver.switch_to.frame(0)  #swicthing frame by index, becoz we have only 1 frame.
# driver.find_element(by=By.ID, value="datepicker").send_keys("06/11/2024")  #works with send_keys()
# time.sleep(3)

#2.Aprroach with Logic:
driver.switch_to.frame(0)
driver.find_element(by=By.ID, value="datepicker").click()   #opens Date Pickers

month="June"
year="2023"
Date="11"

#Picking Year and Month:
while True:
    mon=driver.find_element(by=By.XPATH, value='//*[@id="ui-datepicker-div"]/div/div/span[1]').text
    yr=driver.find_element(by=By.XPATH, value='//*[@id="ui-datepicker-div"]/div/div/span[2]').text

    if mon==month and yr==year:
        break;
    else:
        # driver.find_element(by=By.XPATH, value='//*[@id="ui-datepicker-div"]/div/a[2]/span').click()   #Next Arrow for Future month and year
        driver.find_element(by=By.XPATH, value='//*[@id="ui-datepicker-div"]/div/a[1]/span').click()  #Previous Arrow for previous monthe and Year

#Limitation: In Real time web Applications, we can see either Future or previous dates Arrow, but not both in calender ex Travle dates, date of birth etc.

#Picking the Date as per month and year:
dates=driver.find_elements(by=By.XPATH, value="//*[@class='ui-datepicker-calendar']/tbody/tr/td/a") #element of all dates
for ele in dates:
    if ele==Date:
        ele.click()
        break;

