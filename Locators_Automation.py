"""Locators : locators are required to Identify the web elements on web page
There are Multiple Locators in Selenium:

There are two kinds of Locators: 1.Builtin-locators which are directly supported by selenium webdriver ex: id, name,
link text(partial link text), className, Tag name.

2.Customised locators: these locators cannot find directly on
webpage. we have to generate or write "XPath (Absolute XPath, Relative XPath), or CSS Selector(Tag and ID, Tag and Class,
Tag and Attribute, Tag,class and Attribute) ",
so we call it as Customised Locators.

ID Locator: Examples
driver.find_element(by=By.ID, value="email").send_keys("mahesh")
driver.find_element(by=By.ID, value="login").click()

Name Locator: Examples
driver.find_element(by=By.NAME, value="email").send_keys("mahesh")
driver.find_element(by=By.NAME, value="login").click()

LinkText/Partial LinkText: Examples
driver.find_element(by=By.LINK_TEXT, value="Printed chifron dress").click()
driver.find_element(by=By.PARTIAL_LINK_TEXT, value="Chifron dress").click() #In partial link text we can just pass
little portion Actual text from link value.


ClassName & TagName: when we want to find/identify more than one element, then we will choose class Name or TagName.
Example:
    sliders=driver.find_elements(by=By.CLASS_NAME, value="homeslider-container")   #retuns the 'List'
    print(len(sliders))
    links=driver.find_elements(by=By.TAG_NAME, value="a")             #returns the 'list'
    print(len(links))

    #Below method will returns the single web element becoz, find_element() contains singular word but not plural word:
    driver.find_element(by=By.CLASS_NAME, value="homeslider-container") #will return 1st single web elememt becoz of "find_element()"
    driver.find_element(by=By.TAG_NAME, value="a")  #will return 1st single web elememt becoz of "find_element()"


CSS Selectors:
When there is no posibility of finding an web element with single locator, then we can go with locator combinations like Tag and ID, Tag and Class,
Tag and Attribute, Tag,class and Attribute.
-->In css selectors, Tag Names are optional.

# using index in css selector: ****************************IMP************************************
# syntax:div p:nth-child(index)

NOTE:WE cant use AND/OR functions in css selector, if really wana use it, then use it like this
ex: Tagname.classvalue,Tagname#idvalue


Examples:
    #combo of Tag name and ID:
    driver.find_element(by=By.CSS_SELECTOR, value="input#email")   #syntax: tagname#IDvalue
    #only ID:

    driver.find_element(by=By.CSS_SELECTOR, value="#email")

    #combo of Tag name and class:
    driver.find_element(by=By.CSS_SELECTOR, value="input.inputtext _55r1_6luy")  #syntax: tagname.classvalue
    #only class:
    driver.find_element(by=By.CSS_SELECTOR, value=".inputtext _55r1_6luy")

-------------NOTE: when there is an Space after value, then webdriver will consider as "empty" and execution will not be progressed,
-------------at that time just specify the value till space and run the script.

   #combo of Tag name and Atrribute:
   driver.find_element(by=By.CSS_SELECTOR, value="input[data-testid=royal_email]")   #syntax: tagname[Atrribute=value]
   #only Atrribute:
   driver.find_element(by=By.CSS_SELECTOR, value="[data-testid=royal_email]")

   #combo of Tag name, class and Attribute:
   When Tag name, class are same for multiple web elements, then to differiante them, we can choose this locator.
   driver.find_element(by=By.CSS_SELECTOR, value= "input.inputtext[data-testid=royal_pass]"

   X-Path:
   1.Absolute/Full Path:
     ex: /html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div/div[1]/input
   2.Relative/Partial X-path:
     ex: //*[@id="email"]
   X-Path options:
   And  #driver.find_element(by=By.XPATH, value="//*[@id='email' and @name='Email']")
   OR   #driver.finde_element
   contains()
   starts-with()
   text()


"""

