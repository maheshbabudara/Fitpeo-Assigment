from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time as t
from selenium.webdriver.support.select import Select


serv_obj = Service("C:\Python_Selenium\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.implicitly_wait(10)
driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()


Dropdown_country=driver.find_element(by=By.ID, value='input-country')

#select () is used to get the Dropdown as an web element
drp_country=Select(Dropdown_country)

#Selecting options from the dropdown:
drp_country.select_by_visible_text("India")
# drp_country.select_by_value("10")  #Argentina  #Since 10 is an value of web element kept in qotes
# drp_country.select_by_index(14)  #Index Manually we have to pick by counting from web page and since this is an index not used quotes
t.sleep(3)


#Capture all the options and print:
#options() we can use available options as an web elements:
All_options= drp_country.options
print("Total Number of options: ",len(All_options))

for opt in All_options:
    print(opt.text)
    # opt.click()   #This is not possible becoz, all values cannot be selected in dropdowns

#Select an option in dropdown without using builtin methods:
options= drp_country.options
for opt in options:
    if opt.text == "India":
        opt.click()
        break

#-------------------------------------important-----------------------------------------
# NOTE: Incase there is No 'SELECT' tag, then use XPATH directly or use common Tags for options
# ex: opt=driver.find_elements(by=By.XPATH, value="//*[@name='country_id']/option")
# print(len(opt))
# #rest other steps are same as above


#pracrive automting on dropdowns, checkboxes, radio buttons, text boxes at "test automation blospot,  etc...


