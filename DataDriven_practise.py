# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
# import openpyxl
# from selenium.webdriver.support.select import Select
#
# import XLUtils_practise
#
# def setup():
#     from selenium.webdriver.chrome.service import Service
#     serv_obj = Service("C:/Python_Selenium/Drivers/chromedriver-win64/chromedriver.exe")
#     driver = webdriver.Chrome(service=serv_obj)
#     return driver
#
#
# my_driver = setup()
# my_driver.implicitly_wait(10)
# my_driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
# my_driver.maximize_window()
#
# #Read data from Excel sheet:
# file = ("C:\Python_Selenium\Selenium\PythonSelenium\Testdata1.xlsx")
# rows=XLUtils_practise.getrowcount(file,'Det')
#
# for r in range(2,rows+1):
#     #Redaing form each cell of Excel sheet:
#     principal=XLUtils_practise.readdata(file,"Det",r,1)
#     rate=XLUtils_practise.readdata(file,"Det",r,2)
#     per1=XLUtils_practise.readdata(file,"Det",r,3)
#     per2=XLUtils_practise.readdata(file,"Det",r,4)
#     freq=XLUtils_practise.readdata(file,"Det",r,5)
#     Exp_valu=XLUtils_practise.readdata(file,"Det",r,6)
#
#     my_driver.find_element(by=By.XPATH, value='//*[@id="principal"]').send_keys(principal)
#     my_driver.find_element(by=By.XPATH, value='/html/body/div[10]/div[2]/div/div[5]/div/div[1]/div[3]/form/div[1]/div[4]/input').send_keys(rate)
#     my_driver.find_element(by=By.XPATH, value='//*[@id="tenure"]').send_keys(per1)
#     drp=Select(my_driver.find_element(by=By.XPATH, value='//*[@id="tenurePeriod"]'))
#     drp.select_by_visible_text(per2)
#     freq_drp=Select(my_driver.find_element(by=By.XPATH, value='//*[@id="frequency"]'))
#     freq_drp.select_by_visible_text(freq)
#     my_driver.find_element(by=By.XPATH, value="//img[@src='https://images.moneycontrol.com/images/mf_revamp/btn_calcutate.gif']").click()
#
#     result=my_driver.find_element(by=By.XPATH, value='//*[@id="resp_matval"]/strong').text
#
#     if float(Exp_valu)==float(result):
#         print('Test case passed')
#         XLUtils_practise.writedata(file,"Det",r,7,"Pass")
#         XLUtils_practise.greencolor(file,"Det",r,7)
#     else:
#         print("Test case Failed")
#         XLUtils_practise.writedata(file,'Det',r,7,"Fail")
#         XLUtils_practise.redcolor(file,'Det',r,7)
#     my_driver.find_element(by=By.XPATH, value='//*[@id="fdMatVal"]/div[2]/a[2]/img').click()
#     sleep(2)
#
# my_driver.close()
#

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys, ActionChains
from time import sleep
import XLUtils_practise

serv_obj=Service("C:/Python_Selenium/Drivers/chromedriver-win64/chromedriver.exe")
option=webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
option.add_argument("--disable-Notifications")
# option.add_argument("--headless")
driver=webdriver.Chrome(service=serv_obj,options=option)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.implicitly_wait(10)
driver.maximize_window()

#read_data:
file = ("C:\Python_Selenium\Selenium\PythonSelenium\Testdata1.xlsx")
rows=XLUtils_practise.rowcount('Det',file)

for row in range(2,rows+1):
    princ=XLUtils_practise.readdata('Det',file,row,1)
    intr=XLUtils_practise.readdata('Det',file,row,2)
    per1=XLUtils_practise.readdata('Det',file,row,3)
    per2=XLUtils_practise.readdata('Det',file,row,4)
    freq=XLUtils_practise.readdata('Det',file,row,5)
    Exp_val=XLUtils_practise.readdata('Det',file,row,6)

    P=WebDriverWait(driver,15).until(
        e.presence_of_element_located((By.XPATH,"//input[@name='principal']"))
    )
    P.send_keys(princ)
    driver.find_element(by=By.XPATH,value="//input[@name='interest']").send_keys(intr)
    driver.find_element(by=By.XPATH, value="//input[@name='tenure']").send_keys(per1)
    driver.find_element(by=By.XPATH,value="//select[@name='tenurePeriod']").send_keys(per2)
    driver.find_element(by=By.XPATH,value="//select[@name='frequency']").send_keys(freq)
    driver.find_element(by=By.XPATH,value="//img[contains(@src,'btn_calcutate.gif')]").click()
    sleep(1)
    Actula_vl=driver.find_element(by=By.XPATH,value="//span[@name='resp_matval']").text

    if float(Actula_vl)==float(Exp_val):
        XLUtils_practise.writedata('Det',file,row,7,"Pass")
        XLUtils_practise.greenfill('Det',file,row,7)
        print('Test Case Pass')
    else:
        XLUtils_practise.writedata('Det',file,row,7,"FAIL")
        XLUtils_practise.redfill('Det', file, row, 7)
        print('Test case Fail')
    driver.find_element(by=By.XPATH,value="//img[contains(@src,'btn_clear.gif')]").click()
    sleep(1)
driver.close()







