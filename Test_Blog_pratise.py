from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select


def setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj=Service("C:/Python_Selenium/Drivers/chromedriver-win64/chromedriver.exe")
    driver=webdriver.Chrome(service=serv_obj)
    return driver
my_driver=setup()
my_driver.implicitly_wait(10)
my_driver.get("https://testautomationpractice.blogspot.com/")
my_driver.maximize_window()
# my_driver.find_element(by=By.XPATH, value="//input[@id='name']").send_keys("mahesh babu")
# sleep(1)
# my_driver.find_element(by=By.XPATH, value="//input[@id='email']").send_keys("mahesh@gmail.com")
# sleep(1)
# my_driver.find_element(by=By.XPATH, value="//input[@id='phone']").send_keys("1234568919")
# sleep(1)
# my_driver.find_element(by=By.XPATH, value="//textarea[@id='textarea']").send_keys("OPPOSITE JOURNALIST COLONY, SAI VENKATA BRUNDAVANUM COLONY, CHABOLU ROAD")
# sleep(1)
# # my_driver.find_element(by=By.XPATH, value="//input[@value='female']").click()
# sleep(1)
# #checking all checkboxes and radio buttons:
# radio_butons=my_driver.find_element(by=By.XPATH, value="//input[@id='female']").click()
# sleep(1)
# #Days:
# Days_buttons=my_driver.find_elements(by=By.XPATH, value="//label[@for='days']/..//input[@class='form-check-input']")
# for d in Days_buttons:
#         d.click()
# sleep(1)
# #Dropdown:
# drp=Select(my_driver.find_element(by=By.XPATH, value="//select[@id='country']"))
# drp.select_by_visible_text("Australia")
# sleep(1)
# #Slider:
# my_driver.find_element(by=By.XPATH, value="//option[@value='yellow']").click()
# sleep(1)
# #Datepikcer:
# my_driver.find_element(by=By.XPATH, value="//input[@class='hasDatepicker']").send_keys("06/11/2024")
# sleep(1)
# #links:
# # my_driver.find_element(by=By.XPATH, value="//a[text()='open cart          ']").click()
# # sleep(1)
# # my_driver.back()
# sleep(1)
# my_driver.find_element(by=By.XPATH, value="//a[text()='orange HRM']").click()
# sleep(1)
# my_driver.back()
# my_driver.find_element(by=By.XPATH, value="//a[text()='Home']").click()
# sleep(5)
# my_driver.find_element(by=By.XPATH, value="//a[contains(text(),'Posts')]").click()
# sleep(3)
# print(my_driver.window_handles)
# IDs=my_driver.window_handles
# Parent_id=IDs[0]
# child_id=IDs[1]
# for i in IDs:
#     my_driver.switch_to.window(Parent_id)
# sleep(3)
#
# #Table data:
# rows=my_driver.find_elements(by=By.XPATH, value="//table[@name='BookTable']//tr")
# col=my_driver.find_elements(by=By.XPATH, value="//table[@name='BookTable']//tr/th")
# for r in range(2,len(rows)+1):
#     for c in range(1,len(col)+1):
#         data=my_driver.find_element(by=By.XPATH, value="//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data, end='')
#     print()
# sleep(1)
# #Checkboces of Table:
# rows= my_driver.find_elements(by=By.XPATH, value="//table[@id='productTable']//tbody/tr")
#
# for r in range(1,len(rows)+1):
#     check=my_driver.find_element(by=By.XPATH, value="//table[@id='productTable']//tbody/tr["+str(r)+"]/td[4]/input")
#     check.click()
# sleep(1)

#wiki pedia:
# my_driver.find_element(by=By.XPATH, value="//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("Rony")
# sleep(1)
# my_driver.find_element(by=By.XPATH, value="//input[@class='wikipedia-search-button']").click()
# sleep(1)
# my_driver.find_element(by=By.XPATH, value="//a[text()='Rony Jason']").click()
# sleep(1)
# Tab_ID=my_driver.window_handles
#
# for id in Tab_ID:
#     my_driver.switch_to.window(id)
#     if my_driver.title =="Rony Jason - Wikipedia":
#         my_driver.close()
# sleep(3)
# #New broser window button:
# my_driver.find_element(by=By.XPATH, value="//div[@class='widget-content']//button[text()='New Browser Window']").click()
# sleep(3)
# win_id=my_driver.window_handles
# for w in win_id:
#     my_driver.switch_to.window(w)
#     if my_driver.title=="Your Store":
#         my_driver.close()
# sleep(3)
my_driver.find_element(by=By.XPATH, value="//button[text()='Alert']").click()
sleep(1)
alt=my_driver.switch_to.alert
alt.accept()
sleep(1)
my_driver.find_element(by=By.XPATH, value="//button[text()='Confirm Box']").click()
alt=my_driver.switch_to.alert
alt.dismiss()
sleep(1)
my_driver.find_element(by=By.XPATH, value="//button[text()='Prompt']").click()
alt=my_driver.switch_to.alert
alt.send_keys("mahesh babu")
alt.accept()
sleep(3)
#Actions:
action=ActionChains(my_driver)
action.double_click(my_driver.find_element(by=By.XPATH, value="//button[text()='Copy Text']")).perform()
sleep(1)
source=my_driver.find_element(by=By.XPATH, value="//div[@id='draggable']")
Target=my_driver.find_element(by=By.XPATH, value="//div[@id='droppable']")
action.drag_and_drop(source,Target).perform()
sleep(1)
#Slider Range:
slider_position=my_driver.find_element(by=By.XPATH, value="//*[@class='ui-slider-handle ui-corner-all ui-state-default']")
print(slider_position)
action.drag_and_drop_by_offset(slider_position,50,0).perform()
sleep(1)
#Frames:
# frame=my_driver.find_element(by=By.XPATH, value="//iframe[@id='frame-one796456169']")
my_driver.switch_to.frame('frame-one796456169')
my_driver.find_element(by=By.XPATH, value="//input[@id='RESULT_TextField-0']").send_keys("mahesh babu Rony")
sleep(1)
radio=my_driver.find_element(by=By.XPATH, value="//table[@class='inline_grid choices']/tbody/tr/td/input[@id='RESULT_RadioButton-1_0']")
my_driver.execute_script("arguments[0].click;",radio)
my_driver.execute_script("arguments[0].click;",radio)
sleep(1)
my_driver.find_element(by=By.XPATH, value="//input[@placeholder='mm/dd/yyyy']").send_keys("06/11/2024")   #shoudl try another approcah also
sleep(1)
drp=Select(my_driver.find_element(by=By.XPATH, value="//select[@id='RESULT_RadioButton-3']"))
drp.select_by_visible_text("Automation Engineer")
sleep(1)
my_driver.find_element(by=By.XPATH, value="//input[@id='FSsubmit']").click()
sleep(3)
#Resizeable element:
resize=my_driver.find_element(by=By.XPATH, value="//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
action.click_and_hold(resize).move_by_offset(80,50).release().perform()
sleep(3)










