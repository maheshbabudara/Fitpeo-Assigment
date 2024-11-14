from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

serv_obj=Service("C:/Python_Selenium/Drivers/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://www.google.co.in/")
driver.maximize_window()
sleep(1)
driver.find_element(by=By.XPATH, value="//textarea[@title='Search']").send_keys("amazon")
sleep(1)
driver.find_element(by=By.XPATH, value="//div[@aria-label='amazon']").click()
sleep(1)
driver.find_element(by=By.XPATH, value="//h3[text()='Amazon.in']").click()
sleep(1)
driver.find_element(by=By.XPATH, value="//span[text()='Account & Lists']").click()
sleep(3)
driver.find_element(by=By.XPATH, value="//input[@id='ap_email_login']").send_keys("8639563301")
sleep(5)
driver.find_element(by=By.XPATH, value="//input[@type='submit']").click()
sleep(2)
driver.find_element(by=By.XPATH, value="//input[@name='password' and @id='ap_password']").send_keys("Ronyrani@1201")
sleep(2)
driver.find_element(by=By.XPATH, value="//input[@id='signInSubmit']").click()
sleep(6)
driver.find_element(by=By.XPATH, value="//input[@aria-label='Search Amazon.in']").send_keys("shoes")
sleep(1)
driver.find_element(by=By.XPATH, value="//input[@id='nav-search-submit-button']").click()
sleep(1)

Reviews=driver.find_elements(by=By.XPATH, value="//span[@class='a-size-base s-underline-text']")
list=[]
for review in Reviews:
    list.append(review.text)
print("List of Reviews:",list)
print("Highest Reviews:",max(list))
high=max(list)

product_names=driver.find_elements(by=By.XPATH, value="//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']//span")
names=[]
for name in product_names:
    names.append(name.text)
print("List of product names:",names,end='')

Full_products_Details=driver.find_elements(by=By.XPATH, value="//div[@class='puis-card-container s-card-container s-overflow-hidden aok-relative puis-expand-height puis-include-content-margin puis puis-v1nyb4igz33igf2j9heq96r9jtz s-latency-cf-section puis-card-border']")
detail=[]
for details in Full_products_Details:
    detail.append(details.text)
print("All products full details:",detail)

index=0
while index<len(detail):
    if high in detail[index]:
        print("Details of Highest Reviewed Product:",detail[index],end="")
    print()
    index+=1








