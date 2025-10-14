from pages.elements_page import ElementPage
from components.components import WebElement
import time

'''
def test_visible_sidebar(browser):
    elements_page = ElementPage(browser)
    btn_sidebar_first_textbox = WebElement('div:nth-child(1) > div > ul > #item-0 > span')

    elements_page.visit()
    assert elements_page.btn_sidebar_first_textbox.visible()
'''
'''
def test_not_visible_sidebar(browser):
    elements_page = ElementPage(browser)
    btn_sidebar_first_textbox = WebElement('div:nth-child(1) > div > ul > #item-0 > span')

    elements_page.visit()
    assert elements_page.btn_sidebar_first_checkbox.visible()
    elements_page.btn_sidebar_first.click()
    time.sleep(2)
    assert not elements_page.btn_sidebar_first_checkbox.visible()
'''