from pages.text_box import TextBox


def test_modal_elements(browser):
    text_box = TextBox(browser)
    text_box.visit()

    text_box.name.send_keys('1111')
    text_box.current_address.send_keys('2222')
    text_box.btn_submit.click()

    assert('1111'in text_box.name_result.get_text() and '2222' in text_box.current_address_result.get_text())

