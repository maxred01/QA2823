from selenium.common import NoSuchElementException
from Alexey_Zabrodsky.diplom.pages.base_page import BasePage
from Alexey_Zabrodsky.diplom.pages.locators import home_page_locators
import allure


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        with allure.step("Перейти на главную страницу"):
            self.driver.get('https://www.dollar.by/')

    def click_header_o_magazine(self):
        with allure.step("Проверка ссылки о магазине"):
            get_url1 = self.driver.current_url
            self.driver.find_element(home_page_locators.button_o_magazine).click()
            get_url2 = self.driver.current_url
            return [get_url1, get_url2]

