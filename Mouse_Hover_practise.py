from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

def setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
    driver=webdriver.Chrome(service=serv_obj)
    return driver

my_driver=setup()
my_driver.implicitly_wait(10)
my_driver.get("https://demowebshop.tricentis.com/")
my_driver.maximize_window()


drp=my_driver.find_element(by=By.XPATH, value='/html/body/div[4]/div[1]/div[4]/div[1]/div[1]/div[2]/ul/li[1]/a')



#Mouse actions:
action = ActionChains(my_driver)

action.move_to_element(drp).click().perform()   #drp
time.sleep(2)

drp2=my_driver.find_element(by=By.XPATH, value='/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[3]/div[5]/div/div[2]/h2/a')
action.move_to_element(drp2).click().perform()   #drp2
time.sleep(3)
my_driver.close()