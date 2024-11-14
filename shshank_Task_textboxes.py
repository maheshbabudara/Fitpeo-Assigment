from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("file:///C:/Users/MAHESH/Downloads/demo.html")
driver.implicitly_wait(10)
driver.maximize_window()
names=['mahesh','Rony','Babu','MaheshBabu','Bullet','kinguu','qu','wer','yuotube']
textboxes=driver.find_elements(by=By.XPATH,value="//input[@name='fname']")
index=0
for box in textboxes:
    box.send_keys(names[index])
    index+=1
    sleep(1)
driver.close()

