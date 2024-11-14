# # from selenium import webdriver
# # from selenium.webdriver import ActionChains
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as e
# # from time import sleep
#
#
# # serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
# # option=webdriver.ChromeOptions()
# # option.add_argument("--disable-Notifications")
# # driver=webdriver.Chrome(service=serv_obj,options=option)
# # driver.implicitly_wait(10)
# # driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
# # driver.maximize_window()
# #
# # action=ActionChains(driver)
# # # oslo=driver.find_element(by=By.ID, value="box1")
# # # norway=driver.find_element(by=By.ID, value="box101")
# # # action.click_and_hold(oslo).move_to_element(norway).release().perform()
# # # sleep(3)
# #
# # citys=['box1','box2','box3','box4','box5','box6','box7']
# # Countries=['box101','box102','box103','box104','box105','box106','box107']
# #
# # for city,country in zip(citys,Countries):
# #     cit=driver.find_element(by=By.ID, value=city)
# #     coun=driver.find_element(by=By.ID, value=country)
# #
# #     action.click_and_hold(cit).move_to_element(coun).release().perform()
#
#
#
# #Assignment Task:
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from time import  sleep
# from selenium.webdriver import ActionChains,Keys
#
# serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
# option=webdriver.ChromeOptions()
# option.add_argument("--disable-Notifications")
# option.add_experimental_option("detach", True)
# driver=webdriver.Chrome(service=serv_obj, options=option)
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# driver.implicitly_wait(10)
#
# #Hover:
# alt=driver.find_element(by=By.XPATH, value="//button[text()='Alert']")
# action=ActionChains(driver)
# action.move_to_element(alt).perform()
# print("hovered")
# sleep(1)
#
# #Rightclick:
# ele=driver.find_element(by=By.ID, value="droppable")
# action.context_click(ele).perform()
# print("Right clciked")
# sleep(1)
# #double click:
# dbl_btn=driver.find_element(by=By.XPATH, value="//button[text()='Copy Text']")
# action.double_click(dbl_btn).perform()
# print("Double clicked")
# sleep(1)
# #Drag and drop:
# source=driver.find_element(by=By.ID, value="draggable")
# Target=driver.find_element(by=By.ID, value="droppable")
# action.drag_and_drop(source, Target).perform()
# print("dropped")
# sleep(1)
# #Click&Hold:
# web=driver.find_element(by=By.XPATH, value="//div[@class='ui-resizable-handle ui-resizable-e']")
# print("postion of box:", web.location)
# action.click_and_hold(web).move_by_offset(80,0).release().perform()
# print("holded")
# print("postion of box after changes:", web.location)
# sleep(1)
#
# #slider range:
# slid=driver.find_element(by=By.XPATH, value="//span[@class='ui-slider-handle ui-corner-all ui-state-default']")
# print("slider position:",slid.location)
# action.drag_and_drop_by_offset(slid ,50,0).perform()
# print("Slider position after action:",slid.location)
# sleep(5)
#
# driver.close()
#
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver import Keys, ActionChains
from time import sleep


driver=webdriver.Chrome()
driver.get("https://demoapps.qspiders.com/ui?scenario=1")
driver.implicitly_wait(10)
driver.maximize_window()
act=ActionChains(driver)
driver.find_element(By.XPATH,"//section[text()='Mouse Actions']").click()
sleep(1)
driver.find_element(By.XPATH,"//section[text()='Drag & Drop']").click()
sleep(1)
# target=driver.find_element(By.XPATH,"//div[text()='Drag Me']")
# source=driver.find_element(By.XPATH,"//div[@style='transform: translate(-278px, -124px);']")
# act.drag_and_drop(target,source).perform()
sleep(1)
driver.find_element(By.XPATH,"//a[text()='Drag Position']").click()
sleep(1)
t=driver.find_element(By.XPATH,"//div[text()='Mobile Charger']")
s=driver.find_element(By.XPATH,"//div[text()='Mobile Accessories']")
act.drag_and_drop(t,s).perform()
ta=driver.find_element(By.XPATH,"//div[text()='Laptop Charger']")
so=driver.find_element(By.XPATH,"//div[text()='Laptop Accessories']")
act.drag_and_drop(ta,so).perform()
sleep(1)
driver.find_element(By.XPATH,"//section[text()='Mouse Hover']").click()
sleep(1)
mouse=driver.find_element(By.XPATH,"//img[@src='/assets/message-hint-J20Zlhln.png']")
act.move_to_element(mouse).perform()
driver.find_element(By.XPATH,"//a[text()='Image']").click()
mouse_img=driver.find_element(By.XPATH,"//p[text()='Your Order has been successfully placed!']")
act.move_to_element(mouse_img).perform()
driver.find_element(By.XPATH,"//section[text()='Click & Hold']").click()
hold=driver.find_element(By.XPATH,"//div[@class='zoom-button ']")
act.click_and_hold(hold).release().perform()
sleep(2)

driver.find_element(By.XPATH,"//section[text()='Keyboard Actions']").click()
sleep(2)
driver.find_element(By.XPATH,"//section[text()='Virtual Keyboard']").click()
sleep(1)
driver.find_element(By.XPATH,'//input[@name="email"]')
sleep(1)
# driver.find_element(By.ID,"email").send_keys("mahesh@gmail.com")
act.send_keys(Keys.TAB).send_keys("mahesh@gmail.com").send_keys(Keys.TAB).send_keys('123').send_keys(Keys.TAB).click().perform()
sleep(5)
driver.close()


