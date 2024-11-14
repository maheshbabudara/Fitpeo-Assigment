from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service('C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe')

driver = webdriver.Chrome(service=serv_obj)

#Implicit wait cmd:
driver.implicitly_wait(10)  #seconds and implicit wait is applicable for all below lines of code where the synchronisation issue occurs
#As per industry implicit wait is '10' sec, if it is more than then log an peformance bug

driver.get('https://www.google.co.in/')
driver.maximize_window()

search_box = driver.find_element(by=By.XPATH, value='//*[@id="APjFqb"]')
search_box.send_keys('Selenium')
search_box.submit()
# driver.find_element(by=By.XPATH, value='//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3').click()
driver.find_element(by=By.XPATH, value='//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3').click()

driver.quit()
