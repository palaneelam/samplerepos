import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

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
# 1. static wait statement
#hard-code wait statement
# time.sleep(2.5)

# 2. Dynamic Wait Statement
#   2.1 Implicit wait statement - waits max for the given time. If object appears before the max time, it comes out
#   of the loop and executes next line
#   Usage - they are used to set the default wait time on any web page/ web element

# driver.implicitly_wait(10)

#   2.2 Explicit wait statement - it is more specific than the implicit wait
#                                 they are applied to a particular element based on on some specific condtion.

wait = WebDriverWait(driver, 20)
wait.until(expected_conditions.presence_of_element_located((By.ID, "name")))

# taking scrrenshots
driver.get_screenshot_as_file("screen.png")

#*************************************************************************
# working with javascript
calendar = driver.find_element(By.ID, "calendarInput")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.execute_script("arguments[0].style.backgroundColor = 'yellow';", calendar)
time.sleep(10)

driver.close()