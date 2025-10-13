from pages.base_page import BasePage
from components.components import WebElement
from selenium.webdriver.common.by import By


class DemoQa(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)