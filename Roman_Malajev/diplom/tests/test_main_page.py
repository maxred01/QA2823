import time

import pytest

from Roman_Malajev.diplom.pages.main_page import Header
import allure
from Roman_Malajev.diplom.conftest import driver


@pytest.mark.presentation
@pytest.mark.non_multiple_CPUs_run
@allure.suite("Header")
@allure.title("Проверка элементов хедэра")
def test_header(driver):
    main_page = Header(driver)
    main_page.open_page()
    main_page.check_videos_items()