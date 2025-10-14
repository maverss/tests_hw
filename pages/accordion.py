from pages.base_page import BasePage
from components.components import WebElement


class Accordion(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.card_body_section1Content = WebElement(driver, '#section1Content > p')
        self.card_header_section1Content = WebElement(driver, '#section1Heading')

        self.card_body_section2Content_1 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.card_body_section2Content_2 = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.card_body_section3Content = WebElement(driver, '#section3Content > p')