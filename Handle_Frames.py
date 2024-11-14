from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time as t
from selenium.webdriver.support.select import Select


serv_obj = Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.implicitly_wait(10)
driver.get("https://www.selenium.dev/selenium/docs/api/Java")
driver.maximize_window()


#1.Scenario on swicthing Frames:
# We are switching to FRAME and coming out of frame:
driver.switch_to.frame('packageListFrame')  #this will enter to frame with name of the frame
driver.find_element(by=By.LINK_TEXT, value='org.openqa.selenium').click()
driver.switch_to.default_content() #this will goes back to main page

driver.switch_to.frame("packageFrame")
driver.find_element(by=By.LINK_TEXT, value='WebDriver').click()
driver.switch_to.default_content()

driver.switch_to.frame("classFrame")
driver.find_element(by=By.XPATH, value='').click()

driver.quit()
