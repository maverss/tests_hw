from pages.automation_practice_form import AutomationPracticeForm


def test_modal_elements(browser):
    automation_practice_form = AutomationPracticeForm(browser)
    automation_practice_form.visit()

    assert automation_practice_form.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert automation_practice_form.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert automation_practice_form.user_email.get_dom_attribute('placeholder') == 'name@example.com'
    assert automation_practice_form.user_email.get_dom_attribute('pattern') == r"^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$"

    automation_practice_form.btn_submit.click()

    assert automation_practice_form.user_form.get_dom_attribute('class') == 'was-validated'