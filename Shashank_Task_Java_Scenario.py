from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver import Keys, ActionChains
from time import sleep

serv_obj=Service("C:/Python_Selenium/Drivers/chromedriver-win64/chromedriver.exe")
option=webdriver.ChromeOptions()
option.add_argument("--disable-Notifications")
option.add_experimental_option("detach", True)
driver=webdriver.Chrome(service=serv_obj, options=option)

driver.get("https://docs.oracle.com/javase/8/docs/api/")
driver.implicitly_wait(10)
driver.maximize_window()

#main frame:
# main_frame=driver.find_element(by=By.XPATH, value="//frameset[@title='Documentation frame']")
# driver.switch_to.frame(main_frame)
# sleep(1)
console_frame=driver.find_element(by=By.XPATH, value="//frame[@name='classFrame']")
driver.switch_to.frame(console_frame)
content=driver.find_element(by=By.XPATH, value="//div[contains(text(),'Provides the classes necessary to create an applet and the classes an applet')]").text
print(content)
sleep(1)
driver.switch_to.default_content()
sleep(1)

Abrast_fram=driver.find_element(by=By.XPATH, value="//frame[@name='packageFrame']")
driver.switch_to.frame(Abrast_fram)

action=ActionChains(driver)
Abstract_item=driver.find_element(by=By.XPATH, value="//a[text()='AbstractAction']")
action.key_down(Keys.CONTROL).click(Abstract_item).perform()
sleep(1)
driver.switch_to.default_content()
sleep(1)

All_frame=driver.find_element(by=By.XPATH,value="//frame[@name='packageListFrame']")
driver.switch_to.frame(All_frame)
sleep(1)
Appetite=driver.find_element(by=By.XPATH,value="//h2[text()='Packages']/../ul/li/a[text()='java.applet']")
action.key_down(Keys.CONTROL).click(Appetite).perform()
sleep(1)
driver.switch_to.default_content()
sleep(1)
driver.quit()
