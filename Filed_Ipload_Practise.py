# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from time import sleep
#
# serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
# driver=webdriver.Chrome(service=serv_obj)
#
# driver.implicitly_wait(10)
# driver.get("https://www.csm-testcenter.org/test?do=show&subdo=common&test=file_upload")
# driver.maximize_window()
#
# #uploading files:
# driver.find_element(by=By.XPATH, value='//*[@id="item"]/form/table/tbody/tr[1]/td[2]/input').send_keys("C:\\Users\\MAHESH\\Pictures\\Screenshots\\home.png")
#
# sleep(5)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver import ActionChains,Keys
from time import sleep

serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
option=webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
option.add_argument("--disable-Notifications")
driver=webdriver.Chrome(service=serv_obj, options=option)
driver.get("https://practice.expandtesting.com/upload")
driver.maximize_window()
driver.implicitly_wait(10)

elemen=WebDriverWait(driver, 10).until(
    e.presence_of_element_located((By.XPATH, "//input[@data-testid='file-input']"))
)
elemen.send_keys("C:\\Users\\MAHESH\\home.png")
# elemen.click()
sleep(3)
driver.close()
