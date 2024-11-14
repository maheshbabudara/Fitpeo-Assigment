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
my_driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
my_driver.maximize_window()

my_driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a').click()

#single window:
# print(my_driver.current_window_handle)
# id=my_driver.current_window_handle
# my_driver.switch_to.window(id)
# print(my_driver.title)
# time.sleep(3)


#Multiple windows switching:
print(my_driver.window_handles)
ids=my_driver.window_handles

for i in ids:
    my_driver.switch_to.window(i)
    time.sleep(2)

    if my_driver.title=="OrangeHRM":
        my_driver.close()

my_driver.quit()




