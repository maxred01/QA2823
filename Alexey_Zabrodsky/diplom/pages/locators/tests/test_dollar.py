import pytest
import pytest_check as check
from Alexey_Zabrodsky.diplom.pages.home_page import HomePage

import allure
from Alexey_Zabrodsky.diplom.conftest import driver


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Правовая информация'")
def test_link_header(driver):
    page = HomePage(driver)
    page.open()
    check.equal(page.click_header_o_magazine(), "12321321")

