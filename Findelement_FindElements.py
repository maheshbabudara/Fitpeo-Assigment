from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

##############################################find_element(): returns single value element output

#Scenario1: Locator matching to single web element:
# element=driver.find_element(by=By.XPATH, value='//*[@id="small-searchterms"]')
# element.send_keys("Apple Mac book pro")
# time.sleep(3)

#Scenario2: Locator matching to Multiple web Elements:
# element=driver.find_element(by=By.XPATH, value="//div[@class='footer']//a") #since we used find_element() will return first matched element value
# print(element.text)  #printing the text value of first matched web element
# time.sleep(3)

#Scenario3: Element not Available or unable to find element and then throws NosuchElement Exception
# login_element=driver.find_element(by=By.XPATH, value='/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a')
# login_element=driver.find_element(by=By.XPATH, value='/html/a')
# login_element.click()
# time.sleep(3)


##############################################find_elements(): returns Multiple web elements and also returns in List collection

#Scenario1: Locator Matching to single web element:
# elements=driver.find_elements(by=By.XPATH, value='//*[@id="small-searchterms"]')
# print(len(elements))
# print(elements[0].text)
# elements[0].send_keys("Apple Mac book pro") #we can access these list of element through Indexing and can perform actions
# time.sleep(4)

#Scenario2: Locator matching to Multiple web Elements:
# elements=driver.find_elements(by=By.XPATH, value="//div[@class='footer']//a")
# print(len(elements))

#used for loop for bring all texts of multiple elements:
# for i in range(23):
#     print(elements[i].text);
#another way:
# for i in elements:
#     print(i.text)


#wrt specific index we can bring text:
# print(elements[0].text)
# print(elements[10].text)
# time.sleep(4)


#Scenario3: Element not Available or unable to find element and since find_elements() return 'List' then result will be 0(zero) instead of 'NoSuchElementException' erro
# login_element=driver.find_element(by=By.XPATH, value='/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a')
# login_elements=driver.find_elements(by=By.XPATH, value='/html/a')
# print(len(login_elements))
# time.sleep(3)


#find element:
#single element:
# driver.find_element(by=By.XPATH, value="//ul[@class='top-menu notmobile']//a[text()='Computers ']").click()
# time.sleep(5)
# driver.refresh()
#Multiple elements:
# driver.find_element(by=By.XPATH, value="//a[text()='Computers ']").click()
# time.sleep(6)
#Element not exists:
# driver.find_element(by=By.XPATH, value="//a[text()='Compute']").click()
# time.sleep(4)
# driver.close()

#Find Elements:

#Single element:
# Desktop=driver.find_elements(by=By.XPATH, value="//ul[@class='top-menu notmobile']//a[text()='Computers ']")
# print(len(Desktop))
# Desktop[0].click()
# time.sleep(5)

#Multiple elements:
# Desktops=driver.find_elements(by=By.XPATH, value="//div[@class='footer']//a")
# print(len(Desktops))
# for d in Desktops:
#     print(d.text)
# time.sleep(5)

#No elements Exists:
Desktops=driver.find_elements(by=By.XPATH, value="//div[@class='f']")
for d in Desktops:
    print(d.text)


