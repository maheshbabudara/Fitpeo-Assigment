# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from time import sleep
# from selenium.webdriver import ActionChains, Keys
#
# serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
# option=webdriver.ChromeOptions()
# option.add_argument("--disable-Notifications")
# driver=webdriver.Chrome(service=serv_obj,options=option)
#
# driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")
# driver.maximize_window()
# driver.implicitly_wait(10)
# first_name=driver.find_element(by=By.ID, value="input-firstname")
# action=ActionChains(driver)
# sleep(1)
# action.send_keys("Mahesh").send_keys(Keys.TAB).send_keys("Babu").send_keys(Keys.TAB).send_keys("TinkuTiku@gmail.com").send_keys(Keys.TAB).send_keys("8639563301").send_keys(Keys.TAB).send_keys("123456").send_keys(Keys.TAB).send_keys("123456").send_keys(Keys.TAB).send_keys("Yes").send_keys(Keys.TAB).send_keys(Keys.SPACE).send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()
# sleep(10)
#
# #
# Keys.ENTER


#Assignment Task:
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains,Keys
from time import sleep

srv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
option=webdriver.ChromeOptions()
option.add_argument("--disable-Notifications")
option.add_experimental_option("detach", True)
driver=webdriver.Chrome(service=srv_obj, options=option)
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)
driver.maximize_window()

f_name=driver.find_element(by=By.XPATH, value="//input[@id='name']")
action=ActionChains(driver)
sleep(2)
action.send_keys(Keys.TAB).send_keys("mahesh").send_keys(Keys.TAB).send_keys("ma hesh@gmail.com").send_keys(Keys.TAB).send_keys("8639563301").key_down(Keys.CONTROL).send_keys("a").send_keys("c").key_up(Keys.CONTROL).send_keys(Keys.TAB).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
sleep(1)
# action.send_keys(Keys.TAB).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

sleep(5)
# action.scroll_by_amount(0,500).perform()
# sleep(2)
action.scroll_to_element(driver.find_element(by=By.XPATH, value="//div[@id='slider']")).perform()
sleep(5)
driver.close()
