import allure
from selenium.common import NoSuchElementException

from Tatyana_Malahova.diploma.pages.base_page import BasePage

from Tatyana_Malahova.diploma.pages.locators import autorization_page_locators
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_item_in_cart(self):
        with allure.step("Проверка регистрации"):
            menu = self.find_element(autorization_page_locators.picture_autorization)
            ActionChains(self.driver).move_to_element(menu).click(autorization_page_locators.log_in_in_window).perform()

    def add_first_client(self):
        driver.find_element(By.XPATH, autorization_page_locators.register).click()
        driver.find_element(By.XPATH, autorization_page_locators.name).click()
        driver.find_element(By.XPATH, autorization_page_locators.name).send_keys('Tatyana')
        driver.find_element(By.XPATH, autorization_page_locators.name_continued).click()
        driver.find_element(By.XPATH, autorization_page_locators.name_continued).send_keys('Malahova')
        driver.find_element(By.XPATH, autorization_page_locators.e_mail_address_first).click()
        driver.find_element(By.XPATH, autorization_page_locators.e_mail_address_first).send_keys(
            'something_email@mail.com')
        driver.find_element(By.XPATH, autorization_page_locators.password_first).click()
        driver.find_element(By.XPATH, autorization_page_locators.password_first).send_keys('qwertyui1278')
        driver.find_element(By.XPATH, autorization_page_locators.agree_rules).click()
        driver.find_element(By.XPATH, autorization_page_locators.button_register).click()
