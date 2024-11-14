from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

serv_obj=Service("C:/Python_Selenium/Drivers/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(15)

#Demo web shop:
# driver.get("https://demowebshop.tricentis.com/")
# driver.maximize_window()
# driver.find_element(by=By.XPATH, value='//*[@class="top-menu"]//a[@href="/digital-downloads"]').click()
# sleep(1)
# driver.find_element(by=By.XPATH, value="//div[@data-productid='53']//input[@value='Add to cart']").click()
# sleep(5)

#Amozon locator:
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# driver.find_element(by=By.XPATH, value="//input[@title='Search For']").send_keys("shoes")
# sleep(1)
# driver.find_element(by=By.XPATH, value="//input[@value='Go']").click()
# sleep(1)
# driver.find_element(by=By.XPATH, value="//span[text()='Zeus Men Fashion Sneakers/Running Shoes with Chunky Rubber Outsole for Running, Walking, Training, Gyming, Streets, Parties & Fun']").click()
# sleep(5)


#Task:
# url:Big basket
# price=350 --> add to cart

# driver.get("https://www.bigbasket.com/?utm_source=google&utm_medium=cpc&utm_campaign=Brand-T1&gad_source=1&gclid=EAIaIQobChMI_b_KweyWhwMVrBGtBh3UXQAGEAAYASAAEgIkOfD_BwE")
# driver.maximize_window()
# # searchbar=driver.find_element(by=By.XPATH,value="//div[@class='Header___StyledQuickSearch2-sc-19kl9m3-0 gzbZOD']//input[@placeholder='Search for Products...']").send_keys("Apples")
# searchbar=driver.find_element(by=By.XPATH,value="//div[contains(@class,'Header___StyledQuickSearch2')]//input[@placeholder='Search for Products...']").send_keys("Apples")
# sleep(1)
# driver.find_element(by=By.XPATH, value="//ul[@class='overscroll-contain']//span[text()='₹350']//..//..//button[text()='Add']").click()
# sleep(2)
# driver.find_element(by=By.XPATH, value="//*[@class='cursor-pointer mr-3']").click()
# sleep(1)
# driver.find_element(by=By.XPATH, value="//*[@class='px-1.5 w-9cursor-pointer rounded-2xs py-1.5  bg-rossoCorsa-50 relative']").click()
# sleep(2)
# driver.find_element(by=By.XPATH, value="//input[@placeholder='Enter Phone number/ Email Id']").send_keys("8639563301")
# sleep(2)
# driver.find_element(by=By.XPATH, value="//*[text()='Continue']").click()
# sleep(20)









