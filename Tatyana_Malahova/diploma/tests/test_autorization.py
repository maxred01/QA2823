import pytest

from Tatyana_Malahova.diploma.pages.home_page import HomePage
# from class_work.diplom.pages.profile_page import ProfilePage
import allure
from Tatyana_Malahova.diploma.conftest import driver


@pytest.mark.presentation
@pytest.mark.non_multiple_CPUs_run
@allure.suite("Авторизация")
@allure.title("Авторизация с валидными данными")
def test_login(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.go_to_login_screen()
    home_page.fill_login_inputs_valid_data_and_submit()
#    profile_page = ProfilePage(driver)
#    assert profile_page.check_for_my_orders_tab_on_page(), "Вы не авторизовались"
