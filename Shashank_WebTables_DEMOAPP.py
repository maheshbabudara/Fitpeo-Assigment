from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as e
from time import sleep
import os
location=os.getcwd()

serv=Service("C:\Python_Selenium\Drivers\chromedriver-win64|\chromedriver.exe")
option=webdriver.ChromeOptions()
prefernces={'download.default_directory':location,'plugins.always_open_pdf_externally':True}
option.add_argument("--disable-Notifications")
option.add_experimental_option("detach",True)
option.add_experimental_option('prefs',prefernces)
# option.add_argument('--headless')
# option.add_argument('--disable-gpu')

driver=webdriver.Chrome(options=option)
driver.get("https://demoapps.qspiders.com/ui/table?scenario=1")
driver.implicitly_wait(10)
driver.maximize_window()
sleep(1)

#Printing all Data from Tables:
rows=driver.find_elements(by=By.XPATH,value='//table[@class="w-full text-sm text-left text-gray-500 "]/tbody/tr')
for r in range(1,len(rows)+1):
    data=driver.find_element(by=By.XPATH,value="//table[@class='w-full text-sm text-left text-gray-500 ']/tbody/tr["+str(r)+"]").text
    print(data)
print("______________________________________________________________________________________________________________________________________________________")

#printing data based Item Name:
item_names=driver.find_elements(by=By.XPATH,value='//table[@class="w-full text-sm text-left text-gray-500 "]/tbody/tr/th')
items=[]
for i in item_names:
    items.append(i.text)
for t in items:
    Discount=driver.find_element(by=By.XPATH,value=f'//table[@class="w-full text-sm text-left text-gray-500 "]/tbody/tr/th[text()="{t}"]/../td[3]').text
    print("Name:",t,"->",'Discount:',Discount)
print("______________________________________________________________________________________________________________________________________________________")
#printing data based on Condition of discount:
disc=driver.find_elements(by=By.XPATH,value='//table[@class="w-full text-sm text-left text-gray-500 "]/tbody/tr/td[2]')
r=[]
for item in disc:
    r.append(item.text)
print(r)
d={}
for z in r:
    if z>='5':
        data=driver.find_element(by=By.XPATH,value= f'//table[@class="w-full text-sm text-left text-gray-500 "]/tbody/tr/td[text()="{z}"]/../th').text
        if data not in d:
            d[data]=z
print(d)
print("______________________________________________________________________________________________________________________________________________________")
# Note: Please do for ratings
#printing data based on Condition of quanties for price:
quantities=driver.find_elements(by=By.XPATH,value='//table[@class="w-full text-sm text-left text-gray-500 "]/tbody/tr/td[2]')
q=[]
for i in quantities:
    q.append(i.text)
d={}
for item in q:
    if item >'3':
        names=price=driver.find_element(by=By.XPATH, value=f'//table[@class="w-full text-sm text-left text-gray-500 "]/tbody/tr/td[text()="{item}"]/../th').text
        if names not in d:
            d[names]=item
print(d)
print("______________________________________________________________________________________________________________________________________________________")
#printing data based on Condition of item names for ratings:
ratings=driver.find_elements(by=By.XPATH,value='//table[@class="w-full text-sm text-left text-gray-500 "]/tbody/tr/td[1]')
r=[]
for ra in ratings:
    r.append(ra.text)
rate=[]
for i in r:
    data=i.split()
    rate.append(data[0])
d={}
for item in rate:
    if item>='4.0':
        names=driver.find_element(by=By.XPATH,value=f'//table[@class="w-full text-sm text-left text-gray-500 "]/tbody/tr/td[text()="{item} Star"]/../th').text
        if names not in d:
            d[names]=item
print(d)
print("______________________________________________________________________________________________________________________________________________________")
#Dynamic Web Tables data:
driver.find_element(by=By.XPATH, value='//a[text()="Dynamic Web Table"]').click()
sleep(1)
rows=driver.find_elements(by=By.XPATH,value='//tbody[@class="w-full"]/tr')
for r in range(1,len(rows)+1):
    data = driver.find_element(by=By.XPATH,value=f"//tbody[@class='w-full']/tr['{r}']").text
    print("Dynamic data:",data)



