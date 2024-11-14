from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
    driver=webdriver.Chrome(service=serv_obj)
    return driver

my_driver=setup()
my_driver.implicitly_wait(10)
my_driver.get("https://testautomationpractice.blogspot.com/")
my_driver.maximize_window()

#All Rows and Columns:
rows=my_driver.find_elements(by=By.XPATH, value='//*[@id="HTML1"]/div[1]/table/tbody/tr')
columns=my_driver.find_elements(by=By.XPATH, value='//*[@id="HTML1"]/div[1]/table/tbody/tr/th')

#Select specifc value:
print(my_driver.find_element(by=By.XPATH, value='//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[3]').text)
print(my_driver.find_element(by=By.XPATH, value='//*[@id="HTML1"]/div[1]/table/tbody/tr[5]/td[1]').text)


#Read all Rows and columns data:

for r in range(2,len(rows)+1):
    for c in range(1,len(columns)+1):
        data=my_driver.find_element(by=By.XPATH, value="//*[@id = 'HTML1']/div[1]/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text

        print(data, end=' ')
    print()
time.sleep(4)

#Read Data based on condition(List of Book Names who's subject is selenium):
for r in range(2,len(rows)+1):
    Subject = my_driver.find_element(by=By.XPATH,
                                     value="// *[ @ id = 'HTML1'] / div[1] / table / tbody / tr[" + str(r) + "] / td[3]").text
    print(Subject)


    if Subject=='Selenium':
        Book_Name=my_driver.find_element(by=By.XPATH, value="// *[ @ id = 'HTML1'] / div[1] / table / tbody / tr["+str(r)+"] / td[1]").text
        Author=my_driver.find_element(by=By.XPATH, value="// *[ @ id = 'HTML1'] / div[1] / table / tbody / tr["+str(r)+"] / td[2]").text
        print(Book_Name,":",Author)






