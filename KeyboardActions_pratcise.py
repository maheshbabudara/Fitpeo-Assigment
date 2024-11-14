from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import ActionChains, Keys

serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://text-compare.com/")
driver.maximize_window()

driver.find_element(by=By.ID, value='inputText1').send_keys("kikku ra kikku")

action=ActionChains(driver)

#cotrl+a:
action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
#ctrl+c:
action.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
#Tab:
action.send_keys(Keys.TAB).perform()
#ctrl+v:
action.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
sleep(3)


