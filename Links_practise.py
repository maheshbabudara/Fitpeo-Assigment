from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
import requests

serv_obj = Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)


#Links:
# driver.get("https://provar.com/")
# driver.maximize_window()
#
# links = driver.find_elements(by=By.XPATH, value="//a")
#
# count=0
# for l in links:
#     # print(l.text)  #text
#     print(l.get_attribute('href'))
#     count+=1
#     time.sleep(2)


#Broken links:
driver.get("http://www.deadlinkcity.com/")
links=driver.find_elements(by=By.XPATH, value="//a")

for i in links:
    # print(i.get_attribute("href"))
    broken_link=i.get_attribute("href")
    response=requests.head(broken_link)

    if response.status_code >=400:
        print("Broken link:",broken_link,"status code:",response.status_code)
    else:
        print("working url:", broken_link,"status code:",response.status_code)






