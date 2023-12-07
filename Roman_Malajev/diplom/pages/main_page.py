import time

import allure
from selenium.common import NoSuchElementException

from Roman_Malajev.diplom.pages.base_page import BasePage

from Roman_Malajev.diplom.pages.locators import main_page_locators


class Header(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_page(self):
        with allure.step("Проверка перехода на главную страницу"):
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

            BasePage.check_elements_click(header_elements)

    def check_header_settings_items(self):
        with allure.step("Проверка элементов кнопки 'настройки'"):

            header_settings_elements = [
                main_page_locators.your_data_button,
                main_page_locators.theme_button,
                main_page_locators.language_button,
                main_page_locators.safemode_button,
                main_page_locators.country_button,
                main_page_locators.hotkeys_button,
                main_page_locators.inner_options_button,
                main_page_locators.inner_about_button,
                main_page_locators.inner_send_report_button
            ]

            self.is_element_visible(main_page_locators.options_button).click()

            BasePage.check_elements_click(header_settings_elements)



    def check_left_menu_items(self):
        with allure.step("Проверка элементов бокового меню"):
            left_menu_elements = [
                main_page_locators.history_button,
                main_page_locators.subscriptions_button,
                main_page_locators.shorts_button,
                main_page_locators.left_login_button,
                main_page_locators.main_button,
                main_page_locators.you_button,
                main_page_locators.trend_button,
                main_page_locators.music_button,
                main_page_locators.translations_button,
                main_page_locators.videogames_button,
                main_page_locators.sport_button,
                main_page_locators.catalogue_button,
                main_page_locators.premium_button,
                main_page_locators.yt_music_button,
                main_page_locators.yt_kids_button,
                main_page_locators.settings_button,
                main_page_locators.reports_button,
                main_page_locators.about_button,
                main_page_locators.send_report_button
            ]

            BasePage.check_elements_click(left_menu_elements)

    def check_categories_items(self):
        with allure.step("Проверка категорий"):
            categories_elements = [
                main_page_locators.categoria_rap_button,
                main_page_locators.categoria_music_button,
                main_page_locators.categoria_videogames_button,
                main_page_locators.categoria_streams_button,
                main_page_locators.categoria_sitcoms_button,
                main_page_locators.categoria_sketch_button,
                main_page_locators.categoria_animation_button,
                main_page_locators.categoria_action_and_adventures_button,
                main_page_locators.categoria_nature_button,
                main_page_locators.categoria_recently_published_button
            ]

            BasePage.check_elements_click(categories_elements)

    def check_videos_items(self):
        with allure.step("Проверка видео"):
            videos = self.driver.find_elements(main_page_locators.videos)
            videos_img = self.driver.find_elements(main_page_locators.videos_img)

            for video in videos[:10]:
                assert self.is_element_visible(video) is True
                    #self.driver.find_element(video).click()

            for video_img in videos_img[:10]:
                assert self.is_element_visible(video_img) is True
