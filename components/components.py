from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class WebElement:
    def __init__(self, driver, locator=''):
        self.driver = driver
        self.locator = locator

    def get_text(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator).text

    def find_element(self, locator):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def find_elements(self, locator):
        return self.driver.find_elements(By.CSS_SELECTOR, self.locator)

    def exist(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, self.locator)
            return 'Element found'
        except NoSuchElementException:
            return 'No element'

    def click(self):
        self.driver.find_element(By.CSS_SELECTOR, self.locator).click()
    
    def visible(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator).is_displayed()

    def check_count_elements(self, count: int) -> bool:
        if len(self.find_elements(self.locator)) == count:
            return True
        return False