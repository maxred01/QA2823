import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
from Alexey_Zabrodsky.Class_work.Locator.locators_page_elements import LocatorsForms
import pytest_check as check


def test_classwork5():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://demoqa.com/")
    time.sleep(2)

    driver.find_element(By.XPATH, '//div[@class="card mt-4 top-card"] [last()-5]').click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//div[@class="element-list collapse show"]/ul/li[last()'
                                  '-8]').click()
    driver.implicitly_wait(5)

    driver.execute_script("window.scrollTo(0, 200)")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, LocatorsForms.full_name).send_keys('Алексей')
    driver.implicitly_wait(5)
    driver.find_element(By.CSS_SELECTOR, LocatorsForms.Email).send_keys('Lesha'
                                                                      'Zabrodsky@mail.ru')
    driver.implicitly_wait(5)
    driver.find_element(By.CSS_SELECTOR, LocatorsForms.Current_Address).send_keys('Минск, '
                                                                              'ул. Некрасова 61')
    driver.implicitly_wait(5)
    (driver.find_element(By.CSS_SELECTOR, LocatorsForms.Permanent_Address).send_keys
     ('Минск, ул. 50 лет Победы 68'))
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'submit').click()
    time.sleep(2)
    check.is_true(driver.find_element(By.ID, 'output').is_displayed(), "Формы нет на экране")

    driver.close()
    driver.quit()
