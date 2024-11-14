from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")

driver=webdriver.Chrome(service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#finding rows and columns:
rows=WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='HTML1']/div[1]/table/tbody/tr")))
columns=WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='HTML1']/div[1]/table/tbody/tr[1]/th")))

print(len(rows))
print(len(columns))

#printing all rows and columns data:
for r in range(2,len(rows)+1):
    for c in range(1,len(columns)+1):
        data= driver.find_element(by=By.XPATH, value="//*[@id='HTML1']/div[1]/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data, end=' ')
    print()

#Read Data beased on the condition:
for r in range(2,len(rows)+1):
    subject= driver.find_element(by=By.XPATH, value="//*[@id='HTML1']/div[1]/table/tbody/tr["+str(r)+"]/td[3]").text
    if subject=="Javascript":
        BookName=driver.find_element(by=By.XPATH, value="//*[@id='HTML1']/div[1]/table/tbody/tr["+str(r)+"]/td[1]").text
        print(BookName)











