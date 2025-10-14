from pages.accordion import Accordion
import time


def test_visible_accordion(browser):
    accordion = Accordion(browser)
    accordion.visit()

    assert accordion.card_body_section1Content.visible()
    accordion.card_header_section1Content.click()
    time.sleep(2)
    assert not accordion.card_body_section1Content.visible()

def test_visible_accordion_default(browser):
    accordion = Accordion(browser)
    accordion.visit()

    assert not accordion.card_body_section2Content_1.visible()
    assert not accordion.card_body_section2Content_2.visible()
    assert not accordion.card_body_section3Content.visible()