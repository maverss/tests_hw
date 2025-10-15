from pages.webtables import WebTables
import time
from selenium.webdriver.common.keys import Keys


def test_webtables(browser):
    web_tables = WebTables(browser)
    web_tables.visit()

    web_tables.btn_add.click()

    web_tables.full_name.send_keys('alex')
    web_tables.last_name.send_keys('xela')
    web_tables.user_email.send_keys('name@example.com')
    web_tables.age.send_keys('21')
    web_tables.salary.send_keys('20000')
    web_tables.department.send_keys('Department')
    web_tables.btn_submit.click()

    time.sleep(2)
    
    web_tables.btn_edit.click()

    time.sleep(2)

    web_tables.age.clear()
    web_tables.age.send_keys('30')
    web_tables.btn_submit.click()

    time.sleep(2)

    while web_tables.btn_delete.exist() is True:
        web_tables.btn_delete.click()

    time.sleep(2)
    
    assert web_tables.no_data.exist()

def test_webtables_2(browser):
    web_tables = WebTables(browser)
    web_tables.visit()

    web_tables.select_rows_count.scroll_to_element()
    web_tables.select_rows_count.click()
    web_tables.select_rows_count.send_keys(Keys.PAGE_UP)
    web_tables.select_rows_count.send_keys(Keys.ENTER)

    for i in range(3):
        web_tables.btn_add.click()

        web_tables.full_name.send_keys('alex')
        web_tables.last_name.send_keys('xela')
        web_tables.user_email.send_keys('name@example.com')
        web_tables.age.send_keys('21')
        web_tables.salary.send_keys('20000')
        web_tables.department.send_keys('Department')
        web_tables.btn_submit.click()

    time.sleep(2)

    assert web_tables.page_total_count.get_text() == '2'

    web_tables.btn_next.click()

    time.sleep(2)

    assert web_tables.page_number.get_dom_attribute('value') == '2'

    web_tables.btn_previous.click()

    time.sleep(2)

    assert web_tables.page_number.get_dom_attribute('value') == '1'