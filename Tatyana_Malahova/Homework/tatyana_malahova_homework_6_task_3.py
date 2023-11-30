import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest_check as check

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/links")

element1 = driver.find_element(By.XPATH, "//*[@id='created']")
element2 = driver.find_element(By.XPATH, "//*[@id='no-content']")
element3 = driver.find_element(By.XPATH, "//*[@id='moved']")
element4 = driver.find_element(By.XPATH, "//*[@id='bad-request']")
element5 = driver.find_element(By.XPATH, "//*[@id='unauthorized']")
element6 = driver.find_element(By.XPATH, "//*[@id='forbidden']")
element7 = driver.find_element(By.XPATH, "//*[@id='invalid-url']")


def test_task_3():
    elements = [
        (element1, '201', 'Created'),
        (element2, '204', 'No Content'),
        (element3, '301', 'Moved Permanently'),
        (element4, '400', 'Bad Request'),
        (element5, '401', 'Unauthorized'),
        (element6, '403', 'Forbidden'),
        (element7, '404', 'Not Found'),

    ]
    for element, code, text in elements:
        driver.find_element(By.XPATH, "//body").send_keys(Keys.END)
        element.click()
        time.sleep(2)
        b1 = driver.find_element(By.XPATH, "(//p[@id='linkResponse']//b)[1]")
        b2 = driver.find_element(By.XPATH, "(//p[@id='linkResponse']//b)[2]")
        check.equal(b1.text, code)
        check.equal(b2.text, text)
