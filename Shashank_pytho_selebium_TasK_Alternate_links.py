from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys,ActionChains
from time import sleep
import os
location=os.getcwd()


def setup():
    serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
    option=webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    preferences={"download.default_directory":location,"plugins.always_open_pdf_externally":True}
    option.add_argument("--disable-Notifications")
    # option.add_argument("--headless")
    # option.add_argument("--disable-gpu")
    option.add_experimental_option("prefs",preferences)
    driver=webdriver.Chrome(service=serv_obj,options=option)
    return driver

web_driver=setup()
web_driver.get("https://demowebshop.tricentis.com/")
web_driver.implicitly_wait(10)
web_driver.maximize_window()

links=web_driver.find_elements(by=By.XPATH, value='//div[@class="footer-menu-wrapper"]/div/ul//a')
index=1
action=ActionChains(web_driver)
for link in links:
    if index%2!=0:
        action.key_down(Keys.CONTROL).click(link).perform()
        print(link.text)
        sleep(1)
    index+=1
    sleep(2)

web_driver.quit()




