import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options

import pytest_check as check


def test_classwork5():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://demoqa.com/")
    time.sleep(2)

    elements1 = driver.find_element(By.XPATH, '(//div[@class="card mt-4 top-card"]//h5)[1]')
    elements2 = driver.find_element(By.XPATH, '(//div[@class="card mt-4 top-card"]//h5)[2]')
    elements3 = driver.find_element(By.XPATH, '(//div[@class="card mt-4 top-card"]//h5)[3]')
    elements4 = driver.find_element(By.XPATH, '(//div[@class="card mt-4 top-card"]//h5)[4]')
    elements5 = driver.find_element(By.XPATH, '(//div[@class="card mt-4 top-card"]//h5)[5]')


# Проверяет текст в сравнении!!!
    elements = [
        (elements1.text, 'Elements', 'Неверный текст первого элемента'),
        (elements2.text, 'Forms', 'Неверный текст второй элемент'),
        (elements3.text, 'Alerts, Frame & Windows', 'Неверный текст трейтий элемент'),
        (elements4.text, 'Widgets', 'Неверный текст четвертый элемент'),
        (elements5.text, 'Interactions', 'Неверный текст пятый элемент'),

    ]
    for pervu, vtoroi, treti in elements:
        check.equal(pervu, vtoroi, treti)

# Проверяет отображается ли!!!
    elements = [
        (elements1.is_displayed(), 'Неверный текст первого элемента'),
        (elements2.is_displayed(), 'Неверный текст второй элемент'),
        (elements3.is_displayed(), 'Неверный текст трейтий элемент'),
        (elements4.is_displayed(), 'Неверный текст четвертый элемент'),
        (elements5.is_displayed(), 'Неверный текст пятый элемент'),

    ]
    for pervu, vtoroi in elements:
        check.is_true(pervu, vtoroi)

# elements = [
#         (elements1.text, 'Elements', 'Неверный текст первого элемента'),
#         (elements2.text, 'Forms', 'Неверный текст второй элемент'),
#         (elements3.text, 'Alerts, Frame & Windows', 'Неверный текст трейтий элемент'),
#         (elements4.text, 'Widgets', 'Неверный текст четвертый элемент'),
#         (elements5.text, 'Interactions', 'Неверный текст пятый элемент'),
#     ]
# for pervu, vtoroi, treti  in elements:
#     if check.is_true(pervu, vtoroi)





