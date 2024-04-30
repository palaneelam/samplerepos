import time

from selenium.webdriver.common.by import By

from SeleniumPrograms.commonMethods import launchBrowser

chromeBrowser = launchBrowser("chrome")

chromeBrowser.maximize_window()
chromeBrowser.get("https://edwheel.com/index.php/selenium-practice/")

print("Title of open page is: ", chromeBrowser.title)

# edgeBrowser.find_element(By.ID, "name").send_keys("Neelam Pal")

chromeBrowser.find_element(By.NAME, "name").send_keys("Madhuri")
chromeBrowser.find_element(By.ID, "resetButton").click()


time.sleep(5)