from selenium.webdriver.common.by import By
from components.components import WebElement


class BasePage():

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def visit(self):
        return self.driver.get(self.base_url)

    def get_text(self, locator):
        element = self.driver.find_element(By.CSS_SELECTOR, locator)
        return element.text