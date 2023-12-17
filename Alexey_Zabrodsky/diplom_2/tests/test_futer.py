import time
import pytest_check as check
import allure

from Alexey_Zabrodsky.diplom_2.pages.locators.header_page_locators import HeaderBtn
from Alexey_Zabrodsky.diplom_2.conftest import web_browser


@allure.feature('Смоук тест')
@allure.story('Имитация скролла в низ экрана и нажатия кнопок футера')
def test_header_btn(web_browser):
    """ Убеждаемся, что ссылки/кнопки футера
        кликабельные и переход на страницу корректный. """

    page = HeaderBtn(web_browser)

    with allure.step("Проверка кнопки 'О магазине'"):
        if check.equal(page.button_o_magazine.get_text(), 'О магазине'):
            check.equal(page.button_o_magazine.get_attribute('href'), 'https://www.dollar.by/about')
            page.button_o_magazine.click(1)
            page1 = page.get_current_url()
            check.equal(page1, page.get_current_url())
            check.is_true(page.button_o_magazine.wait_for_visibility())
            check.is_true(page.button_o_magazine.wait_to_be_clickable())

    with allure.step("Проверка кнопки 'Доставка и оплата'"):
        if check.equal(page.button_dostavka_i_oplata.get_text(), 'Доставка и оплата'):
            check.equal(page.button_dostavka_i_oplata.get_attribute('href'), 'https://www.dollar.by/orders')
            page.button_dostavka_i_oplata.click(1)
            page1 = page.get_current_url()
            check.equal(page1, page.get_current_url())
            check.is_true(page.button_dostavka_i_oplata.wait_for_visibility())
            check.is_true(page.button_dostavka_i_oplata.wait_to_be_clickable())
