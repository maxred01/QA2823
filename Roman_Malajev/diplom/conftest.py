import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest, requests, logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import base64
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.proxy import *


@pytest.fixture(scope='function')
def driver():
    options = Options()
    # Опция для отключения GPU (графический процессор)
    options.add_argument("--disable-gpu")
    # Опция для отключения уведомлений в браузере
    options.add_argument("--disable-notifications")
    # Опция для отключения отображения курсора
    options.add_argument("--hide-scrollbars")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    # Принятие недоверенных сертификатов (если такие будут обнаружены)
    driver.accept_untrusted_certs = True
    driver.implicitly_wait(10)
    # Возвращение объекта драйвера для использования в тестах
    yield driver
    driver.quit()
