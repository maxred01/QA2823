import pytest
import allure
from Mihnovich_A_diplom.Homework.Diplom.pages.Main_page import MainPage


@pytest.mark.presentation
@pytest.mark.non_multiple_CPUs_run
@allure.suite("Авторизация")
@allure.title("Авторизация с валидными данными")
def test_elem_displayed(driver):
    main_page = MainPage(driver)
    main_page.open()
    assert main_page.check_displayed_administration() == True
