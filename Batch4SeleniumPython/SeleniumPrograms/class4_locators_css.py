#************************* Sample HTML ******************************
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Advanced CSS Selectors</title>
#     <style>
#         /* CSS styles will be applied here */
#     </style>
# </head>
# <body>
#     <ul>
#         <li>Item 1</li>
#         <li>Item 2</li>
#         <li>Item 3</li>
#         <li>Item 4</li>
#         <li>Item 5</li>
#     </ul>
#     <div class="container">
#         <div>Div 1</div>
#         <div>Div 2</div>
#         <div>Div 3</div>
#         <div>Div 4</div>
#         <div>Div 5</div>
#     </div>
#     <input type="text" placeholder="Text input">
#     <input type="checkbox" id="checkbox1">
#     <input type="checkbox" id="checkbox2">
#     <input type="checkbox" id="checkbox3" checked>
# </body>
# </html>

# Advanced XSS Selectors Cheat-sheet
# 1. li:nth-child(2)            ----- select every second list item
# 2. li:nth-of-type(odd)        ----- selects odd-numbered list
# 3. li:first-child             ----- selects first child of list
# 4. li:last-child             ----- selects last child of list
# 5. li:only-child             ----- selects only child of list
# 6. input:not([type='text'])  ----- selects all the inputs whose attribute 'type' does not have value as 'text'


# ************************  From EdWheel Practice page **************************************************
# select option:nth-child(2)
# select option:nth-child(odd)
# select option:first-child
# select option:last-child
# input option:only-child
# input:not([type='text'])

# ***************** XPATH LOCATORS ***********************************************
# Xpath (Basic) - absolute xpath & relative xpath

# Absolute xpath - starts from root node (Ex. - html/body/ul/li)
# Prone to breaking if the structure of HTML changes

# Relative xpath = starts from anywhere in the HTML document
# More flexible and less prone to break

import time

from selenium.webdriver.common.by import By


from SeleniumPrograms.commonMethods import launchBrowser

driver = launchBrowser("chrome")

driver.maximize_window()
driver.get("https://edwheel.com/index.php/selenium-practice/")

print("Title of open page is: ", driver.title)


driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Neelam")
time.sleep(5)

# Xpath Components:
# 1. Node Selection:
# /: selects from the root node (absolute path)
# //: selects nodes anywhere in the document (Relative xpath)

# 2. Element selection:
# tagname: selects all elements witht he specified tag name
print("Count of input elements:",driver.find_elements(By.XPATH, "//input"))

# 3. *: selects any element
driver.find_element(By.XPATH, "//*[@id='name']").send_keys("Oindrila")

# 4. Attribute selection:
# [@attibute = 'value'] : selects element with a specific attribute and its value
driver.find_element(By.XPATH, "//input[@id='name']").clear()

# 5. Indexing:
driver.find_element(By.XPATH, "//input[6]").send_keys("support@edwheel.com")

# 6. Conditions (and, or)
driver.find_element(By.XPATH, "//*[@id='name' or @name='name']").send_keys("Ragini")
driver.find_element(By.XPATH, "//*[@id='name' and @name='name']").clear()
# driver.find_element(By.XPATH, "//button[text()='Alert' or text()='Reset']").click()

# selecting by text:
# text() - selects element with exact text

#selecting by partial attribute:
# contain(text(),"sub") - selects elements containing the text part

# driver.find_element(By.XPATH, "//button[contains(text(),'Ale')]").click()

time.sleep(5)