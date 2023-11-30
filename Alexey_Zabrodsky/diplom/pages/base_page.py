import allure
from selenium.common import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Alexey_Zabrodsky.diplom.pages.locators import base_page_locators


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_visible(self, *args):
        by_name, by_val = args[0]
        return self.driver.find_element(by_name, by_val)
# Для поиска элемента на странице и возвращает найденный элемент

    def is_element_visible(self, *args):
        by_name, by_val = args[0]
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((by_name, by_val))
        )
        return self.driver.find_element(by_name, by_val)
# Для ожидания видимости элемента на странице в течение 10 секунд

    def is_not_element_present(self, *args):
        try:
            by_name, by_val = args[0]
            WebDriverWait(self.driver, 10).until_not(
                EC.presence_of_element_located((by_name, by_val)),
            )
        except TimeoutException:
            return False
        return True
# Для ожидания отсутствия элемента Если элемент не появляется на странице в течение 10 секунд, метод
# возвращает True. Если элемент все же появляется, возникает исключение
# TimeoutException, и метод возвращает False

    def is_element_present(self, *args):
        try:
            by_name, by_val = args[0]
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((by_name, by_val)),
            )
        except TimeoutException:
            return False
        return True
# Для ожидания появления элемента Если элемент
# появляется на странице в течение 10 секунд, метод возвращает True.
# Если элемент не появляется, возникает исключение TimeoutException,
# и метод возвращает False

    def find_elements(self, *args):
        by_name, by_val = args[0]
        return self.driver.find_elements(by_name, by_val)
# Находит все элементы на странице,
# соответствующие заданным параметрам поиска

    def go_to_main_page(self):
        self.is_element_visible(base_page_locators.header_logo).click()
# Метод go_to_main_page() переходит на главную страницу.
# Метод использует метод is_element_visible() для поиска
# элемента с логотипом на странице и кликает на него.
# Метод is_element_visible() ожидает, что элемент с
# логотипом появится на странице и станет видимым в течение 10 секунд.
# Если элемент не появляется на странице в течение 10 секунд,
# возникает исключение TimeoutException

    def get_current_url(self):
        return self.driver.current_url
# Возвращает текущий URL-адрес страницы