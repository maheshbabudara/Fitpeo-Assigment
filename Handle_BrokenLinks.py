# Pre-requisites: "requests" package should be installed through settings-->python interpreter--> search package(click +) --> install

import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time as t

serv_obj = Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.implicitly_wait(10)
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

broken_links = driver.find_elements(by=By.TAG_NAME, value="a")
count = 0

for link in broken_links:
    url = link.get_attribute('href')
    try:
        result = requests.head(url)
    except:
        None

    if result.status_code >= 400:
        print(url, ' :is an broken code')
        count += 1
    else:
        print(url, ': is an Valid Link')
print('Total number of broken Links: ', count)





