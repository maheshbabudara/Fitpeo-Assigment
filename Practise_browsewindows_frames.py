from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
    driver=webdriver.Chrome(service=serv_obj)
    return driver

my_driver=setup()

my_driver.implicitly_wait(10)
my_driver.get("https://testautomationpractice.blogspot.com/")
my_driver.maximize_window()

my_driver.find_element(by=By.ID, value='Wikipedia1_wikipedia-search-input').send_keys("selenium") #search box
results=my_driver.find_element(by=By.XPATH, value='//*[@id="Wikipedia1_wikipedia-search-form"]/div/span[2]/span[2]/input').click()  #search button
my_driver.find_element(by=By.XPATH, value='//*[@id="wikipedia-search-result-link"]/a').click()

time.sleep(3)

#switching:
print(my_driver.window_handles)
IDs=my_driver.window_handles

for i in IDs:
    my_driver.switch_to.window(i)
    print(my_driver.title)
    time.sleep(2)

my_driver.quit()



