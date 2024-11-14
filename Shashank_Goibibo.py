from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver import Keys,ActionChains
from time import sleep
import os
location=os.getcwd()

serv=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
option.add_argument("--disable-Notifications")
# option.add_argument("--headless")
# option.add_argument("-disable-gpu")
preferences={'download.default_directory':location,'plugins.always_open_pdf_externally':True}
option.add_experimental_option('prefs',preferences)

driver=webdriver.Chrome()
driver.get("https://www.goibibo.com/flights/")
driver.implicitly_wait(10)
driver.maximize_window()
sleep(1)
#login:
# login=WebDriverWait(driver,10).until(
#     e.element_to_be_clickable((By.XPATH, "//li[.='LOGIN / SIGNUP'][1]"))
# )
# login.click()
# sleep(1)
# OTP=WebDriverWait(driver,10).until(
#     e.presence_of_element_located((By.XPATH,'//input[@class="loginCont__input"]'))
# )
# OTP.send_keys('8639563301')
# sleep(1)
# con=WebDriverWait(driver,10).until(
#     e.element_to_be_clickable((By.XPATH,"//button[.='Continue']"))
# )
# con.click()
# sleep(10)

driver.find_element(by=By.XPATH,value='//div[@class="sc-12foipm-0 iiZOql"]/div[3]/div//p[@class="sc-12foipm-4 czGBLf fswWidgetTitle"]').click()
sleep(1)

month=driver.find_element(by=By.XPATH,value='//div[@class="DayPicker-Month"][1]//div[@class="DayPicker-Caption"]/div').text

user_month='June 2025'
while True:
    if user_month==month:
        break
    else:
        driver.find_element(by=By.XPATH,value='//div[@class="DayPicker-NavBar"]//span[@aria-label="Next Month"]').click()
dates=driver.find_elements(by=By.XPATH,value='//div[@class="DayPicker-Month"][1]//div[@class="DayPicker-Body"]//div/p')
da='11'
for date in dates:
    if date.text==da:
        date.click()
        break
sleep(5)
driver.close()


