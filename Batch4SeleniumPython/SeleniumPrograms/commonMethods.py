from selenium import webdriver


def launchBrowser(browserName):
    if browserName.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browserName.lower() == "edge":
        driver = webdriver.Edge()
    elif browserName.lower() == "firefox":
        driver = webdriver.Firefox()
    else:
        print("Not a right browser name. Resetting it to default Chrome browser")
        driver = webdriver.Chrome()
    return driver

# def openApplication(browserDriver, url):
#     browserDriver.get(url)
#     return browserDriver