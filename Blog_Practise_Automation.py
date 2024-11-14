from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select

def setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:/Python_Selenium/Drivers/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    return driver

my_driver = setup()
my_driver.implicitly_wait(10)
my_driver.get("https://testautomationpractice.blogspot.com/")
my_driver.maximize_window()
sleep(1)
my_driver.find_element(by=By.ID, value='name').send_keys("Rony Mahesh Babu")
my_driver.find_element(by=By.ID, value='email').send_keys("mail2mahebabu@gmail.com")
my_driver.find_element(by=By.ID, value='phone').send_keys('8639563301')
my_driver.find_element(by=By.ID, value='textarea').send_keys("Sai venkata brundavanum colony")
sleep(1)
my_driver.find_element(by=By.XPATH, value="//input[@name='gender' and @value='male']").click()
sleep(1)
Days = my_driver.find_elements(by=By.XPATH, value='//*[@id="post-body-1307673142697428135"]/div[4]/div')
day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
for d in Days:
    if d.text in day:
        d.click()
sleep(2)
Country_drp=Select(my_driver.find_element(by=By.XPATH, value='//*[@id="country"]'))
Country_drp.select_by_visible_text("Germany")
sleep(2)
Colours_scroll=Select(my_driver.find_element(by=By.XPATH, value='//select[@id="colors"]'))
Colours_scroll.select_by_visible_text("Blue")
sleep(2)
my_driver.find_element(by=By.XPATH, value="//input[@class='hasDatepicker']").send_keys("06/11/2024")
sleep(2)
my_driver.find_element(by=By.XPATH, value="//a[text()='open cart          ']").click()
sleep(1)
my_driver.back()
my_driver.find_element(by=By.XPATH, value="//a[text()='orange HRM']").click()
sleep(2)
my_driver.back()
my_driver.find_element(by=By.XPATH, value="//a[@class='home-link']").click()
sleep(1)
my_driver.find_element(by=By.XPATH, value="//a[@class='feed-link']").click()
print("window ID's:",my_driver.window_handles)
ID=my_driver.window_handles
Parent_window=ID[0]
Child_window=ID[1]
sleep(1)
my_driver.switch_to.window(Parent_window)
sleep(2)

# #Another aprroach:
# # for i in ID:
# #     my_driver.switch_to.window(i)
# #     tite=my_driver.title
# #     if tite=="testautomation" or tite=="facebook":
# #         my_driver.close()
#
#printing all data of Table:
rows=my_driver.find_elements(by=By.XPATH, value='//*[@id="HTML1"]/div/table/tbody/tr')
columns=my_driver.find_elements(by=By.XPATH, value='//*[@id="HTML1"]/div/table/tbody/tr[1]/th')

