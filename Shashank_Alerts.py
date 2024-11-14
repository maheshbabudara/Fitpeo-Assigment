from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import Keys, ActionChains
from time import sleep

serv_obj = Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
option = webdriver.ChromeOptions()
option.add_argument("--disable-Notifications")
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=serv_obj, options=option)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(by=By.XPATH, value="//button[text()='Click for JS Alert']").click()
alt = driver.switch_to.alert
alt.accept()
sleep(1)
driver.find_element(by=By.XPATH, value="//button[text()='Click for JS Confirm']").click()
alt.accept()
sleep(1)
driver.find_element(by=By.XPATH, value="//button[text()='Click for JS Prompt']").click()
alt.send_keys("Rony Mahesh")
alt.accept()
sleep(5)
driver.close()
