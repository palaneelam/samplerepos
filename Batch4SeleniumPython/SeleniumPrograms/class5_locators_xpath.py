import time

from selenium.webdriver.common.by import By


from SeleniumPrograms.commonMethods import launchBrowser

driver = launchBrowser("chrome")

driver.maximize_window()
driver.get("https://edwheel.com/index.php/selenium-practice/")

print("Title of open page is: ", driver.title)

#selecting by partial attribute:
# contain(text(),"sub") - selects elements containing the text part
# starts-with(text(),"sub") - selects elements which starts with initial text part

driver.find_element(By.XPATH, "//button[contains(text(),'Ale')]").click()
driver.find_element(By.XPATH, "//button[starts-with(text(),'Reset')]").click()

# BASIC - XPATH Cheatsheet:
# // : selects nodes anywhere in the document
# * : selects any element
# tagname: selects all elements with the specified tag name
# [@attribute='value']: selects elements with a specific attribute and value
# [index]: selects nth occurence of the element
# and, or : combines the condition with any of these clause
# text() : selects elements based on text content
# starts-with(), contains(): Partial attribute value matching

# TIP for writing XPATHS:
# prefer using relative xpath
# avoid using indexes unless necessary - xpath is fragile
# use browser's dev tool only
# ensure that xpath returns only 1 occrence of that element, specially in case of dynamic elements
# test xpath in browser console - test your XPATH expression in browser's inspect tool

#************************************************************************************************************
# Advanced XPATH techniques:
# 1. XPath axes:
# axes are used to navigate the tree structure of HTML or XML
# common axes are - child, parent, following-sibling & preceeding sibling
driver.find_element(By.XPATH, "//a[text()='Sample Link']/parent:: label")
driver.find_element(By.XPATH, "//label[@for='sampleLink']/preceding-sibling:: select")
driver.find_element(By.XPATH, "//label[@for='sampleLink']/preceding:: select")
driver.find_element(By.XPATH, "//label[@for='sampleLink']/following-sibling:: table")
driver.find_element(By.XPATH, "//label[@for='sampleLink']/following:: table")
driver.find_element(By.XPATH, "//label[@for='sampleLink']/a")

# 2. xpath Function:
# text(), start-with(), contains(), concat()

# 3. Logical Operators:
# and, or, not

# 4. using ancestor & dependent
driver.find_element(By.XPATH, "//label[@for='sampleLink']/ancestor:: select")
driver.find_element(By.XPATH, "//label[@for='sampleLink']/descendant:: table")

# 5. Using position() and last():
driver.find_element(By.XPATH, "(//input)[position()=6]")
driver.find_element(By.XPATH, "(//input)[last()]")

# Advanced XPath Cheatsheet:

# Axes:
# child::: Selects direct child elements.
# parent::: Selects the parent element.
# following-sibling::: Selects elements that follow the current element.
# preceding-sibling::: Selects elements that precede the current element.

# Functions:
# text(): Selects nodes based on text content.
# contains(string, substring): Checks if a string contains a specified substring.
# starts-with(string, substring): Checks if a string starts with a specified substring.
# concat(string1, string2): Concatenates two strings.

# Logical Operators:
# and: Combines multiple conditions with AND.
# or: Combines multiple conditions with OR.
# not: Negates a condition.

# Positional Operators:
# position(): Returns the index of the current node.
# last(): Returns the index of the last occurrence of the current node.

# Miscellaneous:
# ancestor::: Selects ancestors of the current node.
# descendant::: Selects descendants of the current node.



# Tips for Advanced XPath Creation:

# Use the Browser DevTools:
# Inspect elements and use the browser's DevTools to generate complex XPath expressions.

# Understand Document Structure:
# Understand the document structure to leverage axes effectively.

# Combine Functions and Axes:
# Combine functions and axes to create precise and dynamic XPath expressions.

# Test XPath Expressions:
# Test XPath expressions in the browser console before using them in your automation scripts.

# Be Mindful of Performance:
# Avoid overly complex XPath expressions for better performance.