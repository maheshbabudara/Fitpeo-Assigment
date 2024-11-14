from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj= Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()


#1.Count No of Rows and Columns in Table:
count_row= driver.find_elements(by=By.XPATH, value='//*[@id="HTML1"]/div[1]/table//tr')  #In XPATH if we uses "//" means skiping an Tag. here in this path weskipped "tbody" tag
print("No of Rows:",len(count_row))
count_coloumn=driver.find_elements(by=By.XPATH, value= '//*[@id="HTML1"]/div[1]/table//tr[1]/th')  #In XPATH if we uses "//" means skiping an Tag. here in this path weskipped "tbody" tag
print("No of Clumns: ",len(count_coloumn))

#2. Read specific ROW and COLUMN:
print(driver.find_element(by=By.XPATH, value='//*[@id="HTML1"]/div[1]/table//tr[4]/td[3]').text)   #Javascript
print(driver.find_element(by=By.XPATH, value='//*[@id="HTMSL1"]/div[1]/table/tbody/tr[6]/td[3]').text)  #Java

#3. Read all Rows Data and Columns Data:
print("Printing all Rows and Columns Data:")
for r in range(2,len(count_row)+1):
    for c in range(1,len(count_coloumn)+1):
        # Dynamic Xpath by loops:
        data=driver.find_element(by=By.XPATH, value="//*[@id='HTML1']/div/table//tr["+str(r)+"]/td["+str(c)+"]").text
        print(data, end=' ')
    print()
    time.sleep(4)

#4. Read Data based on condition(List of Book Names who's auther is Mukesh):
# for r in range(2,len(count_row)+1):
#     #making rows as dynamic xpath
#     author=driver.find_element(by=By.XPATH, value="//*[@id='HTML1']/div[1]/table/tbody/tr["+str(r)+"]/td[2]").text
#     if author=="Mukesh":
#         Book_Name=driver.find_element(by=By.XPATH, value="//*[@id='HTML1']/div[1]/table/tbody/tr["+str(r)+"]/td[1]").text
#         price=driver.find_element(by=By.XPATH, value="//*[@id='HTML1']/div[1]/table/tbody/tr["+str(r)+"]/td[4]").text
#         print(Book_Name,"-",author,"-",price)



