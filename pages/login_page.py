from selenium.common import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    email_field = (By.XPATH,"//input[@id='email']")
    password_field = (By.ID, "password")
    login_button = (By.ID, "login-btn")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


#to open the website and login using valid credentials
    def login_web(self, email, password):
        try:
            self.driver.get("https://eventhub.rahulshettyacademy.com/login")
            self.wait = WebDriverWait(self.driver, 10)
            email_element=self.wait.until(EC.visibility_of_element_located(self.email_field))
            email_element.send_keys(email)
            self.wait.until(EC.visibility_of_element_located(self.password_field)).send_keys(password)
            self.wait.until(EC.element_to_be_clickable(self.login_button)).click()
            return "successful login"

        except TimeoutException:
            raise TimeoutException("Timed out waiting for page to load")
        except StaleElementReferenceException:
            raise StaleElementReferenceException("Timed out wa")