from pages.modal_dialogs import ModalDialogs
import time


def test_check_modal(browser):
    modal_dialogs = ModalDialogs(browser)
    modal_dialogs.visit()
    
    modal_dialogs.btn_small_modal.click()
    assert modal_dialogs.modal_content.exist()
    modal_dialogs.btn_close.click()
    assert not modal_dialogs.modal_content.exist()

    time.sleep(2)

    modal_dialogs.btn_large_modal.click()
    assert modal_dialogs.modal_content.exist()
    modal_dialogs.btn_close.click()
    assert not modal_dialogs.modal_content.exist()