import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# option = Options()
# option.add_argument("--window-size=2000,800") #разрешение экрана
# driver = webdriver.Chrome(options=option)
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://hoster.by/")

driver.find_element(By.CSS_SELECTOR, 'input.m-input.m-b1').send_keys('Волшебство')
driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR, 'button.m-button.red').click()
driver.implicitly_wait(5)
#
driver.find_element(By.XPATH, '//input[@class="auth-input auth-input_primary '
                              'auth-input_base auth-form__input '
                              'auth-form__input_width_full"]').clear()
driver.implicitly_wait(5)

element = driver.find_element(By.XPATH, '//input[@class="auth-input '
                                        'auth-input_primary auth-input_base '
                                        'auth-form__input '
                                        'auth-form__input_width_full"]') \
    .get_attribute('placeholder')
# print(element)

driver.find_element(By.CSS_SELECTOR, 'button#accept').click()
# driver.implicitly_wait(5)
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, 'button#domain_monster').click()
# driver.implicitly_wait(5)
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, 'button#domain_best').click()
# driver.implicitly_wait(5)
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, 'button#domain_online').click()
# driver.implicitly_wait(5)
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, 'button#domain_store').click()
# driver.implicitly_wait(5)
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, 'button#domain_tech').click()
# driver.implicitly_wait(5)
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, 'button#domain_net').click()
# driver.implicitly_wait(5)
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, 'button#domain_site').click()
# driver.implicitly_wait(5)
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, 'button#domain_org').click()
# driver.implicitly_wait(5)
time.sleep(1)

# element = driver.find_element(By.CSS_SELECTOR, 'button#domain').is_displayed()
# assert element == True

# driver.execute_script("""window.open('https://www.google.com/')""")
# driver.implicitly_wait(5)

driver.close()
driver.quit()
