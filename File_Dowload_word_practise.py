from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver import ActionChains, Keys
from time import sleep
import os
location=os.getcwd()

serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
preferences={"download.default_directory":location}
option=webdriver.ChromeOptions()
option.add_argument("--disable-Notifications")
option.add_experimental_option("detach", True)
option.add_experimental_option("prefs",preferences)

driver=webdriver.Chrome(service=serv_obj, options=option)
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(by=By.XPATH, value="//a[contains(@href,'https://file-examples.com/wp-content/storage/2017/02/file-sample_100kB.doc') and text()='Download sample DOC file']").click()
sleep(5)
driver.close()