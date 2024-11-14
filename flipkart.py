from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver import Keys, ActionChains




driver = WebDriver()
driver.get("https://www.flipkart.com/search?q=shoes&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
driver.implicitly_wait(10)
driver.maximize_window()
product_names = driver.find_elements('xpath', '//div[@class="hCKiGj"]//a[@class="WKTcLC"]')
for name in product_names:
    print(name.text)
