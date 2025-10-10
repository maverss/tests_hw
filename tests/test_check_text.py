from pages.demoqa import DemoQa
from pages.elements_page import ElementPage

def test_go_to_page_elements(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementPage(browser)
    
    demo_qa_page.visit()
    assert demo_qa_page.get_text('span') == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'

    elements_page.visit()
    assert elements_page.get_text('#app > div > div > div > div:nth-child(2)') == 'Please select an item from left to start practice.'