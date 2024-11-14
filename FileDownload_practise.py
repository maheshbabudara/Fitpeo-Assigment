# import os
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from time import sleep
# location=os.getcwd()
#
# serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
# preferences= {"download.default_directory":location,"plugins.always_open_pdf_externally":True}
# ops=webdriver.ChromeOptions()
# ops.add_experimental_option('prefs',preferences)
# driver=webdriver.Chrome(service=serv_obj)
# # driver.get("https://freetestdata.com/document-files/pdf/")
# # driver.maximize_window()
# #
# # driver.find_element(by=By.XPATH, value='//*[@id="post-81"]/div/div/section[3]/div/div[1]/div/section[3]/div/div[2]/div/div/div/div/a').click()
# # print("Place of download:",location)
# # sleep(3)
# #
# # driver.close()
#
#
#
#
# #Dowload word file:
# driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
# driver.maximize_window()
# driver.find_element(by=By.XPATH, value='//*[@id="table-files"]/tbody/tr[3]/td[5]/a').click()
# print("Place of download:",location)
# sleep(3)


#Assignment Task:
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver import ActionChains, Keys
from time import sleep
location=os.getcwd()
serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
preferences={"download.default_directory": location, "plugins.always_open_pdf_externally":True}
option=webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
option.add_experimental_option("prefs", preferences)
option.add_argument("--disable-Notifications")

driver=webdriver.Chrome(service=serv_obj, options=option)
driver.get("https://onlinetestcase.com/pdf-file/")
driver.maximize_window()
driver.implicitly_wait(10)

#500kb:
# driver.find_element(by=By.XPATH, value="//h2[text()='Download 500 KB PDF File']").click()
# sleep(5)

#1.5mb:
element=WebDriverWait(driver,10).until(
    e.presence_of_element_located((By.XPATH, "//h2[text()='Download 1.5 MB PDF File']"))
)
element.click()
sleep(5)
driver.close()
