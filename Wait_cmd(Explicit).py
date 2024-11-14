# from selenium import webdriver
# from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# serv_obj = Service('C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe')
#
# driver = webdriver.Chrome(service=serv_obj)
#
# #Explicitwait declaration: and 'ignored_exceptions' are written to handle the exceptions withput try & exception blocks.
# MyWait = WebDriverWait(driver, 10,poll_frequency=2, ignored_exceptions=[NoSuchElementException,
#                                                        ElementNotVisibleException,
#                                                        ElementNotSelectableException,
#                                                        Exception])
#
# driver.get('https://www.google.co.in/')
# driver.maximize_window()
#
# search_box = driver.find_element(by=By.XPATH, value='//*[@id="APjFqb"]')
# search_box.send_keys('Selenium')
# search_box.submit()
#
# #Explicit condition along with Declaration:
# search_link = MyWait.until(EC.presence_of_element_located(
#     (By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3'))
# )
#
# #Testing percpective this code will works:
# # if MyWait.until(EC.presence_of_element_located(
# #     (By.XPATH, '//*[@id="rso"]'))
# # ) is True:
# #     print('satisfied')
# # else:
# #     print('bug Exists')
#
# search_link.click()
# driver.quit()
import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotSelectableException, ElementNotVisibleException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.bigbasket.com/?utm_source=google&utm_medium=cpc&utm_campaign=Brand-T1&gad_source=1&gclid=EAIaIQobChMIldXawuOZhwMVVahmAh2lpwI1EAAYASAAEgJttvD_BwE")
driver.maximize_window()

mywait=WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions= [NoSuchElementException,ElementNotSelectableException,ElementNotVisibleException])

Ayurveda=mywait.until(
    ec.element_to_be_clickable((By.XPATH, "//img[@src='https://www.bigbasket.com/media/uploads/banner_images/hp_topstrip_m_250923_03.png?tr=w-3840,q=80']"))
)
Ayurveda.click()
time.sleep(6)

if "ayurveda" in driver.current_url:
    print("Test case passed")
else:
    print("Test case Failed")

