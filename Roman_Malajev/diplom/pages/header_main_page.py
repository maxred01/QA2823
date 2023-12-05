import time

import allure
from selenium.common import NoSuchElementException

from Roman_Malajev.diplom.pages.base_page import BasePage

from Roman_Malajev.diplom.pages.locators import main_page_locators


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_page(self):
        self.driver.get('https://www.youtube.com/')

    def check_header_items(self):
        with allure.step("Проверка элементов хэдэра"):

            header_elements = [
                main_page_locators.search_field,
                main_page_locators.search_button,
                main_page_locators.burger_button,
                main_page_locators.keyboard_button,
                main_page_locators.options_button,
                main_page_locators.header_login_button,
                main_page_locators.voice_search_button
            ]

            for element in header_elements:
                if self.is_element_visible(element):
                    self.driver.find_element(element).click()

    def check_header_settings_items(self):
        with allure.step("Проверка элементов кнопки 'настройки'"):
            header_settings_elements = [

            ]

    def check_left_menu_items(self):
        with allure.step("Проверка элементов бокового меню"):
            left_menu_elements = [

            ]

    def check_categories_items(self):
        with allure.step("Проверка категорий"):
            categories_elements = [

            ]

    def check_videos_items(self):
        with allure.step("Проверка видео"):
            pass