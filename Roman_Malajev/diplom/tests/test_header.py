import pytest

from class_work.diplom.pages.cart_page import CartPage
from class_work.diplom.pages.feedback_page import FeedbackPage
from class_work.diplom.pages.home_page import HomePage
from class_work.diplom.pages.profile_page import ProfilePage
import allure


@pytest.mark.presentation
@pytest.mark.non_multiple_CPUs_run
@allure.suite("Авторизация")
@allure.title("Авторизация с валидными данными")
def test_login(driver):
    home_page = HomePage(driver)