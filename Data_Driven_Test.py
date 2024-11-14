from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

import XLUtils

serv_obj=Service("C:/Python_Selenium/Drivers/chromedriver-win64/chromedriver.exe")

driver= webdriver.Chrome(service=serv_obj)


driver.implicitly_wait(10)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()
time.sleep(8)

file=("C:\Python_Selenium\Selenium\PythonSelenium\Testdata1.xlsx")
rows=XLUtils.getRowCount(file,'Det')

for r in range(2,rows+1):
    #Reading Data from Excel sheet:
    price=XLUtils.readData(file,'Det',r,1)
    rateofinterest=XLUtils.readData(file,'Det',r,2)
    per1 = XLUtils.readData(file, 'Det', r, 3)
    per2 = XLUtils.readData(file, 'Det', r, 4)
    fre = XLUtils.readData(file, 'Det', r, 5)
    exp_mvalue = XLUtils.readData(file, 'Det', r, 6)


    #passing data into web application:
    driver.find_element(by=By.XPATH, value='//*[@id="principal"]').send_keys(price)
    driver.find_element(by=By.XPATH, value='//*[@id="interest"]').send_keys(rateofinterest)
    driver.find_element(by=By.XPATH, value='//*[@id="tenure"]').send_keys(per1)

    perioddrp=Select(driver.find_element(by=By.XPATH, value='//*[@id="tenurePeriod"]'))
    perioddrp.select_by_visible_text(per2)

    frequencydrp=Select(driver.find_element(by=By.XPATH, value='//*[@id="frequency"]'))
    frequencydrp.select_by_visible_text(fre)

    driver.find_element(by=By.XPATH, value='//*[@id="fdMatVal"]/div[2]/a[1]').click()


    act_mvalue= driver.find_element(by=By.XPATH, value='//span[@id="resp_matval"]/strong').text

    #Validation:
    if float(exp_mvalue)==float(act_mvalue):
        print("Test case Passed")
        XLUtils.writeData(file,'Det',r,7,'Pass')
        XLUtils.fillGreenColor(file,'Det',r,7)
    else:
        print("Test case Failed")
        XLUtils.writeData(file,'Det',r,7,'Fail')
        XLUtils.fillRedColor(file,'Det',r,7)
    driver.find_element(by=By.XPATH, value='//*[@id="fdMatVal"]/div[2]/a[2]/img').click()
    time.sleep(3)

driver.close()








