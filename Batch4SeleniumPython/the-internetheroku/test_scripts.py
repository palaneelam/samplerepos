
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

import variables

from SeleniumPrograms.commonMethods import launchBrowser

driver = launchBrowser(variables.browserName)

driver.maximize_window()
driver.get(variables.appURL)

def abtesting():
    driver.find_element(By.LINK_TEXT, "A/B Testing").click()
    headertext = driver.find_element(By.TAG_NAME, "h1").text
    print("Header text is: ", headertext)
    pageContent = driver.find_element(By.TAG_NAME, "h1").text
    print("Page content is: ", pageContent)
    driver.back()


def addRemoveElement():
    add_remove_elements_link = driver.find_element(By.LINK_TEXT, "Add/Remove Elements")
    add_remove_elements_link.click()
    add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
    add_button.click()
    print("Added an element!")
    time.sleep(1)
    delete_button = driver.find_element(By.XPATH, "//button[text()='Delete']")
    delete_button.click()
    print("Deleted the element!")
    time.sleep(1)

    # Confirm deletion by checking if the "Delete" button is no longer present
    assert not driver.find_elements(By.XPATH, "//button[text()='Delete']"), "Element deletion failed!"

    print("Automation successful!")

def basicAuth():
    url = "https://the-internet.herokuapp.com/basic_auth"

    # Set the username and password for basic authentication
    username = "admin"
    password = "admin"

    # Navigate to the URL
    driver.get(url)

    # Build the authentication URL with username and password
    auth_url = f"https://{username}:{password}@{url.split('//')[1]}"
    auth_url = "https://admin:admin@the-internet.herokuapp.com/basic_auth"

    # Navigate to the authentication URL
    driver.get(auth_url)

    # Verify if the authentication is successful
    if "Congratulations! You must have the proper credentials." in driver.page_source:
        print("Authentication Successful! You have access to the page.")
    else:
        print("Authentication Failed! Please check your credentials.")


def context_click():
    driver.find_element(By.XPATH, "//a[text()='Context Menu']").click()
    # heading_context = driver.find_element(By.TAG_NAME, context_menu_heading).text
    # print(heading_context)
    # context_menu_paragraph = driver.find_element(By.XPATH, "(//p)[1]").text
    # print(context_menu_paragraph)
    time.sleep(5)
    action = ActionChains(driver)
    action.context_click(driver.find_element(By.ID, "hot-spot")).perform()
    print("right click done succesffully")

    alert_box = driver.switch_to.alert
    # # alert_text = alert_box.text
    alert_box.accept()

    action.move_by_offset(0,0).click().perform()
    # action.send_keys(Keys.ENTER)
    # action.send_keys(Keys.ESCAPE)
    # print("alert box clicked sucessfully")
    time.sleep(5)
    # action.send_keys(Keys.ENTER)
    # driver.refresh()


context_click()
driver.refresh()
time.sleep(10)

# TC1 - A/B Testing
# abtesting()
#
# #TC2 - Add Remove Elements
# addRemoveElement()