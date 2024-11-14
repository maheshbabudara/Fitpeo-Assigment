from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import pytest
# serv_obj=Service("C:/Python_Selenium/Drivers/chromedriver-win64/chromedriver.exe")
# driver=webdriver.Chrome(service=serv_obj)
@pytest.fixture(scope='class')
def init_chrome_driver(request):
    serv_obj = Service("C:/Python_Selenium/Drivers/chromedriver-win64/chromedriver.exe")
    google_driver = webdriver.Chrome(service=serv_obj)
    request.cls.driver=google_driver

    yield
    google_driver.close()

@pytest.mark.usefixtures('init_chrome_driver')
class Base_fixture_chrome:
    pass