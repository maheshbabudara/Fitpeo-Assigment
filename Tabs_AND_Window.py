from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

def setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
    driver=webdriver.Chrome(service=serv_obj)
    return driver

my_driver=setup()

# my_driver.get("https://demo.nopcommerce.com/")
# my_driver.maximize_window()

#Opens New Tab withput distrurb Home page:
# my_driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a").send_keys(Keys.CONTROL+Keys.ENTER)


#New-Tabe-selenium4: opens new Tab and switches to new tab:
# my_driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
# my_driver.switch_to.new_window('tab')
# my_driver.get("https://demo.nopcommerce.com/")

#New-Tabe-selenium4: opens new Browser window and switches to new window:
my_driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
my_driver.switch_to.new_window('window')
my_driver.get("https://demo.nopcommerce.com/")

time.sleep(8)
my_driver.close()