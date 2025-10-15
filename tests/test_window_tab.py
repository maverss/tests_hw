from pages.links import Links
import time


def test_links(browser):
    links = Links(browser)

    links.visit()

    assert links.btn_home.get_text() == 'Home'

    links.btn_home.click_force()

    time.sleep(4)

    browser.switch_to.window(browser.window_handles[1])

    assert browser.current_url == 'https://demoqa.com/'