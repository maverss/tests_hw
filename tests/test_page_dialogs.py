from pages.modal_dialogs import ModalDialogs
from pages.demoqa import DemoQa


def test_modal_elements(browser):
    modal_dialogs = ModalDialogs(browser)
    modal_dialogs.visit()

    assert modal_dialogs.btns_under_menu.check_count_elements(count = 5)

def test_navigation_modal(browser):
    modal_dialogs = ModalDialogs(browser)
    demoqa_page = DemoQa(browser)
    modal_dialogs.visit()
    
    browser.refresh()
    modal_dialogs.icon.click()

    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()

    assert demoqa_page.equal_url()

    assert browser.title == 'DEMOQA'

    browser.set_window_size(1000, 1000)
