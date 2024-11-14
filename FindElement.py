from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
    driver=webdriver.Chrome(service=serv_obj)
    return driver

my_driver=setup()
my_driver.implicitly_wait(10)
my_driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
my_driver.maximize_window()


#Explicit:
Username = WebDriverWait(my_driver,10).until(
    EC.presence_of_element_located((By.NAME, "username"))
                                             )

Username.send_keys("Admin")

# my_driver.find_element(by=By.NAME, value='username').send_keys("Admin")
my_driver.find_element(by=By.XPATH, value="//input[@placeholder='Password' or @name='password']").send_keys("admin123")
my_driver.find_element(by=By.XPATH, value="//*[contains(@type,'submit')]").click()

menus=my_driver.find_elements(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li')

for menu in menus:
    print(menu.text)

my_driver.close()