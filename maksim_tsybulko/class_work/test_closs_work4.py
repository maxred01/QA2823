from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time, allure, pytest

@pytest.mark.presentation
@pytest.mark.non_multiple_CPUs_run
@allure.suite("Авторизация")
@allure.title("Авторизация с валидными данными")
def test_login():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://onliner.by")

    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//div[@class="auth-bar__item auth-bar__item--text"]').click()
    driver.implicitly_wait(5)

    driver.find_element(By.XPATH, '//input[@class="auth-input auth-input_primary auth-input_base auth-form__input auth-form__input_width_full"]').send_keys('google@google.com')
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//input[@class="auth-input auth-input_primary auth-input_base auth-form__input auth-form__input_width_full"]').clear()
    driver.implicitly_wait(5)
    element = driver.find_element(By.XPATH, '//input[@class="auth-input auth-input_primary auth-input_base auth-form__input auth-form__input_width_full"]').get_attribute('placeholder')
    print(element)

    element = driver.find_element(By.XPATH, '//input[@class="auth-input auth-input_primary auth-input_base auth-form__input auth-form__input_width_full"]').is_displayed()
    assert element == True

    driver.execute_script("""window.open('https://logbook.itstep.org/')""")
    time.sleep(2)






#
# onliner.by - КОШЕЛЕК, title
# hoster.by - От домена до корпоративных решений, title
# tesla.com - Model Y, title
# 5element.by - Популярные категории, title