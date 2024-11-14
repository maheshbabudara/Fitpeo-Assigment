import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys, ActionChains
serv_obj=Service("C:/Python_Selenium/Drivers/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://demoapps.qspiders.com/ui/datePick?sublist=0")
driver.implicitly_wait(10)
driver.maximize_window()

Icon=WebDriverWait(driver,10).until(
    e.presence_of_element_located((By.XPATH,"//label[text()='Default Date picker ( Normal )']/..//*[@fill='currentColor' and @xmlns='http://www.w3.org/2000/svg']"))
)
Icon.click()

Month_Year="August 2026"
Date="10"
while True:
    data=driver.find_element(by=By.XPATH,value="//div[@class='react-datepicker__current-month']").text
    if data==Month_Year:
        break
    else:
        next_btn=driver.find_element(by=By.XPATH,value="//button[@aria-label='Next Month']").click()

dates=driver.find_elements(by=By.XPATH,value="//div[@class='react-datepicker__month']//div")
time.sleep(2)
for d in range(1,len(dates)+1):
    if dates[d].text==Date:
        dates[d].click()
        break
time.sleep(3)


# #Dropdown:
# driver.find_element(by=By.XPATH,value="//a[text()='Dropdown DatePicker']").click()
# time.sleep(1)
# driver.find_element(by=By.XPATH,value='//*[@fill="currentColor"]/../../label[.="Drop Down Date picker"]//../div/*[@stroke="currentColor"]').click()
# time.sleep(1)
# # driver.find_element(by=By.XPATH, value='//span[@class="react-datepicker__year-read-view--down-arrow"]').click()
# # time.sleep(1)
# months=driver.find_elements(by=By.XPATH,value='//div[@class="react-datepicker__month-dropdown"]/div')
# for m in months:
#     if m.text=="September":
#         m.click()
#     break
# time.sleep(2)
# y=WebDriverWait(driver,15,poll_frequency=2).until(
#     e.element_to_be_clickable((By.XPATH,'//div[@class="react-datepicker__year-read-view"]//span[@class="react-datepicker__year-read-view--down-arrow"]'))
# )
# y.click()
# time.sleep(1)
# years=driver.find_elements(by=By.XPATH,value='//div[@class="react-datepicker__year-dropdown"]/div')
# for year in years:
#     if year.text=="2026":
#         year.click()
#     break
# time.sleep(1)
# Dates=driver.find_elements(by=By.XPATH,value='//div[@class="react-datepicker__week"]/div')
# for date in Dates:
#     if date.text=="10":
#         date.click()
#     break
# time.sleep(3)
#
# #Icon Trigger:
# driver.find_element(by=By.XPATH,value="//a[.='Icon Trigger']").click()
# time.sleep(2)
# icon=WebDriverWait(driver,10).until(
#     e.element_to_be_clickable((By.XPATH,'//div[@class="react-datepicker-wrapper"]/..//*[@fill="currentColor"]'))
# )
# icon.click()
# time.sleep(1)
# mon_year='September 2027'
# time.sleep(1)
# while True:
#     m_y=driver.find_element(by=By.XPATH, value='//div[@class="react-datepicker__current-month"]').text
#     if m_y==mon_year:
#         break
#     else:
#         driver.find_element(by=By.XPATH,value='//button[@class="react-datepicker__navigation react-datepicker__navigation--next"]').click()
# dates=driver.find_elements(by=By.XPATH, value='//div[@class="react-datepicker__month"]//div')
# for date in dates:
#     if date.text=="11":
#         date.click()
#     break
# time.sleep(5)


#Time Picker:
# driver.find_element(by=By.XPATH,value="//section[text()='Date & Time Picker']").click()
# time.sleep(1)
#
# driver.find_element(by=By.XPATH, value="//a[@href='/ui/timePick']/section[text()='Time Picker']").click()
# time.sleep(1)
# driver.find_element(by=By.XPATH,value='//button[@class="MuiButtonBase-root MuiIconButton-root MuiIconButton-edgeEnd MuiIconButton-sizeMedium css-slyssw"]').click()
# time.sleep(1)
# Hours=driver.find_elements(by=By.XPATH,value='//ul[@aria-label="Select hours"]/li')
# hr="09"
# for h in Hours:
#     if h.text==hr:
#         h.click()
#     break 
# time.sleep(1)
# Minutes=driver.find_elements(by=By.XPATH,value='//ul[@aria-label="Select minutes"]/li')
# mt="30"
# for m in Minutes:
#     if m.text==mt:
#         m.click()
#     break
# time.sleep(1)
# driver.find_element(by=By.XPATH,value='//ul[@aria-label="Select meridiem"]/li[text()="AM"]').click()
# time.sleep(4)
#
# #Clock:
# driver.find_element(by=By.XPATH,value='//a[.="Time Picker Clock"]').click()
# time.sleep(3)
# driver.find_element(by=By.XPATH,value='//input[@placeholder="hh:mm aa"]').click()
# time.sleep(3)
# HOUR=WebDriverWait(driver,15,poll_frequency=1).until(
#     e.element_to_be_clickable((By.XPATH,'//div[@class="MuiClock-clock css-eziifo"]//span[@aria-label="3 hours"]'))
# )
# driver.execute_script("arguments[0].click();", HOUR)
# # HOUR.click()
# time.sleep(2)
# driver.find_element(by=By.XPATH,value='//div[@class="MuiClock-clock css-eziifo"]//span[@aria-label="30 minutes"]').click()
# time.sleep(1)
# driver.find_element(by=By.XPATH,value='//span[.="PM"]').click()
# time.sleep(1)
# driver.find_element(by=By.XPATH,value="//button[.='OK']").click()
# time.sleep(5)


driver.close()




