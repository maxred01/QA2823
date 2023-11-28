from selenium import webdriver
from selenium.webdriver.common.by import By
from locators.locators_page_elements import LocatorsForms
import pytest_check as check
import time

def test_classwork3():

    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get('https://demoqa.com/')
    driver.implicitly_wait(5)
    # test_text = driver.find_element(By.XPATH, '(//div[@class="card-body"])[1]//h5').text
    # check.equal(test_text, '13123321', 'Ошибка')
    # test_text2 = driver.find_element(By.XPATH, '(//div[@class="card-body"])[2]//h5').text
    # check.equal(test_text2, '13123321', 'Ошибка')
    # test_text3 = driver.find_element(By.XPATH, '(//div[@class="card-body"])[3]//h5').text
    # check.equal(test_text3, '13123321', 'Ошибка')
    # test_text4 = driver.find_element(By.XPATH, '(//div[@class="card-body"])[4]//h5').text
    # check.equal(test_text4, '13123321', 'Ошибка')
    # test_text5 = driver.find_element(By.XPATH, '(//div[@class="card-body"])[5]//h5').text
    # check.equal(test_text5, '13123321', 'Ошибка')
    # test_text6 = driver.find_element(By.XPATH, '(//div[@class="card-body"])[6]//h5').text
    # check.equal(test_text6, '13123321', 'Ошибка')

    title = driver.find_element(By.XPATH, '(//div[@class="card-body"])[1]//h5')
    title2 = driver.find_element(By.XPATH, '(//div[@class="card-body"])[2]//h5')
    title3 = driver.find_element(By.XPATH, '(//div[@class="card-body"])[3]//h5')
    title4 = driver.find_element(By.XPATH, '(//div[@class="card-body"])[4]//h5')
    title5 = driver.find_element(By.XPATH, '(//div[@class="card-body"])[5]//h5')
    title6 = driver.find_element(By.XPATH, '(//div[@class="card-body"])[6]//h5')

    titles_special = [
        title,
        title2,
        title3,
        title4,
        title5,
        title6,
    ]

    titles_text = [
        (title.text, 'Elements', 'Неверный текст первого элемента'),
        (title2.text, 'Forms', 'Неверный текст второго элемента'),
        (title3.text, 'Alerts, Frame & Windows', 'Неверный текст третьего элемента'),
        (title4.text, 'Widgets', 'Неверный текст четвертого элемента'),
        (title5.text, 'Interactions', 'Неверный текст пятого элемента'),
        (title6.text, 'Book Store Application', 'Неверный текст шестого элемента'),
    ]

    # for perviy, vtoroy, tretiy in titles_text:
    #     check.equal(perviy, vtoroy, tretiy)

    titles_isdisplayed = [
        (title.is_displayed(), 'Первый элемент не отображается'),
        (title2.is_displayed(), 'Второй элемент не отображается'),
        (title3.is_displayed(), 'Третий элемент не отображается'),
        (title4.is_displayed(), 'Четвертый элемент не отображается'),
        (title5.is_displayed(), 'Пятый элемент не отображается'),
        (title6.is_displayed(), 'Шестой элемент не отображается'),
    ]

    # for perviy, vtoroy in titles_isdisplayed, titles_text:
    #     check.is_true(perviy, vtoroy)

    titles_special = [
        (title, 'Elements', 'Неверный текст первого элемента'),
        (title2, 'Forms', 'Неверный текст второго элемента'),
        (title3, 'Alerts, Frame & Windows', 'Неверный текст третьего элемента'),
        (title4, 'Widgets', 'Неверный текст четвертого элемента'),
        (title5, 'Interactions', 'Неверный текст пятого элемента'),
        (title6, 'Book Store Application', 'Неверный текст шестого элемента'),
    ]

    # for element, name, error in titles_special:
    #     if check.is_true(element.):
    #         check.equal(element, name, error)

    driver.find_element(By.XPATH, '//div[@class="card-body"]//*[text()="Elements"]').click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//li[@id="item-0"]//*[text()="Text Box"]').click()
    driver.implicitly_wait(5)
    driver.find_element(By.CSS_SELECTOR, LocatorsForms.Full_Name).send_keys('rom4ik228')
    driver.implicitly_wait(5)
    driver.find_element(By.CSS_SELECTOR, LocatorsForms.Email).send_keys('adad@gmail.com')
    driver.implicitly_wait(5)
    driver.find_element(By.CSS_SELECTOR, LocatorsForms.Current_Address) \
        .send_keys('496 Nut Swamp Dr. Clarksville, TN 37040')
    driver.implicitly_wait(5)
    driver.find_element(By.CSS_SELECTOR, LocatorsForms.Permanent_Address) \
        .send_keys('894 Mayfield Dr. Johnson City, TN 37601')
    driver.implicitly_wait(5)
    driver.execute_script('window.scrollBy(0,300)')
    driver.implicitly_wait(5)
    driver.find_element(By.CSS_SELECTOR, '[id="submit"]').click()
    output = driver.find_element(By.XPATH, '//div[@id="output"]')
    check.is_true(output.is_displayed(), 'Поля нет')
