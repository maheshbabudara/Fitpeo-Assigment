import time

from selenium import webdriver
from selenium.webdriver.common.by import By
def setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
    driver=webdriver.Chrome(service=serv_obj)
    return driver

my_driver= setup()
my_driver.implicitly_wait(10)
my_driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
my_driver.maximize_window()

my_driver.find_element(by=By.NAME, value='username').send_keys("Admin")
# my_driver.find_element(by=By.NAME, value='password').send_keys("admin123")

# my_driver.find_element(by=By.XPATH, value="//*[@class='oxd-input oxd-input--active' and @name='username']").send_keys("Admin")
my_driver.find_element(by=By.XPATH, value="//input[@placeholder='Password' or @name='password']").send_keys("admin123")
my_driver.find_element(by=By.XPATH, value="//*[contains(@type,'submit')]").click()

PIM=my_driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span')

#App cmds:
print(my_driver.title)
print(my_driver.current_url)

#Conditionals cmd's:
print("Displayed status:",PIM.is_displayed())
print("Enabled status:",PIM.is_enabled())
print("Selected status:",PIM.is_selected())


#Navigational cmd's:
my_driver.back()
my_driver.forward()
my_driver.refresh()


time.sleep(3)
my_driver.close()





