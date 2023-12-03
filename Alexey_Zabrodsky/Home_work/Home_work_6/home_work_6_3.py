import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest_check as check


CREATED = 'https://demoqa.com/created'
NO_CONTENT = 'https://demoqa.com/no-content'
MOVED = 'https://demoqa.com/moved'
BAD_REQUEST = 'https://demoqa.com/bad-request'
UNAUTHORIZED = 'https://demoqa.com/unauthorized'
FORBIDDEN = 'https://demoqa.com/forbidden'
NOT_FOUND = 'https://demoqa.com/invalid-url'


def test_homework6_check_links():

    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get('https://demoqa.com/links')
    driver.implicitly_wait(5)
    driver.execute_script('window.scrollBy(0,300)')

    links_url = [CREATED, NO_CONTENT, MOVED, BAD_REQUEST, UNAUTHORIZED, FORBIDDEN, NOT_FOUND]
    links_url_data = {}

    driver.implicitly_wait(5)
    links = driver.find_elements(By.CSS_SELECTOR, '[href="javascript:void(0)"]')
    links_data = {}

    for i in range(7):
        link_url = links_url[i]
        response = requests.get(link_url)
        links_url_data['status_actual'] = response.status_code
        links_url_data['reason_actual'] = response.reason

        link = links[i]
        link.click()
        time.sleep(0.5)
        value = driver.find_element(By.XPATH, '//p[@id="linkResponse"]//b[1]').text
        links_data['status_expected'] = int(value)
        links_data['reason_expected'] = driver.find_element \
            (By.XPATH, '//p[@id="linkResponse"]//b[2]').text
        time.sleep(0.5)

        check.equal(
            links_url_data['status_actual'],
            links_data['status_expected'],
            'Статус отличается'
        )
        check.equal(
            links_url_data['reason_actual'],
            links_data['reason_expected'],
            'Описание статуса отличается'
        )

    driver.close()
