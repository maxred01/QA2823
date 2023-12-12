# import allure
# from selenium.common import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains

# 1. allure - библиотека для создания отчетов и документации о тестировании.
# Она используется для создания красивых отчетов о пройденных тестах,
# включая скриншоты и описания процесса тестирования.
# 2. selenium.common.TimeoutException - исключение, которое возникает,
# когда таймаут истекает в Selenium WebDriver.
# Оно используется для обработки исключений при работе с WebDriver и ожидании элементов на странице.
# 3. selenium.webdriver.chrome.webdriver.
# WebDriver - класс для создания экземпляра веб-драйвера для браузера Google Chrome.
# Он используется для создания экземпляра WebDriver для автоматизации действий в браузере.
# 4. selenium.webdriver.support.ui.WebDriverWait - класс для ожидания элементов на странице
# в Selenium WebDriver. Он используется для задания таймаута и повторения попыток до тех пор,
# пока элемент не будет найден на странице.
# 5. selenium.webdriver.support.expected_conditions - модуль с ожидаемыми условиями
# в Selenium WebDriver. Он используется для проверки наличия определенных элементов на странице,
# проверки их видимости, доступности и других свойств.
# 6. selenium.webdriver.common.action_chains.ActionChains - класс для создания цепочки действий
# в Selenium WebDriver. Он используется для создания последовательности действий, таких как клики,
# наведение курсора, перетаскивание элементов и других событий.


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, *args):
        by_name, by_val = args[0]
        return self.driver.find_element(by_name, by_val)
    """ Метод find_element() принимает два аргумента:
                by_name и by_val, которые определяют, как искать
                элемент на странице. Метод использует self.driver
                для поиска элемента на странице и возвращает найденный элемент"""

    def element_is_visible(self, *args):
        by_name, by_val = args[0]
        return wait(
            self.driver, timeout=10).until(EC.visibility_of_element_located((by_name, by_val))
        )
    """Метод elements_is_visible() использует WebDriverWait для ожидания видимости
            элемента на странице в течение 10 секунд, после чего
            он возвращает найденный элемент. Если элемент не появляется
            на странице в течение 10 секунд, возникает исключение TimeoutException"""

    def elements_are_visible(self, *args):
        by_name, by_val = args[0]
        return wait(
            self.driver, timeout=10).until(EC.visibility_of_all_elements_located((by_name, by_val))
                                           )
    """Метод elements_is_visible() использует WebDriverWait для ожидания видимости
                элемента на странице в течение 10 секунд, после чего
                он возвращает найденный элемент. Если элемент не появляется
                на странице в течение 10 секунд, возникает исключение TimeoutException"""