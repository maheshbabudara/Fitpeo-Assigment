# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.chrome.service import Service
#
# serv_obj= Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
# ops= webdriver.ChromeOptions()
# ops.add_experimental_option("detach", True)
# driver=webdriver.Chrome()
# driver.get("https://demowebshop.tricentis.com/")
#
# driver.maximize_window()
# print(driver.name)
# time.sleep(2)
# print(driver.title)
# time.sleep(3)
# print(driver.current_url)
# driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

serv_obj = Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.google.com/search?q=mahesh+babu&sca_esv=7b0e25503c647052&sca_upv=1&hl=en&source=hp&ei=86B-ZuecLoTm2roPgcq7mA0&iflsig=AL9hbdgAAAAAZn6vA4_Vmm1Knrg_hiMX7qC1ZJyHBiFL&ved=0ahUKEwin4r2bm_6GAxUEs1YBHQHlDtMQ4dUDCA0&uact=5&oq=mahesh+babu&gs_lp=Egdnd3Mtd2l6IgttYWhlc2ggYmFidTIOEC4YgAQYsQMYgwEYyQMyEBAAGIAEGLEDGIMBGIoFGAoyERAuGIAEGLEDGIMBGNQCGIoFMgoQABiABBhDGIoFMgsQABiABBixAxiDATILEC4YgAQYsQMYgwEyCBAAGIAEGLEDMg4QLhiABBixAxiDARjUAjILEAAYgAQYkgMYigUyCxAAGIAEGJIDGIoFSKUOUABY_wtwAHgAkAEAmAH6AqABkAeqAQUyLTIuMbgBA8gBAPgBAZgCA6ACrQfCAgUQLhiABMICERAuGIAEGLEDGNEDGIMBGMcBwgIOEC4YgAQYsQMYgwEYigXCAgoQLhiABBhDGIoFwgIQEAAYgAQYsQMYQxiDARiKBcICFhAuGIAEGLEDGNEDGEMYgwEYxwEYigWYAwCSBwUyLTIuMaAH_iM&sclient=gws-wiz")
driver.maximize_window()
print(driver.title)
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)


driver.refresh()
driver.close()


