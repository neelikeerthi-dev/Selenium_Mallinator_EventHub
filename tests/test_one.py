from selenium.webdriver.support.wait import WebDriverWait
from pages.mallinator_page import MallinatorPage
from pages.register_page import RegisterMain
from pages.login_page import LoginPage
import time

password = "12345678Ke@"

def test_mallinator(driver):
#mallinator page
    mallinator = MallinatorPage(driver)
    email = mallinator.mallinator_generate_button()
    print("Generated email:", email)

#register page
    register = RegisterMain(driver)
    register.register_button_home(email, password, password)
    WebDriverWait(driver,10)
#login page
    login = LoginPage(driver)
    time.sleep(10)
    login.login_web(email, password)
