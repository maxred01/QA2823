from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest_check as check


def test_homework6_change_table():

    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get('https://demoqa.com/webtables')
    driver.implicitly_wait(5)

    old_first_name = driver.find_element(By.XPATH, '(//div[@class="rt-tr-group"]//div[@class="rt-td"])[1]').text
    old_last_name = driver.find_element(By.XPATH, '(//div[@class="rt-tr-group"]//div[@class="rt-td"])[2]').text
    old_age = driver.find_element(By.XPATH, '(//div[@class="rt-tr-group"]//div[@class="rt-td"])[3]').text
    old_email = driver.find_element(By.XPATH, '(//div[@class="rt-tr-group"]//div[@class="rt-td"])[4]').text
    old_salary = driver.find_element(By.XPATH, '(//div[@class="rt-tr-group"]//div[@class="rt-td"])[5]').text
    old_department = driver.find_element(By.XPATH, '(//div[@class="rt-tr-group"]//div[@class="rt-td"])[6]').text

    old_data = [old_first_name, old_last_name, old_email, old_age, old_salary, old_department]

    driver.find_element(By.CSS_SELECTOR, '[id="edit-record-1"]').click()
    driver.implicitly_wait(5)

    new_first_name = 'duvdfivb'
    new_last_name = 'sdfsdsdfsdf'
    new_email = 'aasdas@aiodjasiod.com'
    new_age = '99'
    new_salary = '1000000'
    new_department = 'egfefefesd'

    new_data = [new_first_name, new_last_name, new_email, new_age, new_salary, new_department]

    first_name = driver.find_element(By.CSS_SELECTOR, '[id="firstName"]')
    first_name.clear()
    first_name.send_keys(new_first_name)
    driver.implicitly_wait(5)
    last_name = driver.find_element(By.CSS_SELECTOR, '[id="lastName"]')
    last_name.clear()
    last_name.send_keys(new_last_name)
    driver.implicitly_wait(5)
    email = driver.find_element(By.CSS_SELECTOR, '[id="userEmail"]')
    email.clear()
    email.send_keys(new_email)
    driver.implicitly_wait(5)
    age = driver.find_element(By.CSS_SELECTOR, '[id="age"]')
    age.clear()
    age.send_keys(new_age)
    driver.implicitly_wait(5)
    salary = driver.find_element(By.CSS_SELECTOR, '[id="salary"]')
    salary.clear()
    salary.send_keys(new_salary)
    driver.implicitly_wait(5)
    department = driver.find_element(By.CSS_SELECTOR, '[id="department"]')
    department.clear()
    department.send_keys(new_department)
    driver.implicitly_wait(5)
    driver.find_element(By.CSS_SELECTOR, '[id="submit"]').click()

    for i in range(6):
        old = old_data[i]
        new = new_data[i]
        check.not_equal(old, new, 'Данные не изменились')

    driver.close()
