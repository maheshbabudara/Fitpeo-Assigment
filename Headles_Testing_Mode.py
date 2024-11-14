from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def headle_setup():
    # Set up the Chrome driver in headless mode
    serv_obj = Service("C:/Python_Selenium/Drivers/chromedriver-win64/chromedriver.exe")
    ops=webdriver.ChromeOptions()
    ops.add_argument("--headless")
    ops.add_argument("--disable-gpu")
    driver = webdriver.Chrome(service=serv_obj, options=ops)
    return driver

#Edge:
def head_setup():
    # Set up the edge driver in headless mode
    from selenium.webdriver.edge.service import Service
    serv_obj = Service("C:/Python_Selenium/Drivers/chromedriver-win64/chromedriver.exe")
    ops=webdriver.EdgeOptions()
    ops.headless = True
    driver = webdriver.Edge(service=serv_obj, options=ops)
    return driver

#Firefox:
def he_setup():
    # Set up the edge driver in headless mode
    from selenium.webdriver.firefox.service import Service
    serv_obj = Service("C:/Python_Selenium/Drivers/chromedriver-win64/chromedriver.exe")
    ops=webdriver.FirefoxOptions()
    ops.add_argument("--headless")
    ops.add_argument("--disable-gpu")
    driver = webdriver.Firefox(service=serv_obj, options=ops)
    return driver

# Initialize the driver
my_driver = headle_setup()  #chrome
# my_driver=he_setup()  #firefox
# my_driver=head_setup()  #Edge


# Open the website:
my_driver.get("https://demo.nopcommerce.com/")
my_driver.maximize_window()

# Print the page title and URL
print(my_driver.title)
print(my_driver.current_url)

# Pause for a few seconds to ensure the page is fully loaded
time.sleep(3)

# Don't forget to close the driver
my_driver.quit()
