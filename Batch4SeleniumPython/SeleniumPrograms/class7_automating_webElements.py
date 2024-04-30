import time

from selenium.webdriver import ActionChains
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

#************************************************************************************************************

# handling link
# driver.find_element(By.PARTIAL_LINK_TEXT, "Sample").click()
# driver.find_element(By.LINK_TEXT, "Sample Link").click()
# time.sleep(5)

# handling switch window
driver.find_element(By.ID, "switchWindowButton").click()
driver.switch_to.window(driver.window_handles[1])
print(driver.title)

print("window handle id: ",driver.window_handles[0])

driver.switch_to.window(driver.window_handles[0])
print("After switching back:", driver.title)

driver.implicitly_wait(10)

#handling alert
driver.find_element(By.ID, "nameTextbox").send_keys("Neelam")
driver.find_element(By.XPATH, "//button[text()='Alert']").click()
# time.sleep(2)

alert_box = driver.switch_to.alert
alert_text = alert_box.text
print("ALert text:", alert_text)
# time.sleep(5)

#when alert has ok button
alert_box.accept()
# time.sleep(2)

# if alert box has cancel button
# alert_box.dismiss()

# Handling mouse hovers
# using Action class - Advanced user Interactions
action = ActionChains(driver)
action.click_and_hold(driver.find_element(By.ID, "mouseHoverButton")).perform()
# time.sleep(10)

#right-click
# action.context_click(driver.find_element(By.ID, "mouseHoverButton")).perform()

# action.drag_and_drop(driver.find_element(By.ID, "mouseHoverButton")).perform()

#handling iframe
# driver.find_element(By.ID, "toggleIframeButton").click()
# time.sleep(5)
# driver.switch_to.frame("exampleIframe")
# time.sleep(10)
# print("Iframe title: ", driver.title)
# print("header is:", driver.find_element(By.TAG_NAME, "h1").text)

# handling dynamic web-elements
driver.find_element(By.ID, "hideShowButton").click()
time.sleep(5)

try:
    driver.find_element(By.ID, "toggleTextbox").send_keys("Neelam")
except Exception as e:
    print("Hid/Show text filed does not appear", e)

#handling webtables

# table_first_cell = driver.find_element(By.XPATH, '//table[@id="sampleTable"]/tbody/tr[1]/td[1]').text
# table_second_cell = driver.find_element(By.XPATH, '//table[@id="sampleTable"]/tbody/tr[1]/td[2]').text

table = driver.find_element(By.XPATH, '//table[@id="sampleTable"]/tbody')
rows = table.find_elements(By.XPATH, ".//tr")

for rw in rows:
    cells = rw.find_elements(By.XPATH, ".//td")
    for cellVal in cells:
        print(cellVal.text)


#handling calendar object
calendar = driver.find_element(By.ID, "calendarInput").send_keys("04/15/2024")

time.sleep(10)



driver.close()