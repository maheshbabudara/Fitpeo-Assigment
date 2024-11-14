from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj= Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.implicitly_wait(10)
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.maximize_window()
#
# #1.window ID of current window:
# # print(driver.current_window_handle)
#
# driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a').click()  #click link in 1st page
#
# #2.window ID of Multiple windows:
# Window_IDs=driver.window_handles   #returns List
# # Parent_window=Window_IDs[0]
# # Child_Window=Window_IDs[1]
# # # print("Parent window ID:",Window_IDs[0],"Child Window ID:", Window_IDs[1])
# #
# # driver.switch_to.window(Child_Window)
# # print('Title of Child window:',driver.title)
# #
# # driver.switch_to.window(Parent_window)
# # print('Title of Parent window:',driver.title)
# # time.sleep(4)
# # driver.quit()
#
# #Aproach with Loops:
# for i in Window_IDs:
#     driver.switch_to.window(i)
#     print(driver.title)
#
#     #Can perform close operations or other operations based on Title of window:
#     if driver.title=="OrangeHRM" or driver.title=="facebook":
#         driver.close()




#Assignment Task: important
driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element(by=By.XPATH, value="//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("selenium")
time.sleep(1)
driver.find_element(by=By.XPATH, value="//input[@class='wikipedia-search-button']").click()
time.sleep(1)
driver.find_element(by=By.XPATH, value="//a[text()='Selenium']").click()
print(driver.title)
time.sleep(1)
windowids=driver.window_handles
parent=windowids[0]
driver.switch_to.window(parent)
time.sleep(1)
driver.find_element(by=By.XPATH, value="//a[text()='Selenium in biology']").click()
print(driver.title)
time.sleep(1)
driver.switch_to.window(parent)
driver.find_element(by=By.XPATH, value="//a[text()='Selenium (software)']").click()
print(driver.title)
time.sleep(1)
driver.switch_to.window(parent)
time.sleep(5)




