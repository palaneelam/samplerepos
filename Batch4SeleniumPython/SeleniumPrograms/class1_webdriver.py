import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Option 1:
# driverPath = r"C:\Users\Neelam\PycharmProjects\webdrivers\chromedriver.exe"
# servicePath = Service(driverPath)
# driver = webdriver.Chrome(service=servicePath)

# driverPath = r"C:\Users\Neelam\PycharmProjects\webdrivers\msedgedriver.exe"
# servicePath = Service(driverPath)
# driver = webdriver.Edge(service=servicePath)

# driverPath = r"C:\Users\Neelam\PycharmProjects\webdrivers\geckodriver.exe"
# servicePath = Service(driverPath)
# driver = webdriver.Firefox(service=servicePath)

#Option 2
# driver = webdriver.Chrome()
# driver = webdriver.Edge()
driver = webdriver.Firefox()

driver.get("https://edwheel.com/index.php/selenium-practice/")
driver.maximize_window()

print("Title of the open webpage is:",driver.title)
print("Current url is:",driver.current_url)
# driver.get("https://edwheel.com/")
# time.sleep(5)
# print("Current url is:",driver.current_url)
# driver.back()
# print("Current url is:",driver.current_url)
# driver.forward()
# print("Current url is:",driver.current_url)
# driver.refresh()
# print("Current url is:",driver.current_url)


# driver.minimize_window()


#***************************************************************************************************************
driver.find_element(By.ID, "name").send_keys("Neelam Pal")
driver.find_element(By.ID, "email").send_keys("support@edwheel.com")
driver.find_element(By.ID, "name").clear()
driver.find_element(By.ID, "name").send_keys("Ragini Khollam")

time.sleep(10)
driver.quit()
