from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys, ActionChains
from time import sleep

serv_obj=Service("C:/Python_Selenium/Drivers/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("file:///C:/Users/MAHESH/Downloads/demo.html")
driver.implicitly_wait(10)
driver.maximize_window()

#customers:
rows=driver.find_elements(by=By.XPATH,value="//table[@name='customers']//tr")
columns=driver.find_elements(by=By.XPATH,value="//table[@name='customers']//th")
for r in range(2,len(rows)+1):
    for c in range(1,len(columns)+1):
        data=driver.find_element(by=By.XPATH,value="//table[@name='customers']//tr["+str(r)+"]/td["+str(c)+"]").text
        print(data, end='  ')
    print()
sleep(2)


#columns:
rows=driver.find_elements(by=By.XPATH,value="//table[@name='numbers']//tr")
columns=driver.find_elements(by=By.XPATH,value="//table[@name='numbers']//tr/th")
for r in range(2,len(rows)+1):
    for c in range(1,len(columns)+1):
        data=driver.find_element(by=By.XPATH,value="//table[@name='numbers']//tr["+str(r)+"]/td["+str(c)+"]").text
        print(data, end=' ')
    print()
sleep(2)
driver.close()

