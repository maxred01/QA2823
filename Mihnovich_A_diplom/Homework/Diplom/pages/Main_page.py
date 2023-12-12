import allure
import requests
from Mihnovich_A_diplom.Homework.Diplom.pages.locators import main_page_locators
from Mihnovich_A_diplom.Homework.Diplom.pages.Base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        with allure.step('Перейти на главную страницу'):
            self.driver.get('https://www.whitehouse.gov/')

    def check_displayed_administration(self):
        with allure.step('Проверить видимость кнопки Administration'):
            assert self.find_element(main_page_locators.ADMINISTRATION).is_displayed()

    def check_link_administration(self):
        with allure.step('Проверить ссылку на страницу Administration'):
            adm = self.element_is_visible(main_page_locators.ADMINISTRATION)
            link_adm = adm.get_attribute('href')
            request = requests.get(link_adm)
            if request.status_code == 200:
                adm.click()
                current_url = self.driver.current_url
                return link_adm, current_url
            else:
                return request.status_code

    def check_displayed_priorities(self):
        with allure.step('Проверить видимость кнопки Priorities'):
            assert self.find_element(main_page_locators.PRIORITIES).is_displayed()

    def check_link_priorities(self):
        with allure.step('Проверить ссылку на страницу Priorities'):
            element = self.element_is_visible(main_page_locators.PRIORITIES)
            link = element.get_attribute('href')
            request = requests.get(link)
            if request.status_code == 200:
                element.click()
                current_url = self.driver.current_url
                return link, current_url
            else:
                return request.status_code

    def check_displayed_record(self):
        with allure.step('Проверить видимость кнопки The_record'):
            assert self.find_element(main_page_locators.THE_RECORD).is_displayed()

    def check_link_record(self):
        with allure.step('Проверить ссылку на страницу The_record'):
            element = self.element_is_visible(main_page_locators.THE_RECORD)
            link = element.get_attribute('href')
            request = requests.get(link)
            if request.status_code == 200:
                element.click()
                current_url = self.driver.current_url
                return link, current_url
            else:
                return request.status_code

    def check_displayed_briefing(self):
        with allure.step('Проверить видимость кнопки Briefing'):
            assert self.find_element(main_page_locators.BRIEFING).is_displayed()

    def check_link_briefing(self):
        with allure.step('Проверить ссылку на страницу Briefing'):
            element = self.element_is_visible(main_page_locators.BRIEFING)
            link = element.get_attribute('href')
            request = requests.get(link)
            if request.status_code == 200:
                element.click()
                current_url = self.driver.current_url
                return link, current_url
            else:
                return request.status_code

    def check_displayed_menu_button(self):
        with allure.step('Проверить видимость кнопки MENU'):
            assert self.find_element(main_page_locators.MENU_BUTTON).is_displayed()

    def click_menu_button(self):
        with allure.step('Нажать кнопку MENU'):
            self.element_is_visible(main_page_locators.MENU_BUTTON).click()

    def check_displayed_logo(self):
        with allure.step('Проверить видимость логотипа'):
            assert self.find_element(main_page_locators.TITLE_LOGO).is_displayed()

    def check_logo(self):
        with allure.step('Проверить что логотип возвращает на главную страницу'):
            main_url = self.driver.current_url
            element = self.element_is_visible(main_page_locators.TITLE_LOGO)
            link = element.get_attribute('href')
            request = requests.get(link)
            if request.status_code == 200:
                element.click()
                current_url = self.driver.current_url
                return main_url, current_url
            else:
                return request.status_code

