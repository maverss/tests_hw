from pages.base_page import BasePage
from components.components import WebElement


class ModalDialogs(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btns_under_menu = WebElement(driver, '#app > div > div > div > div:nth-child(1) > div > div > div:nth-child(3) > div > ul > li')
        self.icon = WebElement(driver, '#app > header > a > img')

        self.btn_small_modal = WebElement(driver, '#showSmallModal')
        self.btn_large_modal = WebElement(driver, '#showLargeModal')
        self.btn_close = WebElement(driver, 'body > div.fade.modal.show > div > div > div.modal-footer > button')
        self.modal_content = WebElement(driver, 'body > div.fade.modal.show > div > div')
        