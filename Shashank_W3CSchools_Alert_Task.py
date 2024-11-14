from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys,ActionChains
from time import sleep

serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
option.add_argument("--disable-Notifications")
driver=webdriver.Chrome(service=serv_obj, options=option)
driver.get("https://www.w3schools.com/jsref/met_win_alert.asp")
driver.implicitly_wait(10)
driver.maximize_window()
alt=WebDriverWait(driver,10).until(
    e.presence_of_element_located((By.XPATH,'//div[contains(@class,"w3-example")]//div//span[contains(text(),"Hello! I am an alert box!!")]/../../../a'))
)
alt.click()
sleep(1)
ids=driver.window_handles
print(ids)
driver.switch_to.window(ids[1])
sleep(1)
driver.switch_to.frame("iframeResult")
sleep(1)
driver.find_element(by=By.XPATH,value="//button[.='Try it']").click()
sleep(2)
popup=driver.switch_to.alert
print(popup.text)
popup.accept()
sleep(2)
driver.quit()

