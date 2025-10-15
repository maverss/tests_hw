from pages.webtables import WebTables
from components.components import WebElement
from selenium.common.exceptions import NoSuchElementException
import time
import pytest


@pytest.mark.parametrize('parametr', ['First Name', 'Last Name', 'Age', 'Email', 'Salary', 'Department', 'Action'])
def test_webtables(browser, parametr):
    web_tables = WebTables(browser)
    web_tables.visit()

    header_content = WebElement(
        browser,
        f"//div[@class='rt-resizable-header-content' and normalize-space(text())='{parametr}']",
        'xpath'
    )

    header_wrapper = WebElement(
        browser,
        f"//div[@role='columnheader'][.//div[@class='rt-resizable-header-content' and normalize-space(text())='{parametr}']]",
        'xpath'
    )

    try:
        header_content.find_element()
    except NoSuchElementException:
        pytest.fail(f"Заголовок '{parametr}' не найден на странице")

    assert header_content.find_element().text.strip() == parametr

    header_content.find_element().click()
    time.sleep(1)
    class_after_first_click = header_wrapper.find_element().get_attribute("class") or ""
    assert "-sort-asc" in class_after_first_click, f"После первого клика '{parametr}' не отсортирован по возрастанию"
    assert "-sort-desc" not in class_after_first_click

    header_content.find_element().click()
    time.sleep(1)
    class_after_second_click = header_wrapper.find_element().get_attribute("class") or ""
    assert "-sort-desc" in class_after_second_click, f"После второго клика '{parametr}' не отсортирован по убыванию"
    assert "-sort-asc" not in class_after_second_click