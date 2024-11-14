from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import ActionChains, Keys

serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
option=webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver=webdriver.Chrome(service=serv_obj, options=option)
driver.get("https://demowebshop.tricentis.com/")
driver.implicitly_wait(10)
driver.maximize_window()

links=driver.find_elements(by=By.XPATH, value="//div[@class='column information']/ul//a")
action=ActionChains(driver)

for link in links:

    mahesh=driver.find_element(by=By.LINK_TEXT, value=link.text)
    action.key_down(Keys.CONTROL).click(mahesh).key_up(Keys.CONTROL).perform()

sleep(3)
driver.quit()
