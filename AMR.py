import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from time import sleep

try:
    #SETUP:
    driver = WebDriver()
    option = Options()
    option.add_argument('--disable-notifications')
    driver.get("http://3.7.121.249:8080/maioraSSO/#/")
    driver.implicitly_wait(15)
    driver.maximize_window()
    sleep(2)

    #LOGIN WEB APP:
    driver.find_element('xpath', '//input[@placeholder="Email Id"]').send_keys("kowshikshaiva121@gmail.com")
    sleep(2)
    driver.find_element("xpath", '//input[@placeholder="Password"]').send_keys("Kowshik@123")
    sleep(2)
    driver.find_element('xpath', "//span[contains(text(),'Log In')]").click()
    sleep(2)

    #DASHBOARD:
    driver.find_element('xpath','//*[contains(@src,"amazonaws.com/website/NewImages26082022/DO_IT_RIGHT_Logo")]').click()
    sleep(2)
    driver.find_element('xpath', "//span[contains(text(),'Datastore')]").click()
    sleep(5)

    #DATASTORE;
    driver.find_element('xpath', '//button[@ng-reflect-specific-title="Add Datastore"]').click()
    sleep(3)
    WebDriverWait(driver, 10, poll_frequency=0.4).until(
        e.presence_of_element_located(("xpath", '//input[@placeholder="Search"]'))
    ).send_keys("SQL")
    sleep(3)
    sql = WebDriverWait(driver, 10, poll_frequency=0.3).until(
        e.presence_of_element_located(('xpath',
                                       '//img[contains(@src,"assets/newImages/SQL.png") and @style="border-radius: 4px; height: 120px; width: 110px; border: 3px solid red;"]')))
    sql.click()
    sleep(5)

    # Next=WebDriverWait(driver,10).until(
    #     e.visibility_of_element_located(('xpath','//div[@class="ant-drawer-body" and @style="overflow: hidden scroll; max-height: 650px;"]/div[@id="Bottom"]/button/span'))
    # )
    # Next.click()


    element = driver.find_element('xpath',
                                  '//div[@class="ant-drawer-body" and @style="overflow: hidden scroll; max-height: 650px;"]/div[@id="Bottom"]/button/span[@class="ng-star-inserted"]')
    driver.execute_script("arguments[0].click();", element)
    sleep(2)

    #CHOOSING DATBASE:
    # Database=WebDriverWait(driver,20,poll_frequency=0.1).until(
    #     e.presence_of_element_located(('xpath','//*[@id="cdk-overlay-3"]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div[1]/nz-select[@nzplaceholder="Select Datastore"]/*[@ng-reflect-place-holder="Select Datastore"]'))
    #
    # )
    # driver.execute_script('arguments[0].click();',Database)
    # sleep(2)
    # WebDriverWait(driver,10,poll_frequency=0.2).until(
    #     e.presence_of_element_located(('xpath','//*[@id="cdk-overlay-3"]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div[1]/nz-select[@nzplaceholder="Select Datastore"]/*[@ng-reflect-place-holder="Select Datastore"]'))
    # ).send_keys("Selenium using java project 3")
    # sleep(3)
    # WebDriverWait(driver,10,poll_frequency=0.4).until(e.visibility_of_element_located(('xpath','//div[@class="ant-select-item-option-content"]'))).click()
    # sleep(3)


    #ENTERING DB DETAILS :
    try:
        # driver.find_element('xpath', "//div[normalize-space()='Selenium using java project 3']").click()
        # sleep(2)
        WebDriverWait(driver, 10, poll_frequency=0.5).until(
            e.visibility_of_element_located(
                ('xpath', '//*[@id="cdk-overlay-3"]//input[@placeholder="Title"]'))).send_keys(
            "MY SQL Settings config")
        sleep(3)
        WebDriverWait(driver, 10, poll_frequency=0.3).until(e.presence_of_element_located(
            ('xpath', '//*[@id="cdk-overlay-3"]//textarea[@placeholder="Description"]'))).send_keys(
            "This is all about MYSQL Settings config ")
        sleep(2)
    except Exception as error:
        print(error)
    else:
        driver.find_element('xpath', '//div[@id="cdk-overlay-3"]//input[@placeholder="Host"]').send_keys(
            "43.204.212.240")
        sleep(1)
        driver.find_element("xpath", '//div[@id="cdk-overlay-3"]//input[@placeholder="Port"]').send_keys("3306")
        sleep(1)
        driver.find_element("xpath", '//div[@id="cdk-overlay-3"]//input[@placeholder="Database"]').send_keys(
            "zarus_load_testing")
        sleep(1)
        driver.find_element("xpath", '//div[@id="cdk-overlay-3"]//input[@placeholder="Username"]').send_keys(
            "loadtesting_user")
        sleep(1)
        driver.find_element('xpath', '//div[@id="cdk-overlay-3"]//input[@placeholder="Password"]').send_keys(
            "Ext_User@2024")
        sleep(1)
        Test = WebDriverWait(driver, 10, poll_frequency=0.2).until(
            e.visibility_of_element_located(('xpath', "//div[@id='cdk-overlay-3']//button[2]/span")))
        driver.execute_script("arguments[0].click();", Test)
        sleep(2)
        # driver.find_element('xpath', "//div[@id='Bottom']//span[contains(text(),'Save ')]").click()

    sleep(5)
    #NAVIGATING TO DASHBOARD:
    driver.back()
    sleep(3)

     #SCHEDULER OPERATIONS: TASK2:
    driver.find_element('xpath', '//li[@ng-reflect-specific-title="Scheduler"]/..').click()
    sleep(2)
    driver.find_element('xpath', '//button[@class="ant-btn-primary ant-btn"]').click()
    sleep(1)
    driver.find_element('xpath', '//input[@placeholder="Schedule Name"]').send_keys("Testing")
    sleep(2)

    # driver.find_element('xpath', '//*[@ng-reflect-placeholder="Job Name"]').click()
    # sleep(2)
    # driver.find_element('xpath','//*[@ng-reflect-placeholder="Job Name"]').send_keys("farheen")
    # sleep(3)
    # Jobnames=driver.find_elements('xpath','//div[@class="cdk-virtual-scroll-content-wrapper"]')
    # for name in Jobnames:
    #     if name.text=="farheen-source2":
    #         name.click()
    #         break
    # value = driver.find_element('xpath', "//div[normalize-space()='farheen-source2']").is_displayed()
    # if value == True:
    #     driver.execute_script("arguments[0].click();", value)



    sleep(2)
    driver.find_element('xpath', "//div[text()=' Description ']//input").send_keys("Testing scheduler")
    sleep(2)
    WebDriverWait(driver, 10, poll_frequency=0.3).until(
        e.visibility_of_element_located(('xpath',
                                         '//div[@class="formInput-container" and text()=" Start Date "]//div[@ng-reflect-placeholder="Select date"]'))
    ).click()
    sleep(2)
    year = '2024'
    month = 'Nov'
    date = '12'
    while True:
        y = driver.find_element('xpath', '//button[@title="Choose a year"]').text
        m = driver.find_element('xpath', '//button[@title="Choose a month"]').text
        if y == year and m == month:
            break
        else:
            driver.find_element('xpath', '//button[@title="Next month (PageDown)"]').click()
            driver.find_element('xpath', '//button[@title="Next year (Control + right)"]').click()
    Dates = driver.find_elements('xpath', '//div[@class="ant-picker-body ng-star-inserted"]//tr/td/div')
    for d in Dates:
        if d.text == date:
            d.click()
            break

    WebDriverWait(driver, 10, poll_frequency=0.3).until(
        e.presence_of_element_located(
            ('xpath', '//div[@class="formInput-container" and text()=" End Date "]//input[@placeholder="Select date"]'))
    ).click()
    E_year = '2024'
    E_month = 'Nov'
    E_date = '14'
    while True:
        y_E = driver.find_element('xpath', '//button[@title="Choose a year"]').text
        m_E = driver.find_element('xpath', '//button[@title="Choose a month"]').text
        if y_E == E_year and m_E == E_month:
            break
        else:
            driver.find_element('xpath', '//button[@title="Next month (PageDown)"]').click()
            driver.find_element('xpath', '//button[@title="Next year (Control + right)"]').click()
    E_Dates = driver.find_elements('xpath', '//div[@class="ant-picker-body ng-star-inserted"]//tr/td/div')
    for dam in E_Dates:
        if dam.text == E_date:
            dam.click()
            break
    #ENTERING DATES WITH SEND_KEYS():
    # WebDriverWait(driver,10,poll_frequency=0.3).until(
    #     e.presence_of_element_located(('xpath','//*[@id="cdk-overlay-5"]//input[@placeholder="Select date" and @class="ng-tns-c147-31 ng-pristine ng-valid ng-touched"]'))
    # ).send_keys("2024-11-12")
    # sleep(2)
    # WebDriverWait(driver,10,poll_frequency=0.3).until(
    #     e.presence_of_element_located(('xpath','//*[@id="cdk-overlay-5"]//input[@placeholder="Select date" and @class="ng-tns-c147-32 ng-untouched ng-pristine ng-valid"]'))
    # ).send_keys("2024-11-14")
    # sleep(2)
    driver.find_element('xpath', '//input[@placeholder="Select time"]').send_keys("12:02")
    sleep(2)
    save = driver.find_element('xpath', "//button[@class='ant-btn-primary ant-btn ng-star-inserted']/span")
    driver.execute_script("arguments[0].click();", save)
    sleep(5)
    driver.close()

except Exception as error:
    print(error)
finally:
    print('Reports Generated and EXECUTION Completed')


