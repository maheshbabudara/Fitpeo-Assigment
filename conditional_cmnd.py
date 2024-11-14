#conditional cmd's:
# is_displayed():used to check whether element is displayed or not, if yes returns True else False
#is_enabled():used to check whether particular element is enabled or not, if yes returns True else False
#is_selected():used to check whether particular element is selected or not , mainly deals with Radiobuttons and checkboxes.
import time

#Note: Conditional cmd's are accessible thorough "web elements" but not "driver".


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
# driver=webdriver.Chrome(service=serv_obj)
# driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
# driver.maximize_window()
#
#
# #is_displayed() and is_enabled():
# search_box=driver.find_element(by=By.XPATH, value="//*[@id='small-searchterms']")
# print("search_box displayed status:",search_box.is_displayed())
# print("Enabled status:",search_box.is_enabled())
#
#
# #is_selected():
# # radio_btn=driver.find_element(by=By.ID, value="gender-male")
# radio_btn=driver.find_element(by=By.XPATH, value="//*[@id='gender-male']")
# radio_btn_femal=driver.find_element(by=By.XPATH, value='//*[@id="gender-female"]')
# print('radio_button status:',radio_btn.is_selected())
# print('radio_button_female status:',radio_btn_femal.is_selected())
# radio_btn.click()
# # radio_btn_femal.click()
# print('radio_button  status after click:',radio_btn.is_selected())
# print('radio_button_female status: after click:',radio_btn_femal.is_selected())

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

def setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
    driver=webdriver.Chrome(service=serv_obj)
    return driver
my_driver=setup()
my_driver.get("https://www.bigbasket.com/?utm_source=google&utm_medium=cpc&utm_campaign=Brand-T1&gad_source=1&gclid=EAIaIQobChMIldXawuOZhwMVVahmAh2lpwI1EAAYASAAEgJttvD_BwE")
my_driver.maximize_window()
my_driver.implicitly_wait(10)
Meat=WebDriverWait(my_driver,10).until(
    ec.presence_of_element_located((By.XPATH, "//img[@src='https://www.bigbasket.com/media/uploads/banner_images/hp_topstrip_m_250923_01.png?tr=w-3840,q=80']"))
)
print("status of Meta:",Meat.is_displayed())
time.sleep(1)
Sasta=WebDriverWait(my_driver,10).until(
    ec.presence_of_element_located((By.XPATH, "//li[@style='opacity: 1;']//span[text()='₹82']/../../..//span[text()='Har Din Sasta!']"))
)
print("status f sasta:",Sasta.is_enabled())
time.sleep(5)
cauliflower=my_driver.find_element(by=By.XPATH, value="//*[text()='₹145']/../../..//div[@class='flex items-center justify-between w-full h-full']").click()
time.sleep(5)
my_driver.execute_script("arguments[0].click();",cauliflower)
time.sleep(3)






