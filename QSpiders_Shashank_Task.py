from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as e
from time import sleep

def setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    return driver

my_driver = setup()
my_driver.implicitly_wait(10)
my_driver.get("https://demoapps.qspiders.com/ui/progress/element?sublist=2")
my_driver.maximize_window()

input = WebDriverWait(my_driver, 5).until(
    e.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter time in seconds']"))
)
input.send_keys("5")
start = WebDriverWait(my_driver, 5).until(
    e.visibility_of_element_located((By.XPATH, "//button[text()='Start']"))
)
start.click()
percent = WebDriverWait(my_driver, 10, poll_frequency=0.002).until(
    # e.presence_of_element_located((By.XPATH, "//span[text()='70%']"))
    e.presence_of_element_located((By.XPATH, "//div[@style='width: 69.6%;']"))
    #   e.presence_of_element_located((By.XPATH, "//div[@style='width: 70.4;']"))

)
print(percent.text)
Pause_btn = WebDriverWait(my_driver, 10,poll_frequency=0.001).until(
    e.presence_of_element_located((By.XPATH, "//button[text()='Pause']"))
)
Pause_btn.click()

#Below if condition consuming some amount of time, so Not prefered:
# if percent.text == '70%' or percent.text == '71%' :
#     Pause_btn=WebDriverWait(my_driver,10).until(
#         e.visibility_of_element_located((By.XPATH, "//button[text()='Pause']"))
#     )
#     Pause_btn.click()

sleep(20)
