from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MallinatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait=WebDriverWait(driver,10)

    mallinator_button=(By.XPATH,"//a[@class='wp-block-button__link wp-element-button']")
    mallinator_email=(By.XPATH,"//div[@class='wrapper-primary-input medium-w100']//span")

#to open the mallinator webpage to store and the generate email
    def mallinator_generate_button(self):
        try:
            self.driver.get("https://www.mailinator.com/fake-email-generator/")
            self.wait=WebDriverWait(self.driver,10)
            self.wait.until(EC.element_to_be_clickable(self.mallinator_button)).click()
            email = self.wait.until(EC.visibility_of_element_located(self.mallinator_email))
            if not email:
                raise ValueError("Email not available")
            return email.text

        except TimeoutException:
            raise TimeoutException("Timed out waiting for page to load")


