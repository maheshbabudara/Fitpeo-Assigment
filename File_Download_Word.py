from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
location=os.getcwd()   #will return current working directory

#Google Chrome browser file download:
def setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")

  #download fiels in desired locations:
    preferences={"download.default_directory":location}
    ops=webdriver.ChromeOptions()
    ops.add_experimental_option('prefs',preferences)  #creating an location for downloading files

    driver=webdriver.Chrome(service=serv_obj, options=ops)
    return driver


#Microsft Edge broswer file download:
def edge_setup():
    from selenium.webdriver.edge.service import Service
    serv_obj=Service("C:\Python_Selenium\Drivers\edgedriver_win64\msedgedriver.exe")
    preferences= {"download.default_directory":location}
    ops=webdriver.EdgeOptions()
    ops.add_experimental_option("prefs",preferences)
    driver=webdriver.Edge(service=serv_obj)
    driver.start_session(options=ops.to_capabilities())
    return driver

#Firefox broswer file download:
def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    serv_obj=Service("C:\Python_Selenium\Drivers\geckodriver-v0.34.0-win-aarch64\geckodriver.exe")  #Firefox webdriver paths
    #Settings:
    ops=webdriver.FirefoxOptions()
    ops.set_preference("browser.download.folderList", 2)   #0-will dowload in DeskTop, 1-will download in Downloads, 2- will download at desiredlocation
    ops.set_preference("browser.download.dir", location)
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/msword")  #application/msword is an MIME type to download files, for various files we can have variosu mime types ex: application/txt,application/excel etc
    #websire for MIME types-https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    driver=webdriver.Firefox(service=serv_obj,options=ops)
    return driver


my_driver=setup() #calling function
# my_driver=edge_setup()  #Calling function for Microsoft Edge
# my_driver=firefox_setup()   #Calling function for FireFox

my_driver.implicitly_wait(10)
my_driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/") #launching apllication
my_driver.maximize_window()

time.sleep(2)
my_driver.find_element(by=By.XPATH, value='//*[@id="table-files"]/tbody/tr[2]/td[5]/a').click()
time.sleep(3)
print('downloaded file here:',location)



