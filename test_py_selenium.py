from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys, ActionChains
from time import sleep

serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
def test_instagram():
    driver.get("https://www.instagram.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    print(driver.title)
    assert driver.title=="Instagram"
    driver.close()

def test_fb():
    driver.get("https://www.facebook.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    print(driver.title)
    assert driver.title=='Facebook – log in or sign up'
    driver.close()

def test_youtube():
    driver.get("https://www.youtube.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    print(driver.title)
    assert  driver.title=="YouTube"
    driver.close()