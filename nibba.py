from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from time import sleep

serv=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
option=webdriver.ChromeOptions()
option.add_argument("--disable-Notifications")

driver=webdriver.Chrome(service=serv, options=option)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

aler=WebDriverWait(driver,10).until(
   e.visibility_of_element_located((By.XPATH, "//button[text()='Alert']"))
)
aler.click()
#alert text:
alm=driver.switch_to.alert
print(alm.text)
alm.dismiss()

#alert accept:
elemen=WebDriverWait(driver,10).until(
    e.presence_of_element_located((By.XPATH, "//button[text()='Confirm Box']"))
)
elemen.click()

a=driver.switch_to.alert
a.accept()

#alert send keys:
send=WebDriverWait(driver,10).until(
    e.presence_of_element_located((By.XPATH, "//button[text()='Prompt']"))
)
send.click()

test=driver.switch_to.alert
test.send_keys("Sarileru neekevaru")
test.accept()

sleep(5)


