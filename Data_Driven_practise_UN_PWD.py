from selenium import webdriver
from time import sleep
import XLUtils_UN_PWD
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


def setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj=Service("C:/Python_Selenium/Drivers/chromedriver-win64/chromedriver.exe")
    driver=webdriver.Chrome(service=serv_obj)
    return  driver

my_driver=setup()
my_driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
my_driver.maximize_window()

#Reading data from XLUtils file:
file=("C:\Python_Selenium\Selenium\PythonSelenium\WiteData_practise.xlsx")
rows= XLUtils_UN_PWD.getrow(file,"Sheet1")

for r in range(3,rows+1):
    UN = XLUtils_UN_PWD.readata(file, "Sheet1", r, 1)
    pwd= XLUtils_UN_PWD.readata(file,"Sheet1",r,2)

    username=WebDriverWait(my_driver,10).until(
        ec.presence_of_element_located((By.XPATH, "//input[@name='username']"))
    )
    username.clear()
    username.send_keys(UN)
    sleep(1)
    password=WebDriverWait(my_driver,10).until(
        ec.presence_of_element_located((By.XPATH, "//input[@name='password']"))
    )
    password.clear()
    password.send_keys(pwd)
    sleep(1)
    login_btn=WebDriverWait(my_driver,10).until(
        ec.element_to_be_clickable((By.XPATH, "//button[text()=' Login ']"))
    )
    login_btn.click()
    sleep(3)
    if "dashboard" in my_driver.current_url:
        print("Testcase Passed")
        XLUtils_UN_PWD.writedata(file,"Sheet1",r,3,"Pass")
        XLUtils_UN_PWD.fillGreenColor(file,"Sheet1",r,3)

        my_driver.find_element(by=By.XPATH,value="//p[@class='oxd-userdropdown-name']").click()
        sleep(1)
        logout = WebDriverWait(my_driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "// a[text() = 'Logout']"))
        )
        logout.click()
        sleep(1)
    elif my_driver.find_element(by=By.XPATH, value="//p[text()='Invalid credentials']").text=="Invalid credentials":
        print("Testcase Failed")
        XLUtils_UN_PWD.writedata(file, "Sheet1", r, 3, "Fail")
        XLUtils_UN_PWD.fillRedColor(file, "Sheet1", r, 3)









