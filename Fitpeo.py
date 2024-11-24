import os
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver import ActionChains, Keys
from time import sleep

try:
    option = Options()
    option.add_argument('--disable-notifications')
    # option.add_argument('--headless')
    # option.add_argument('--disable-gpu')
    option.add_experimental_option('detach', True)
    location = os.getcwd()
    preferences = {'download.default_directory': location, 'plugins.always_open_pdf_externally': True}
    driver = WebDriver(options=option)
    driver.get("https://www.fitpeo.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    sleep(1)
    driver.find_element("xpath", "//*[contains(text(),'Revenue Calculator')]").click()
    sleep(2)
    slider = driver.find_element('xpath', "//span[text()='Patients should be between 0 to 2000']")
    action = ActionChains(driver)
    action.scroll_to_element(slider).perform()
    sleep(2)
    source = driver.find_element('xpath', '//input[@aria-orientation="horizontal" and @type="range"]')
    sleep(1)
    # action.drag_and_drop_by_offset(source,94,0).perform()
    action.click_and_hold(source).move_by_offset(94, 0).release().perform()
    sleep(5)
    driver.refresh()
    sleep(3)
    driver.find_element("xpath", '//input[@type="number"]').clear()
    sleep(3)
    driver.find_element("xpath", '//input[@type="number"]').send_keys("560")
    sleep(2)
    check_element = driver.find_element('xpath', "//p[text()='CPT-99091']")
    action.scroll_to_element(check_element).perform()
    sleep(2)
    driver.find_element('xpath', '//p[text()="CPT-99091"]/..//*[@class="PrivateSwitchBase-input css-1m9pwf3"]').click()
    sleep(3)
    driver.find_element('xpath', '//p[text()="CPT-99453"]/..//*[@class="PrivateSwitchBase-input css-1m9pwf3"]').click()
    sleep(2)
    driver.find_element('xpath', '//p[text()="CPT-99454"]/..//*[@class="PrivateSwitchBase-input css-1m9pwf3"]').click()
    sleep(2)
    CPT = driver.find_element('xpath', '//p[text()="CPT-99474"]')
    action.scroll_to_element(CPT).perform()
    sleep(2)
    driver.find_element('xpath', '//p[text()="CPT-99474"]/..//*[@class="PrivateSwitchBase-input css-1m9pwf3"]').click()
    sleep(5)
    total = driver.find_element('xpath',
                                '//div[@class="MuiToolbar-root MuiToolbar-gutters MuiToolbar-regular css-1lnu3ao"]/p[4]/p').text
    print(total)

    driver.close()

except Exception as e:
    print(e, ' is an exception for source code')
finally:
    print('reports generated')
