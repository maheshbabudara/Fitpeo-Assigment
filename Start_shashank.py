from selenium import webdriver
from time import sleep

def setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj=Service("C:/Python_Selenium/Drivers/chromedriver-win64/chromedriver.exe")
    driver=webdriver.Chrome(service=serv_obj)
    return driver

my_driver=setup()
my_driver.get("https://www.youtube.com/watch?v=cVZMah9kEjI")
sleep(1)
# print("window position:",my_driver.get_window_position())
# sleep(1)

my_driver.set_window_size(100,200)  #Manually setting the window size
sleep(1)
print("Size of the current window before maximize window:",my_driver.get_window_size())
sleep(1)
my_driver.maximize_window()
sleep(1)
print("Size of the current window:",my_driver.get_window_size())
sleep(1)

my_driver.close()


