from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time as t
from selenium.webdriver.support.select import Select


serv_obj = Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/ul/li[3]/button').click()


alert_window=driver.switch_to.alert

print(alert_window.text)
t.sleep(2)
alert_window.send_keys('Mahesh Babu')
t.sleep(5)
# alert_window.accept() #closing alert popup with OK button.

alert_window.dismiss()  #Close the alert window with Cancel button.

driver.quit()




