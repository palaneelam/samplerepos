import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup():
    driver = webdriver.Chrome()

    yield driver

    print("\nClosing browser... ")
    driver.close()