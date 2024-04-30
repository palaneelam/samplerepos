import time

from selenium.webdriver.common.by import By


from SeleniumPrograms.commonMethods import launchBrowser

driver = launchBrowser("chrome")

driver.maximize_window()
driver.get("https://edwheel.com/index.php/selenium-practice/")

print("Title of open page is: ", driver.title)

# Locators in any test automation
# generic locators in Selenium - ID, Name, ClassName, Linktext, partial linktext, tag
# special locators - css selectors, xpaths

# driver.find_element(By.ID, "name").send_keys("Madhuri")
driver.find_element(By.ID, "name").send_keys("Neelam Pal")
# time.sleep(5)
driver.find_element(By.NAME, "name").clear()
# time.sleep(5)
driver.find_element(By.NAME, "name").send_keys("Madhuri")
# time.sleep(5)

# headerText = driver.find_element(By.CLASS_NAME, "entry-title").text
# print("Header text is:", headerText)

# driver.find_element(By.LINK_TEXT, "Sample Link").click()

# driver.find_element(By.PARTIAL_LINK_TEXT, "Sample").click()
# time.sleep(5)

#*********************************************************************************************
# CSS-Selectors

# 1 - using css selector to locate an element by id
buttonText = driver.find_element(By.CSS_SELECTOR, "#resetButton").text
print("Text on button is: ", buttonText)

# 2 - using css selector to locate an element by class
headerText = driver.find_element(By.CSS_SELECTOR, ".entry-title").text
print("Header text is:", headerText)

# 3. using css selector by tag and class; syntax = tag.class value
hText = driver.find_element(By.CSS_SELECTOR, "h1.entry-title").text
print("Header text from css#3 is:", hText)

# 4. using css selector to locate an element by tag and attribute; syntax = tag[attribute=value]
driver.find_element(By.CSS_SELECTOR, "input[id='email']").send_keys("support@edwheel.com")
time.sleep(5)

driver.close()
