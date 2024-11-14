# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver import Keys,ActionChains
# from time import sleep
#
# serv_obj=Service("C:/Python_Selenium/Drivers/chromedriver-win64/chromedriver.exe")
# option=webdriver.ChromeOptions()
# option.add_argument("--disable-Notifications")    #disable browser notifications
#
# option.add_experimental_option("detach",True)
# driver=webdriver.Chrome(service=serv_obj, options=option)
# driver.get("https://web-push-book.gauntface.com/demos/notification-examples/")
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.find_element(by=By.XPATH, value="//input[@class='c-toggle js-example-toggle']").click()
# sleep(5)


#Bootsrap Modal:
# driver.get("https://demoapps.qspiders.com/ui/modal?sublist=0")
# driver.maximize_window()
# driver.implicitly_wait(10)
# # driver.find_element(by=By.XPATH, value="//section[.='Popups']").click()
# # driver.find_element(by=By.XPATH, value="//section[.='Modal']").click()
# driver.find_element(by=By.XPATH, value="//button[text()='Open Modal']").click()
# sleep(3)
# driver.find_element(by=By.ID, value="closeModal").click()
# sleep(5)
# driver.close()


#light box:
# driver.get("https://www.bigbasket.com/")
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.find_element(by=By.XPATH, value="//button[.='Login/ Sign Up']").click()
# sleep(2)
# driver.find_element(by=By.XPATH, value="//input[@placeholder='Enter Phone number/ Email Id']").send_keys('8639563301')
# sleep(3)
# driver.find_element(by=By.XPATH, value="//button[.='Continue']").click()
# sleep(3)
# driver.close()
#
# #cookies:
# driver.get("https://www.cogstate.com/?gad_source=1&gclid=Cj0KCQjw-5y1BhC-ARIsAAM_oKlKaFYLUfPV_bfJYtgDg3EiQRaeEbQ4OFr-DbwbTiJRHrJLbhUF914aAu-XEALw_wcB")
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.find_element()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver import Keys,ActionChains
from time import sleep
import os
location=os.getcwd()

serv_obj=Service("C:/Python_Selenium/Drivers/chromedriver-win64/chromedriver.exe")
preferences={"download.default_directory":location,"plugins.always_open_pdf_externally":True}
option=webdriver.ChromeOptions()
option.add_argument("--disable-Notifications")
option.add_experimental_option('prefs',preferences)
option.add_experimental_option("detach",True)
option.add_argument("--headless")
option.add_argument("--disable-gpu")
driver=webdriver.Chrome(service=serv_obj, options=option)

#Browser push Notifications:
driver.get("https://web-push-book.gauntface.com/demos/notification-examples/")
driver.maximize_window()
driver.implicitly_wait(10)
Toggle=WebDriverWait(driver,10).until(
    e.visibility_of_element_located((By.XPATH, '//input[contains(@class,"c-toggle js-example-toggle")]'))
)
Toggle.click()
sleep(3)

#Bootstrap Dialog Box:
driver.get("https://demoapps.qspiders.com/ui?scenario=1")
driver.maximize_window()
driver.implicitly_wait(10)
Popups=WebDriverWait(driver,10).until(
    e.presence_of_element_located((By.XPATH, "//section[.='Popups']"))
)
Popups.click()
sleep(1)
driver.find_element(by=By.XPATH, value="//section[.='Modal']").click()
sleep(1)
driver.find_element(by=By.XPATH, value="//button[.='Open Modal']").click()
sleep(1)
Dialog_box=driver.find_element(by=By.XPATH, value="//button[.='×']").text
print(Dialog_box)
sleep(1)
driver.find_element(by=By.XPATH, value="//button[.='×']").click()
sleep(3)

#Light Box:
driver.get("https://www.bigbasket.com/?utm_source=google&utm_medium=cpc&utm_campaign=Brand-T1&gad_source=1&gclid=EAIaIQobChMI_b_KweyWhwMVrBGtBh3UXQAGEAAYASAAEgIkOfD_BwE")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(by=By.XPATH, value="//*[.='Login/ Sign Up']").click()
sleep(1)
driver.find_element(by=By.XPATH, value="//input[@name='multiform']").send_keys("8639563301")
sleep(1)
driver.find_element(by=By.XPATH, value="//button[.='Continue']").click()
sleep(2)

#Cookies:
driver.get("https://www.cogstate.com/?gad_source=1&gclid=Cj0KCQjw-5y1BhC-ARIsAAM_oKlKaFYLUfPV_bfJYtgDg3EiQRaeEbQ4OFr-DbwbTiJRHrJLbhUF914aAu-XEALw_wcB")
driver.maximize_window()
driver.implicitly_wait(10)
print("List of cookies in cogatste website:",driver.get_cookies())
print(len(driver.get_cookies()))

#Adding Cookies:
driver.add_cookie({'name':'Rony','value':'3'})
print('After adding cookie:',driver.get_cookies())
print(len(driver.get_cookies()))

#Deleting specific Cookie:
driver.delete_cookie('Rony')
print('After deleting specific cookie:',len(driver.get_cookies()))

#Deleting all cookies:
driver.delete_all_cookies()
print('After deleting all cookies:',len(driver.get_cookies()))
driver.close()

