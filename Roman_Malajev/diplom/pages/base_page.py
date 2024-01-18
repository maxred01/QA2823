import time
from urllib.parse import urlparse
import allure
import requests
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def check_button_text(self, locator, expected_value):
        actual_value = self.driver.find_element(*locator).text
        if actual_value == expected_value:
            pass
        else:
            raise ValueError(f"тексты кнопок не совпадают actual:{actual_value}, expected:{expected_value}")

    def check_placeholder(self, locator,  expected_value):
        actual_value = self.driver.find_element(*locator).get_attribute("placeholder")
        if actual_value == expected_value:
            pass
        else:
            raise ValueError(f"placeholder'ы не совпадают actual:{actual_value}, expected:{expected_value}")

    def check_headers_yt(self, url, headers, payload):
        with allure.step('Проверка скорости ответа сервера'):
            start_time = time.time()
            response = requests.request("POST", url, headers=headers, data=payload)
            end_time = time.time()
            final_time = end_time - start_time
            assert final_time < 1

        with allure.step("API Проверка статус кода"):
            assert response.status_code == 200

        with allure.step("API Проверка значения параметра Content-Type"):
            assert response.headers['Content-Type'] == 'application/json; charset=UTF-8'

        with allure.step("API Проверка значения параметра Server"):
            assert response.headers['Server'] == 'scaffolding on HTTPServer2'

        with allure.step("API Проверка значения параметра Cache-Control"):
            assert response.headers['Cache-Control'] == 'private'

        with allure.step("API Проверка значения параметра X-XSS-Protection"):
            assert response.headers['X-XSS-Protection'] == '0'

        with allure.step("API Проверка значения параметра X-Frame-Options"):
            assert response.headers['X-Frame-Options'] == 'SAMEORIGIN'

        with allure.step("API Проверка значения параметра X-Content-Type-Options"):
            assert response.headers['X-Content-Type-Options'] == 'nosniff'

    def wait_for_page_to_load(self, driver, timeout=10):
        WebDriverWait(driver, timeout).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*"))
        )

    def get_domain(self, url):
        parsed_url = urlparse(url)
        return parsed_url.netloc

    def compare_domains(self, def_url, cur_url):
        def_domain = self.get_domain(def_url)
        cur_domain = self.get_domain(cur_url)
        if def_domain == cur_domain:
            return True

    def wait_for_element_visibility(self, locator):
        try:
            return WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            return False

    def find_and_click_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element.click()

    def check_elements(self, *args):
        element = args
        for elem in element:
            assert self.driver.find_element(elem).is_displayed() is True

    def check_elements_click(self, arg):
        elements = arg
        for element in elements:
            time.sleep(1)
            if self.driver.find_element(*element).is_displayed():
                time.sleep(1)
                self.driver.find_element(*element).click()

    def find_element(self, *args):
        by_name, by_val = args
        try:
            return self.driver.find_element(by_name, by_val).is_displayed()
        except NoSuchElementException:
            return False

    def is_not_element_present(self, *args):
        try:
            by_name, by_val = args[0]
            WebDriverWait(self.driver, 10).until_not(
                EC.presence_of_element_located((by_name, by_val)),
            )
        except TimeoutException:
            return False
        return True

    def is_element_present(self, *args):
        try:
            by_name, by_val = args[0]
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((by_name, by_val)),
            )
        except TimeoutException:
            return False
        return True

    def get_current_url(self):
        return self.driver.current_url

    def is_elements_text_equal_to(self, *args, element_text):
        try:
            by_name, by_val = args[0]
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element((by_name, by_val), element_text),
            )
        except TimeoutException:
            return False
        return True

    def drag_and_drop_from_right_to_left(self, source, x_offset=0, y_offset=0):
        source_web_element = self.find_element(source)
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(source_web_element, x_offset, y_offset).perform()

    def check_for_url_is_changed(self, current_url, url_that_should_be):
        with allure.step(f"Проверяем, что текущий url равен {url_that_should_be}"):
            assert current_url == url_that_should_be