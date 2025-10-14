'''
from pages.automation_practice_form import AutomationPracticeForm


def test_modal_elements(browser):
    automation_practice_form = AutomationPracticeForm(browser)
    automation_practice_form.visit()

    automation_practice_form.state.click()
    automation_practice_form.haryana.click()
    automation_practice_form.city.click()
    automation_practice_form.karnal.click()

    assert automation_practice_form.haryana.get_text() == 'Haryana'
    assert automation_practice_form.karnal.get_text() == 'Karnal'
'''