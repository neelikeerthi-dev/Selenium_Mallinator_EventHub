from selenium import webdriver
import pytest

@pytest.fixture
def driver():
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        yield driver
        driver.quit()