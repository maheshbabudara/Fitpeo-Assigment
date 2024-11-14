import pyodbc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select



serv_obj=Service("C:/Python_Selenium/Drivers/chromedriver-win64/chromedriver.exe")

driver= webdriver.Chrome(service=serv_obj)


driver.implicitly_wait(10)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()
time.sleep(8)


try:
    #DB:
    connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=my_database;UID=my_username;PWD=my_password"
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute("select * from caldata")  # data stored in cursor, becoz this select cmd will return data

    for row in cursor:
        #Reading Data from DB:
        price= row[0]
        rateofinterest= row[1]
        per1 = row[2]
        per2 = row[3]
        fre = row[4]
        exp_mvalue = row[5]

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

        else:
            print("Test case Failed")

        driver.find_element(by=By.XPATH, value='//*[@id="fdMatVal"]/div[2]/a[2]/img').click()
        time.sleep(3)
    cursor.close()  #not part of forloop
    connection.close() #not part of forloop
except Exception as e:
    print(e, 'is an issue')



driver.close()








