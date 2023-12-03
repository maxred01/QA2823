import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest_check as check

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/webtables")

driver.find_element(By.CSS_SELECTOR, 'span#edit-record-1').click()
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, 'input#firstName').clear()
driver.find_element(By.CSS_SELECTOR, 'input#firstName').send_keys('Alexey')
driver.find_element(By.CSS_SELECTOR, 'input#lastName').clear()
driver.find_element(By.CSS_SELECTOR, 'input#lastName').send_keys('Zabrodsky')
driver.find_element(By.CSS_SELECTOR, 'input#userEmail').clear()
driver.find_element(By.CSS_SELECTOR, 'input#userEmail').send_keys('Alexey@example.com')
driver.find_element(By.CSS_SELECTOR, 'input#age').clear()
driver.find_element(By.CSS_SELECTOR, 'input#age').send_keys('26')
driver.find_element(By.CSS_SELECTOR, 'input#salary').clear()
driver.find_element(By.CSS_SELECTOR, 'input#salary').send_keys('666666')
driver.find_element(By.CSS_SELECTOR, 'input#department').clear()
driver.find_element(By.CSS_SELECTOR, 'input#department').send_keys('SportEducation')
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, 'button#submit').click()
time.sleep(2)
def test_task_2():
    elements1 = driver.find_element(By.XPATH, '(//div[@class="rt-tr -odd"]/div)[1]')
    elements2 = driver.find_element(By.XPATH, '(//div[@class="rt-tr -odd"]/div)[2]')
    elements3 = driver.find_element(By.XPATH, '(//div[@class="rt-tr -odd"]/div)[3]')
    elements4 = driver.find_element(By.XPATH, '(//div[@class="rt-tr -odd"]/div)[4]')
    elements5 = driver.find_element(By.XPATH, '(//div[@class="rt-tr -odd"]/div)[5]')
    elements6 = driver.find_element(By.XPATH, '(//div[@class="rt-tr -odd"]/div)[6]')

    elements = [
        (elements1.text, 'Alexey', 'Неверный текст первого элемента'),
        (elements2.text, 'Zabrodsky', 'Неверный текст второго элемента'),
        (elements3.text, '26', 'Неверный текст третьего элемента'),
        (elements4.text, 'Alexey@example.com', 'Неверный текст четвертого элемента'),
        (elements5.text, '666666', 'Неверный текст пятого элемента'),
        (elements6.text, 'SportEducation', 'Неверный текст пятого элемента')
    ]

    for pervu, vtoroi, treti in elements:
        check.equal(pervu, vtoroi, treti)
