# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from time import sleep
#
# def setupp():
#     serv_obj=Service("C:/Python_Selenium/Drivers/chromedriver-win64/chromedriver.exe")
#     ops=webdriver.ChromeOptions()
#     ops.add_argument('--headless')
#     ops.add_argument('--disable-gpu')
#     driver=webdriver.Chrome(service=serv_obj,options=ops)
#     return driver
# my_driver=setupp()
# my_driver.implicitly_wait(10)
# my_driver.get("https://testautomationpractice.blogspot.com/")
# my_driver.maximize_window()
# my_driver.find_element(by=By.XPATH, value="//button[text()='Prompt']").click()
# sleep(1)
# alt=my_driver.switch_to.alert
# alt.send_keys("mahesh babu")
# sleep(1)
# alt.accept()
# sleep(1)
# print(my_driver.find_element(by=By.ID, value='demo').text)
# print("Operation occomplished")
# sleep(1)
# my_driver.close()

#Wync Muisc Task:
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains, Keys
from time import sleep


obj=Service("C:/Python_Selenium/Drivers/chromedriver-win64/chromedriver.exe")
option=webdriver.ChromeOptions()
option.add_argument("--disable-Notifications")
option.add_experimental_option("detach", True)
option.add_argument("--headless")
option.add_argument("--disable-gpu")

driver=webdriver.Chrome(service=obj,options=option)
driver.get("https://wynk.in/music/album/murari/am_A10400DAMTEFA0991Y?q=mur")
driver.maximize_window()
driver.implicitly_wait(10)

Bangaru_kalla=WebDriverWait(driver, 10).until(
    e.visibility_of_element_located((By.XPATH, "//a[text()='Bangaru Kalla']"))
)
Bangaru_kalla.click()
sleep(80)

driver.close()


