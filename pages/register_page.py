from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class RegisterMain:
    register_but=(By.XPATH,"//a[@class='text-indigo-600 hover:underline font-medium']")
    email_cli=(By.XPATH,"//input[@id='register-email']")
    password_cli=(By.XPATH,"//input[@id='register-password']")
    confirm_password_cli=(By.XPATH,"//input[@placeholder='Repeat your password']")
    click_but=(By.XPATH,"//button[@id='register-btn']")

    def __init__(self,driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

#to open the eventhub webpage and register with the generated email and verify passowrd
    def register_button_home(self, email, password, confirm_password):
        try:
            self.driver.get("https://eventhub.rahulshettyacademy.com/login")
            self.wait = WebDriverWait(self.driver, 10)
            self.wait.until(EC.element_to_be_clickable(self.register_but)).click()
            self.wait.until(EC.visibility_of_element_located(self.email_cli)).send_keys(email)
            self.wait.until(EC.visibility_of_element_located(self.password_cli)).send_keys(password)
            self.wait.until(EC.visibility_of_element_located(self.confirm_password_cli)).send_keys(confirm_password)
            self.wait.until(EC.element_to_be_clickable(self.click_but)).click()
            return "successfully registered"

        except TimeoutException:
            raise TimeoutException("Timed out waiting for page to load")



