from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
serv_obj=Service("C:/Python_Selenium/Drivers/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
sleep(1)

#Logo of webshop:
# elemnt=driver.find_element(by=By.CLASS_NAME, value='header-logo')  #class name
# elemnt.click()
# sleep(10)
# driver.find_element(by=By.TAG_NAME, value="a").click()  #Tagname
# sleep(1)
# driver.find_element(by=By.CSS_SELECTOR, value="input[value='3']").click()  #input[attribute='value']
# sleep(1)
# driver.find_element(by=By.CSS_SELECTOR, value="span.cart-label").click()  #Tagname.classvalue
# sleep(1)
# driver.find_element(by=By.CSS_SELECTOR, value="input[value='Search store']").send_keys("laptop") #sending data in search bar
# sleep(1)
# driver.find_element(by=By.CSS_SELECTOR, value="input[value='Search']").click()  #sear ch butn click
# sleep(2)
# driver.find_element(by=By.CSS_SELECTOR, value="input[value='Add to cart']").click()  #Add to cart
# sleep(2)
# driver.find_element(by=By.CSS_SELECTOR, value="span[class='cart-label']").click()
# sleep(2)
# driver.find_element(by=By.CSS_SELECTOR, value="input[type='checkbox']").click()
# sleep(2)
# driver.find_element(by=By.CSS_SELECTOR, value="input[value='Update shopping cart']").click()
# sleep(4)

#XPATH for ADD To Cart:
# driver.find_element(by=By.XPATH, value="//a[@class='ico-login']").click()
# sleep(1)
# driver.find_element(by=By.XPATH, value="//input[@name='Email']").send_keys("TinkuTiku@gmail.com")
# sleep(1)
# driver.find_element(by=By.CSS_SELECTOR,value="input[name='Password']").send_keys("123456")
# sleep(1)
# driver.find_element(by=By.XPATH,value="//input[@value='Log in']").click()
# sleep(1)
# driver.find_element(by=By.XPATH,value="//input[@value='Search store']").send_keys("laptop")
# sleep(1)
# driver.find_element(by=By.XPATH,value="//input[@value='Search']").click()
# sleep(1)
# driver.find_element(by=By.XPATH,value="//input[@value='Add to cart']").click()
# sleep(1)
# driver.find_element(by=By.XPATH,value= "(//*[text()='Shopping cart'])[1]").click()
# sleep(1)
# driver.find_element(by=By.XPATH,value="//input[@name='removefromcart']").click()
# sleep(1)
# driver.find_element(by=By.XPATH,value="//input[@name='updatecart']").click()
# sleep(3)
# driver.find_element(by=By.XPATH,value="(//a[contains(text(),'Electronics')])[1]").click()
# sleep(1)
# driver.find_element(by=By.XPATH,value="(//a[@title='Show products in category Camera, photo'])[1]").click()
# sleep(1)
# driver.find_element(by=By.XPATH,value="//img[@title='Show details for 1MP 60GB Hard Drive Handycam Camcorder']").click()
# sleep(1)
# driver.find_element(by=By.XPATH,value="//input[@value='Add to compare list']").click()
# sleep(1)
# driver.find_element(by=By.XPATH,value="//input[@title='Remove']").click()
# sleep(1)
# # driver.find_element(by=By.CSS_SELECTOR, value="a[class='ico-logout']").click()
# # sleep(1)
# driver.find_element(by=By.XPATH, value="//ul[@class='top-menu']/li[6]").click()
# sleep(1)
# driver.find_element(by=By.XPATH, value="//div[@class='product-grid']/div[1]/div[1]/div[2]/div[3]/div[2]/input").click()
# sleep(1)
# driver.find_element(by=By.XPATH, value="//input[@id='add-to-cart-button-71']").click()   #Exists BUg here
# sleep(6)




#Registration Automation code:
# driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Regist').click()
# sleep(1)
# driver.find_element(by=By.ID, value='gender-female').click()
# sleep(1)
# driver.find_element(by=By.CSS_SELECTOR,value="input#FirstName").send_keys("Tinku")
# sleep(1)
# driver.find_element(by=By.CSS_SELECTOR, value='input#LastName').send_keys("Tiku")
# sleep(1)
# driver.find_element(by=By.XPATH, value="//input[@name='Email']").send_keys("TinkuTiku@gmail.com") #email
# sleep(1)
# driver.find_element(by=By.XPATH, value="//input[@id='Password']").send_keys("123456") #pwd
# sleep(1)
# driver.find_element(by=By.XPATH, value="//input[@id='ConfirmPassword']").send_keys("123456")
# sleep(1)
# driver.find_element(by=By.XPATH, value="//input[@id='register-button']").click()
# sleep(1)
# message=driver.find_element(by=By.XPATH, value="//div[@class='result']").text
# if message=="Your registration completed":
#         driver.find_element(By.XPATH, "//input[@value='Continue']").click()
# else:
#     exists_msg=driver.find_element(by=By.XPATH, value="//li[text()='The specified email already exists']").text
#     if exists_msg=="The specified email already exists":
#         driver.find_element(by=By.CSS_SELECTOR, value="a[class='ico-login']").click()
#     print("Registration message is wrong")


#Login Automation code:
# driver.find_element(by=By.CSS_SELECTOR, value="a[class='ico-login']").click()  #Login link
# # driver.find_element(by=By.PARTIAL_LINK_TEXT, value="Log").click()  #partial link text
# sleep(1)
# driver.find_element(by=By.CSS_SELECTOR, value="input[name='Email']").send_keys("TinkuTiku@gmail.com")  #UN
# sleep(1)
# driver.find_element(by=By.CSS_SELECTOR, value="input[name='Password']").send_keys("123456") #pwd
# sleep(1)
# driver.find_element(by=By.CSS_SELECTOR, value="input[value='Log in']").click()  #login btn
# sleep(1)
# driver.find_element(by=By.CSS_SELECTOR, value="a[class='ico-logout']").click()
# sleep(4)


#Logi n and Regirstration using text():
driver.find_element(by=By.XPATH, value="//*[text()='Register']").click()
sleep(1)
driver.find_element(by=By.XPATH, value="//input[@id='gender-male']").click()
sleep(1)
driver.find_element(by=By.XPATH, value="//input[@name='FirstName']").send_keys("kou")
sleep(1)
driver.find_element(by=By.XPATH, value="//input[@name='LastName']").send_keys("ko")
sleep(1)
driver.find_element(by=By.XPATH, value="//input[@name='FirstName']")






