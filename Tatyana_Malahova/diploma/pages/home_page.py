import time

from selenium.common import NoSuchElementException
# from selenium.webdriver import ActionChains

from Tatyana_Malahova.diploma.pages.base_page import BasePage
from Tatyana_Malahova.diploma.pages.locators import autorization_page_locators
import allure
from selenium.webdriver.common.action_chains import ActionChains


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        with allure.step("Перейти на главную страницу"):
            self.driver.get('https://www.zalando.pl/kobiety-home/')

    def go_to_login_screen(self):
        with allure.step("Нажать кнопку войти на главном экране"):
            actions = ActionChains(self.driver)
            actions.move_to_element(autorization_page_locators.picture_autorization)
            time.sleep(2)
            actions.click(autorization_page_locators.log_in_in_window)
            actions.perform()

    def fill_login_inputs_valid_data_and_submit(self):
        with allure.step("Заполнить поле логин"):
            self.find_element(autorization_page_locators.e_mail_address_second).send_keys("something_email@mail.com")
        with allure.step("Заполнить поле пароль"):
            self.find_element(autorization_page_locators.password_second).send_keys("qwertyui1278")
        with allure.step("Нажать кнопку войти"):
            self.find_element(autorization_page_locators.log_in).click()
