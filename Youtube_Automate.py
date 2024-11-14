from selenium import  webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
def setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj=Service("C:/Python_Selenium/Drivers/chromedriver-win64/chromedriver.exe")
    driver=webdriver.Chrome(service=serv_obj)
    return driver
my_driver=setup()
my_driver.implicitly_wait(10)
my_driver.get("https://www.youtube.com/")
my_driver.maximize_window()

my_driver.find_element(by=By.XPATH, value="//input[@id='search']").send_keys("roar of kesari")  #search bar
sleep(1)
my_driver.find_element(by=By.XPATH, value="//button[@id='search-icon-legacy']").click() #search button
sleep(1)
my_driver.find_element(by=By.XPATH, value="(//yt-formatted-string[text()='Roar of Kesari | Lyrical Video | Bhagavanth Kesari | NBK | Sree Leela | Anil Ravipudi | Thaman S'])[1]").click()
sleep(30)
# ad=my_driver.switch_to.alert
# ad.dismiss()
sleep(1)
# my_driver.find_element(by=By.XPATH, value="//button[@title='Pause (k)']").click()
# sleep(1)
# settings=WebDriverWait(my_driver,10).until(
#     ec.element_to_be_clickable((By.XPATH,"//button[@class='ytp-button ytp-settings-button']"))
# )
# settings.click()


my_driver.find_element(by=By.XPATH, value="//button[@class='ytp-button ytp-settings-button']").click()
sleep(2)

my_driver.find_element(by=By.XPATH, value="//yt-formatted-string[text()='720p']").click()
sleep(3)

my_driver.find_element(by=By.XPATH, value="//button[@title='Play (k)']").click()
sleep(5)
