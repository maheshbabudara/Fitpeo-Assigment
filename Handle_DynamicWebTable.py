# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
#
# serv_obj= Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
# driver=webdriver.Chrome(service=serv_obj)
# driver.implicitly_wait(10)
#
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.maximize_window()
#
# #Login:
# driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")
# driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys('admin123')
# driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
#
# #Admin:
# driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click()
# #User management:
# driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span').click()
# #Users:
# driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li/a').click()
#
#
#
# #Total no of rows:
# rows=len(driver.find_elements(by=By.XPATH, value="//table[@id='resultTable']/tbody/tr"))
# print('total rows:',rows)
#
#
#
# #Finding status of users:
# count=0
# for r in range(1, rows+1):  #we choosed 1 becoz, in this table No Header columns, existing header is present in separate web element so poicked from 1
#     status=driver.find_element(by=By.XPATH, value='//table[@id=""resultTable]/tbody/tr["+str(r)+"]/td[5]').text
#     print(status)
#     if status=="Enabled":
#         count+=1;
#
#
# print("Number of Enabled Users:",count)
# print("Total Number of User", rows)   #Rows equals to users, so we used rows for total no of users in table
# print("Total no of Disabled users", rows-count)  #total users-enabled users = disabled users



#Assignment Task:
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from time import sleep
serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
option=webdriver.ChromeOptions()
option.add_argument("--disable-Notifications")
driver=webdriver.Chrome(service=serv_obj,options=option)
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

# element=WebDriverWait(driver,10).until(
#     e.presence_of_element_located((By.XPATH, '//input[@name="username"]'))
# )
# element.send_keys("Admin")
# driver.find_element(by=By.XPATH, value="//input[@name='password']").send_keys("admin123")
# sleep(1)
# driver.find_element(by=By.XPATH, value="//button[text()=' Login ']").click()
# sleep(3)
# driver.find_element(by=By.XPATH, value="//span[text()='Admin']").click()
# sleep(1)
# driver.find_element(by=By.XPATH, value="//span[text()='User Management ']").click()
# sleep(1)
# driver.find_element(by=By.XPATH, value="//a[text()='Users']").click()
# sleep(1)

# #Table details:
# # status=driver.find_elements(by=By.XPATH, value="//div[@class='oxd-table-body']/div//div[5]")
# rows=driver.find_elements(by=By.XPATH, value="//div[@class='oxd-table-body']/div")
# count=0
# for row in rows:
#     status=row.find_element(by=By.XPATH, value=".//div[5]").text
#     if status=="Enabled":
#         # Name=row.find_element(by=By.XPATH, value=".//div[2]").text
#         role = row.find_element(by=By.XPATH, value=".//div[3]").text
#         print(role)
#     count+=1

#Table details:
rows=driver.find_elements(by=By.XPATH, value="//table[@name='BookTable']/tbody//tr")
cols=driver.find_elements(by=By.XPATH, value="//table[@name='BookTable']/tbody/tr/th")
for row in range(2,len(rows)+1):
    for col in range(1,len(cols)+1):
        data=driver.find_element(by=By.XPATH, value="//table[@name='BookTable']/tbody//tr["+str(row)+"]/td["+str(col)+"]").text
        print(data, end=' ')
    print()










