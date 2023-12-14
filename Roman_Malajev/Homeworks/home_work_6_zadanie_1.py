from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest_check as check


def test_homework6_yes_button():

    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get('https://demoqa.com/radio-button')
    driver.implicitly_wait(5)
    driver.find_element(By.CSS_SELECTOR, '[for="yesRadio"]').click()
    driver.implicitly_wait(5)
    yes_button = driver.find_element(By.CSS_SELECTOR, '[id="yesRadio"]')
    check.is_true(yes_button.is_selected(), 'Кнопка не выбрана')

    driver.close()


def test_homework6_impressive_button():

    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get('https://demoqa.com/radio-button')
    driver.implicitly_wait(5)
    driver.find_element(By.CSS_SELECTOR, '[for="impressiveRadio"]').click()
    driver.implicitly_wait(5)
    impressive_button = driver.find_element(By.CSS_SELECTOR, '[id="impressiveRadio"]')
    check.is_true(impressive_button.is_selected(), 'Кнопка не выбрана')

    driver.close()
