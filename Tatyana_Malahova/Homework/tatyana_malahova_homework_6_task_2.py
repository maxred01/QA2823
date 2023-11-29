import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest_check as check

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/webtables")

driver.find_element(By.XPATH, "(//span[@class='mr-2'])[3]").click()
time.sleep(1)
element1 = driver.find_element(By.XPATH, "//input[@id='firstName']").clear()
driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys('Tatyana')
time.sleep(1)
element2 = driver.find_element(By.XPATH, "//input[@id='lastName']").clear()
driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys('Malahova')
time.sleep(1)
element3 = driver.find_element(By.XPATH, "//input[@id='userEmail']").clear()
driver.find_element(By.XPATH, "//input[@id='userEmail']") \
    .send_keys('tatyana@example.com')
time.sleep(1)
element4 = driver.find_element(By.XPATH, "//input[@id='age']").clear()
driver.find_element(By.XPATH, "//input[@id='age']").send_keys('24')
time.sleep(1)
element5 = driver.find_element(By.XPATH, "//input[@id='salary']").clear()
driver.find_element(By.XPATH, "//input[@id='salary']").send_keys('2500')
time.sleep(1)
element6 = driver.find_element(By.XPATH, "//input[@id='department']").clear()
driver.find_element(By.XPATH, "//input[@id='department']").send_keys('sale')
time.sleep(3)
driver.find_element(By.XPATH, "//button[@id='submit']").click()
time.sleep(1)


def test_task_2():
    elements1 = driver.find_element(By.XPATH, "(//div[@class='rt-td'])[15]")
    elements2 = driver.find_element(By.XPATH, "(//div[@class='rt-td'])[16]")
    elements3 = driver.find_element(By.XPATH, "(//div[@class='rt-td'])[18]")
    elements4 = driver.find_element(By.XPATH, "(//div[@class='rt-td'])[17]")
    elements5 = driver.find_element(By.XPATH, "(//div[@class='rt-td'])[19]")
    elements6 = driver.find_element(By.XPATH, "(//div[@class='rt-td'])[20]")

    elements = [
        (elements1.text, 'Tatyana', 'Неверный текст первого элемента'),
        (elements2.text, 'Malahova', 'Неверный текст второго элемента'),
        (elements3.text, 'tatyana@example.com', 'Неверный текст третьего элемента'),
        (elements4.text, '24', 'Неверный текст четвертого элемента'),
        (elements5.text, '2500', 'Неверный текст пятого элемента'),
        (elements6.text, 'sale', 'Неверный текст пятого элемента')
    ]

    for pervu, vtoroi, treti in elements:
        check.equal(pervu, vtoroi, treti)
