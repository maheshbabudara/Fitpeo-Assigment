from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys, ActionChains
from time import sleep
import pytest

serv_obj = Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
def setup_module(module):
    global driver
    driver.get("https://demowebshop.tricentis.com/")
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.maximize_window()

def teardown_module(module):
    driver.quit()

def test_demo_title():
    assert driver.title=="Demo Web Shop"

def test_demo_url():
    assert  driver.current_url=="https://demowebshop.tricentis.com/"

