import selenium.common
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.maximize_window()

# driver.get('https://www.onliner.by/')
# driver.implicitly_wait(5)
# element_click = driver.find_element(By.CSS_SELECTOR, '[class="auth-bar__item auth-bar__item--text"]').click()
# driver.implicitly_wait(5)
# element_input = driver.find_element(By.CSS_SELECTOR, 'div>div>div>div>div>div>input[class="auth-input auth-input_primary auth-input_base auth-form__input auth-form__input_width_full"]').send_keys('roma')
# driver.implicitly_wait(5)
# element_clear = driver.find_element(By.CSS_SELECTOR, 'div>div>div>div>div>div>input[class="auth-input auth-input_primary auth-input_base auth-form__input auth-form__input_width_full"]').clear()
# driver.implicitly_wait(5)
# element_get = driver.find_element(By.CSS_SELECTOR, 'div>div>div>div>div>div>input[class="auth-input auth-input_primary auth-input_base auth-form__input auth-form__input_width_full"]').get_attribute('placeholder')
# print(element_get)
# element_get = driver.find_element(By.CSS_SELECTOR, 'div>div>div>div>div>div>input[class="auth-input auth-input_primary auth-input_base auth-form__input auth-form__input_width_full"]').is_displayed()
# assert element_get == True
# driver.implicitly_wait(5)
# driver.execute_script("""window.open('https://github.com/maxred01/QA2823')""")
# driver.implicitly_wait(5)

driver.get('https://hoster.by/')
driver.implicitly_wait(5)
element_input = driver.find_element(By.CSS_SELECTOR, '[class="m-input m-b1"]').send_keys('sgsssgdfsgfdg')
driver.implicitly_wait(5)
element_click = driver.find_element(By.CSS_SELECTOR, '[class="m-button red"]').click()
driver.implicitly_wait(5)
element_get = driver.find_element(By.CSS_SELECTOR, '[class="btnFill full redBtn"]').is_displayed()
time.sleep(10)
element_click_2 = driver.find_element(By.CSS_SELECTOR, '[id="accept"]').click()
time.sleep(2)
elements_basket = driver.find_elements(By.XPATH, '//div[@class="domainsTable recom done"]//button[@class="btnBorder redBtn small  toCart gmt-active-to-basket"]')
for element in elements_basket:
    element.click()
time.sleep(20)
driver.quit()
