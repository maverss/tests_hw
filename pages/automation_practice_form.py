from pages.base_page import BasePage
from components.components import WebElement


class AutomationPracticeForm(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.btn_submit = WebElement(driver, '#submit')

        self.user_form = WebElement(driver, '#userForm')

        self.state= WebElement(driver, '#state')
        self.city = WebElement(driver, '#city')
        self.haryana = WebElement(driver, '#state > div > div.css-1hwfws3 > div.css-1uccc91-singleValue')
        self.karnal = WebElement(driver, '#city > div > div.css-1hwfws3 > div.css-1uccc91-singleValue')

        