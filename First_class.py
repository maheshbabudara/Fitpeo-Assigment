from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver_path=("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")

# C:\\Python_Selenium\\Drivers\\chromedriver-win64\\chromedriver.exe
service=Service(chromedriver_path)
driver=webdriver.Chrome(service=service)
driver.get("https://www.facebook.com/")

driver.find_element(by=By.ID,value="email").send_keys("mahesh")
time.sleep(5)
driver.find_element(by=By.ID,value="pass").send_keys('123')
time.sleep(3)
driver.find_element(by=By.ID,value='u_0_5_vd').click()

login_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.NAME, "login"))
)
login_button.click()

driver.quit()



