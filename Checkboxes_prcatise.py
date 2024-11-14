# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# def setup():
#     from selenium.webdriver.chrome.service import Service
#     serv_obj = Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
#     driver = webdriver.Chrome(service=serv_obj)
#     return driver
#
#
# my_driver = setup()
# my_driver.implicitly_wait(10)
# my_driver.get("https://testautomationpractice.blogspot.com/")
# my_driver.maximize_window()

#select specific check box:
# my_driver.find_element(by=By.XPATH, value='//*[@id="productTable"]/tbody/tr[3]/td[4]/input').click()
# time.sleep(3)

# my_driver.find_element(by=By.XPATH, value='//*[@id="pagination"]/li[2]/a').click()
# time.sleep(1)
# my_driver.find_element(by=By.XPATH, value='//*[@id="pagination"]/li[3]/a').click()
# time.sleep(1)
# my_driver.find_element(by=By.XPATH, value='//*[@id="productTable"]/tbody/tr[5]/td[4]/input').click()

#select All checkboxes:
# checkboxes=my_driver.find_elements(by=By.XPATH, value='//*[@id="productTable"]/tbody/tr/td[4]/input')
# for c in checkboxes:
#     c.click()
# time.sleep(3)


#Moving to  3rd page:
# my_driver.find_element(by=By.XPATH, value='//*[@id="pagination"]/li[2]/a').click()
# time.sleep(1)
# my_driver.find_element(by=By.XPATH, value='//*[@id="pagination"]/li[3]/a').click()
# time.sleep(1)
# boxes=my_driver.find_elements(by=By.XPATH, value='//*[@id="productTable"]/tbody/tr/td[4]/input')
# for b in boxes:
#     b.click()
#     time.sleep(1)

#select few checboxes by choice:
# checkbox_few = my_driver.find_elements(by=By.XPATH, value='//*[@id="productTable"]/tbody/tr/td[4]/input')
#
# Name = my_driver.find_elements(by=By.XPATH, value='//*[@id="productTable"]/tbody/tr/td[2]')
#
# rows = my_driver.find_elements(by=By.XPATH, value='//*[@id="productTable"]/tbody/tr')
#
# for row in rows:
#     product_name = row.find_element(by=By.XPATH, value='./td[2]').text
#     if product_name == "Product 3" or product_name == "Product 4":
#         row.find_element(by=By.XPATH, value='./td[4]/input').click()
#

#Moving to  3rd page:
# my_driver.find_element(by=By.XPATH, value='//*[@id="pagination"]/li[2]/a').click()
# time.sleep(1)
# my_driver.find_element(by=By.XPATH, value='//*[@id="pagination"]/li[3]/a').click()
# time.sleep(1)
# rows=my_driver.find_elements(by=By.XPATH, value='//*[@id="productTable"]/tbody/tr')
#
# for row in rows:
#     product_name= row.find_element(by=By.XPATH, value='./td[2]').text
#     if product_name== "Product 13" or product_name=="Product 15":
#         row.find_element(by=By.XPATH, value='./td[4]/input').click()

#select last 3 checboxes :
# checkbox_few=my_driver.find_elements(by=By.XPATH, value='//*[@id="productTable"]/tbody/tr/td[4]/input')
# rows=my_driver.find_elements(by=By.XPATH, value='//*[@id="productTable"]/tbody/tr')
#
# for r in range(len(checkbox_few)-3,len(checkbox_few)):
#     checkbox_few[r].click()

#Moving to  3rd page:
# my_driver.find_element(by=By.XPATH, value='//*[@id="pagination"]/li[2]/a').click()
# time.sleep(1)
# my_driver.find_element(by=By.XPATH, value='//*[@id="pagination"]/li[3]/a').click()
# time.sleep(1)
# checkboxes=my_driver.find_elements(by=By.XPATH, value='//*[@id="productTable"]/tbody/tr/td[4]/input')
# for c in range(len(checkboxes)-3, len(checkboxes)):
#     checkboxes[c].click()



#select first 2 checkboxes:
# checkbox_few = my_driver.find_elements(by=By.XPATH, value='//*[@id="productTable"]/tbody/tr/td[4]/input')
# for c in range(len(checkbox_few)):
#     if c <= 1:
#         checkbox_few[c].click()

# time.sleep(5)
# my_driver.close()