for r in range(2,len(rows)+1):
    for c in range(1,len(columns)+1):
        data=my_driver.find_element(by=By.XPATH, value="//*[@id='HTML1']/div/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text

        print(data, end=' ')
    print()

#Checking checking all:
count_row=my_driver.find_elements(by=By.XPATH, value='//*[@id="productTable"]/tbody/tr')

for r in range(1,len(count_row)+1):
    my_driver.find_element(by=By.XPATH, value="//*[@id='productTable']/tbody/tr["+str(r)+"]/td[4]/input").click()
sleep(3)

my_driver.find_element(by=By.XPATH, value="//input[@class='wikipedia-search-input']").send_keys("mahesh")
sleep(1)
my_driver.find_element(by=By.XPATH, value='//*[@id="Wikipedia1_wikipedia-search-form"]/div/span[2]/span[2]/input').click()
sleep(1)
my_driver.find_element(by=By.LINK_TEXT, value='Mahesh Babu').click()
sleep(2)
wiki_ID=my_driver.window_handles
Parent_id= wiki_ID[0]
Child_id=wiki_ID[1]
sleep(1)
for id in wiki_ID:
    my_driver.switch_to.window(id)
    if my_driver.title == "Mahesh Babu - Wikipedia":
        my_driver.close()
sleep(4)

# New Browser window:
Next_frame=my_driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside")
my_driver.switch_to.frame(Next_frame)
sleep(1)
my_driver.find_element(by=By.XPATH, value='//*[@id="sidebar-right-1"]/div[2]/div[1]/button').click()
sleep(2)
link_ID= my_driver.window_handles
for id in link_ID:
    my_driver.switch_to.window(id)
    if my_driver.title=="Your Store":
        my_driver.close()
sleep(3)

#Alerts:
my_driver.find_element(by=By.XPATH, value='//*[@id="HTML9"]/div[1]/button[1]').click()
alet=my_driver.switch_to.alert
alet.accept()
sleep(2)
my_driver.find_element(by=By.XPATH, value='//*[@id="HTML9"]/div[1]/button[2]').click()
alt=my_driver.switch_to.alert
alt.dismiss()
sleep(2)
my_driver.find_element(by=By.XPATH, value='//*[@id="HTML9"]/div[1]/button[3]').click()
atl=my_driver.switch_to.alert
atl.send_keys("Rony mahesh Babu")
atl.accept()
sleep(3)


#Mouse Actions:
#Double click:
action=ActionChains(my_driver)
dbl_button=my_driver.find_element(By.XPATH, '//*[@id="HTML10"]/div[1]/button')
action.double_click(dbl_button).perform()

#Drag and drop:
drag_source=my_driver.find_element(By.ID, 'draggable')
drop_target=my_driver.find_element(By.ID, 'droppable')
action.drag_and_drop(drag_source,drop_target).perform()

#Slider:
slider_position=my_driver.find_element(By.XPATH, '//*[@id="slider"]/span')
print(slider_position)
action.drag_and_drop_by_offset(slider_position,100,0).perform()

#Frames:
my_driver.switch_to.frame('frame-one796456169')
#Text box:
my_driver.find_element(By.XPATH, '//*[@id="RESULT_TextField-0"]').send_keys("Mahesh Babu Rony")
sleep(2)
#Radion button:
radio_button=my_driver.find_element(By.ID, 'RESULT_RadioButton-1_1')
my_driver.execute_script("arguments[0].click;",radio_button)
# radio_button = my_driver.find_element(By.ID, 'RESULT_RadioButton-1_1')
# my_driver.execute_script("arguments[0].click();", radio_button)
sleep(2)
#Date calender:
my_driver.find_element(By.XPATH, '//*[@id="RESULT_TextField-2"]').send_keys("06/11/2024")
sleep(2)
#DropDown:
drp_down=Select(my_driver.find_element(By.XPATH, '//*[@id="RESULT_RadioButton-3"]'))
drp_down.select_by_visible_text("QA Engineer")
#Report Abuse:
my_driver.find_element(By.XPATH, '//*[@id="FSForm"]/div[2]/div[10]/a[2]').click()
sleep(2)
#Action performed in New window:
# my_driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-5']").send_keys("mail2mahebabu@gmail.com")
# sleep(1)
# my_driver.find_element(By.XPATH,'//*[@id="RESULT_CheckBox-6_0"]').click()
# sleep(1)
# my_driver.find_element(By.XPATH, '//*[@id="recaptcha-anchor"]/div[1]').click()
Win_ID=my_driver.window_handles
for w in Win_ID:
    my_driver.switch_to.window(w)
    if my_driver.title=="Report Abuse":
        my_driver.close()
sleep(1)

#Form Site:
# my_driver.find_element(By.XPATH, '//*[@id="FSForm"]/div[2]/div[10]/a[1]').click()
# sleep(2)
# my_driver.back()

#Submit:
# my_driver.find_element(By.XPATH, "//input[@id='FSsubmit']").click()
# sleep(2)

#Resize:
# resize_field=my_driver.find_element(By.XPATH, '//*[@id="resizable"]/div[3]')
# action.click_and_hold(resize_field).move_by_offset(30,50).release().perform()







