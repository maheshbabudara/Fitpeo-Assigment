# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# def setup():
#     from selenium.webdriver.chrome.service import Service
#     serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
#     driver=webdriver.Chrome(service=serv_obj)
#     return driver
#
# my_driver=setup()
# my_driver.implicitly_wait(10)
# my_driver.get("https://demo.automationtesting.in/Frames.html")
# my_driver.maximize_window()
# time.sleep(1)
# my_driver.minimize_window()
# time.sleep(1)
# my_driver.maximize_window()
#
# my_driver.find_element(by=By.XPATH, value='/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a').click()
#
# my_driver.switch_to.frame(my_driver.find_element(by=By.XPATH, value='//*[@id="Multiple"]/iframe')) #switching to outer frame using elements xpath
# time.sleep(1)
# my_driver.switch_to.frame(my_driver.find_element(by=By.XPATH, value='/html/body/section/div/div/iframe')) #swicthing to inner frame uisng elements xpath
# time.sleep(1)
# my_driver.find_element(by=By.XPATH, value='/html/body/section/div/div/div/input').send_keys("Mahesh Babu")
# time.sleep(3)
#
# my_driver.close()
#

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from time import sleep
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
option=webdriver.ChromeOptions()
option.add_argument("--disable-Notifications")

driver=webdriver.Chrome(service=serv_obj,options=option)
driver.get("https://www.hyrtutorials.com/p/frames-practice.html#google_vignette")
driver.maximize_window()

#swicthing frame by ID:
frame1=driver.switch_to.frame("frm1")
drp_down=Select(driver.find_element(by=By.ID, value="selectnav1"))
drp_down.select_by_visible_text("Tech News")
sleep(3)
# driver.switch_to.default_content()
driver.switch_to.parent_frame()

#switching frame by Name:
driver.switch_to.frame("frm2")
# label=driver.find_element(by=By.XPATH, value="//li[text()='Radiobutton']").click()
driver.find_element(by=By.ID, value="firstName").send_keys("Mahesh Babu")
driver.find_element(by=By.ID, value="femalerb").click()
# driver.switch_to.default_content()
driver.switch_to.parent_frame()
print(driver.title)

sleep(5)



