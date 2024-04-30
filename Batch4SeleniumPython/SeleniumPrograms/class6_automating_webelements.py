import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from SeleniumPrograms.commonMethods import launchBrowser

driver = launchBrowser("chrome")

driver.maximize_window()
driver.get("https://edwheel.com/index.php/selenium-practice/")

print("Title of open page is: ", driver.title)

#handling cookie information
time.sleep(10)
try:
    reject_all_button = driver.find_element(By.XPATH, "(//button[contains(text(), 'Reject All')])[1]")
    reject_all_button.click()
    print("Clicked 'Reject ALL' button in privacy pop-up")
except Exception as e:
    print(f"error: {e}")

# handling input box
driver.find_element(By.ID, "name").send_keys("Neelam Pal")
driver.find_element(By.ID, "email").send_keys("support@edwheel.com")

# handling drop down in 3 different ways
dropdownObject = driver.find_element(By.ID, "dropdown")
select_dp = Select(dropdownObject)
# 1.
select_dp.select_by_visible_text("DPValue 2")
time.sleep(5)
# 2.
select_dp.select_by_index(2)
time.sleep(5)
# 3.
select_dp.select_by_value("DPValue1")
time.sleep(5)

#handling checkbox
checkbox = driver.find_element(By.ID, "chbValue1")
checkbox.click()

driver.find_element(By.ID, "chbValue2").click()

#handling button
driver.find_element(By.ID, "resetButton").click()
time.sleep(5)

#handling listbox
listbox = driver.find_element(By.ID, "listbox")
select_list = Select(listbox)
select_list.select_by_index(1)
time.sleep(5)
select_list.select_by_value("list1")
time.sleep(5)
select_list.select_by_visible_text("List 3")
time.sleep(5)

#handling radio-button
radiobtn = driver.find_element(By.ID, "radio2")
radiobtn.click()

#handling auto-suggestion text box
driver.find_element(By.ID, "countrySuggestion").send_keys("Australia")
time.sleep(5)

# to read a value from any label or webelement

# .text method will not work for dynamic values
auto_suggest_text = driver.find_element(By.ID, "countrySuggestion").text
print("text is: ", auto_suggest_text)

# getattributevlue will work for dynamic values
auto_suggest_text1 = driver.find_element(By.ID, "countrySuggestion").get_attribute("value")
print("text from getattribute is: ", auto_suggest_text1)

#same code using css selector
driver.find_element(By.CSS_SELECTOR, "#countries > option:nth-child(2)").click()
countries = driver.find_elements(By.CSS_SELECTOR, "#countries > option")
print("Total suggestions:",len(countries))

driver.close()
