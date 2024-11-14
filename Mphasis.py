# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.chrome.options import Options
# from time import sleep
#
# driver = WebDriver()
# option = Options()
# driver.get("https://www.amazon.in/")
# driver.implicitly_wait(10)
# driver.maximize_window()
# time.sleep(3)
#
# # CSS SELECTOR:
# # syntax:Tagname#id
# # syntax:Tagname.classname
# # syntax:Tagname[attribute='value']
# # using index in css selector:
# # syntax:div p:nth-child(index)     or we can use another--> div p:nth-of-type(index)
# driver.find_element("css selector", 'a[data-csa-c-slot-id="nav_cs_0"]').click()  # tagname[attribute='value]
# time.sleep(5)
# driver.back()
# time.sleep(2)
# driver.find_element('css selector', 'span#nav-global-location-data-modal-action').click()  # Tagname#idvalue
# time.sleep(5)
# driver.back()
# time.sleep(2)
# driver.find_element('css selector', 'div.nav-line-1-container').click()  # Tagname.classvalue
# time.sleep(4)
# driver.close()





#chatgpt code:
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from time import sleep

# Set up Chrome options
option = Options()
option.add_argument('--disable-notifications')

# Initialize the WebDriver
driver = webdriver.Chrome(options=option)

# Open the URL
driver.get("http://3.7.121.249:8080/maioraSSO/#/")

# Implicit wait
driver.implicitly_wait(15)

# Maximize the window
driver.maximize_window()

# Login process
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Email Id"]'))).send_keys("kowshikshaiva121@gmail.com")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Password"]'))).send_keys("Kowshik@123")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Log In')]"))).click()

# Navigate to Datastore
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(@src,"amazonaws.com/website/NewImages26082022/DO_IT_RIGHT_Logo")]'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Datastore')]"))).click()

# Add Datastore
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@ng-reflect-specific-title="Add Datastore"]'))).click()

# Search for SQL and select it
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Search"]'))).send_keys("SQL")
sql_element = WebDriverWait(driver, 10, poll_frequency=0.3).until(
    EC.presence_of_element_located((By.XPATH, '//img[contains(@src,"assets/newImages/SQL.png") and @style="border-radius: 4px; height: 120px; width: 110px; border: 3px solid red;"]'))
)
sql_element.click()

# Click Next button after selecting SQL
# action=ActionChains(driver)
element=driver.find_element('xpath','//div[@class="ant-drawer-body" and @style="overflow: hidden scroll; max-height: 650px;"]/div[@id="Bottom"]/button/span[@class="ng-star-inserted"]')
# action.scroll_to_element(element)
# sleep(5)
# WebDriverWait(driver, 10,poll_frequency=0.5).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="ant-drawer-body" and @style="overflow: hidden scroll; max-height: 650px;"]/div[@id="Bottom"]/button/span[@class="ng-star-inserted"]'))).click()

#JS CLICK"
driver.execute_script("arguments[0].click();",element)

# Fill in Datastore configuration details
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Title"]'))).send_keys('MY SQL Settings config')
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//textarea[@placeholder="Description"]'))).send_keys('This is all about MYSQL Settings config ')
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@title="Host"]'))).send_keys("43.204.212.240")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@title="Port"]'))).send_keys("3306")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@title="Database"]'))).send_keys("zarus_load_testing")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Username"]'))).send_keys("loadtesting_user")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@title="Password"]'))).send_keys("Ext_User@2024")

# Test connection and Save
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Test')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='Bottom']//span[contains(text(),'Save ')]"))).click()

# Wait and navigate back
sleep(8)
driver.back()

# Open Scheduler and configure
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//li[@ng-reflect-specific-title="Scheduler"]/..'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="ant-btn-primary ant-btn"]'))).click()

# Fill Scheduler details
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Schedule Name"]'))).send_keys("Testing")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@ng-reflect-placeholder="Job Name"]'))).send_keys('farheen-source2')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='farheen-source2']"))).click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[text()=' Description ']//input"))).send_keys("Testing scheduler")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@class="ng-tns-c147-31"]'))).send_keys("2024-11-12")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@class="ng-tns-c147-32"]'))).send_keys("2024-11-14")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Select time"]'))).send_keys("12:02")

# Save Scheduler
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Save')]"))).click()

# Close the browser
sleep(5)
driver.quit()