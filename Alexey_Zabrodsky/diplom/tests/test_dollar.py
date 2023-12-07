import pytest
import pytest_check as check
from Alexey_Zabrodsky.diplom.pages.home_page import HomePage
from Alexey_Zabrodsky.diplom.conftest import driver
import allure


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Правовая информация'")
def test_link_header(driver):
    page = HomePage(driver)
    page.open()
    page.go_to()
    page.check_for_url_is_changed(page.get_current_url(), 'https://www.dollar.by/about')
