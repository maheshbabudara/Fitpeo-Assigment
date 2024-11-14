# ctrl+a
# ctrl+c
# TAB
# ctrl+v


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains, Keys
import time

from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By


serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)  #browser launch
driver.implicitly_wait(10)

driver.get("https://text-compare.com/")  #web application launch
driver.maximize_window()

driver.find_element(by=By.ID, value='inputText1').send_keys("mahesh Babu ki jai")

act=ActionChains(driver)

#ctrl+a:
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
time.sleep(1)
#ctrl+c:
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
time.sleep(1)
#TAB:
act.send_keys(Keys.TAB).perform()
time.sleep(1)
#ctrl+v:
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(3)


driver.close()

driver.switch_to.new_window()

