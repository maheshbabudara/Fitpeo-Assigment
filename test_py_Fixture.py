import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from time import sleep
from selenium.webdriver import Keys, ActionChains

serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
@pytest.fixture(scope="module")
def init_driver():
    driver.get("https://demowebshop.tricentis.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()

    yield   #yeild will execute after the execrion of above intial setup code
    driver.quit()

#First approch of using Fxiture:
# def test_demo_title(init_driver):
#     assert driver.title=="Demo Web Shop"
# def test_demo_url(init_driver):
#     assert driver.current_url=="https://demowebshop/"

#Another way of using fixture:
@pytest.mark.usefixtures('init_driver')
def test_demo_title():
    assert  driver.title=="Demo Web Shop"

@pytest.mark.usefixtures('init_driver')
def test_demo_url():
    assert driver.current_url=="https://demowebshop.tricentis.com/"