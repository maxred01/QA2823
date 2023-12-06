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

    def go_to(self):
        with allure.step("Нажать кнопку войти на главном экране"):
            self.find_element(home_page_locators.button_o_magazine).click()



