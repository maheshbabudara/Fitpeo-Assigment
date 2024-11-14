import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

serv=Service("C:\Python_Selenium\Drivers\chromedriver-win64|\chromedriver.exe")
driver=webdriver.Chrome()
driver.get("file:///C:/Users/MAHESH/Downloads/demo.html")
driver.implicitly_wait(10)
driver.maximize_window()


#My Approaxch:
# rows=driver.find_elements(by=By.XPATH,value='//table[@name="customers"]/tbody/tr')
# d={}
#
# for r in range(2,len(rows)+1):
#     lastname=driver.find_element(by=By.XPATH,value="//table[@name='customers']/tbody/tr["+str(r)+"]/td[3]").text
#     percentage=driver.find_element(by=By.XPATH,value="//table[@name='customers']/tbody/tr["+str(r)+"]/td[4]").text
#     if lastname not in d:
#         d[lastname]=percentage
# print(d)

#Shashank Approcah:
names=driver.find_elements(by=By.XPATH,value='//table[@name="customers"]/tbody/tr/td[3]')
nam=[]
for n in names:
    nam.append(n.text)
d={}
for p in nam:
    data=driver.find_element(by=By.XPATH,value= f'//table[@name="customers"]/tbody/tr/td[.="{p}"]/../td[4]').text
    if p not in d:
        d[p]=data
print(d)

#Shashank Ascending order:
percent_elements=driver.find_elements(by=By.XPATH,value='//table[@name="customers"]/tbody/tr/td[4]')
percentages=[]
for p in percent_elements:
    percentages.append(p.text)
percentages.sort()
d={}
for percent in percentages:
    name=driver.find_element(by=By.XPATH, value=f"//table[@name='customers']/tbody//td[text()='{percent}']/../td[3]").text
    if name not in d:
        d[name]=percent
print(d)









