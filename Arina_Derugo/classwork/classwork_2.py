from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('https://onliner.by/')
# keyword = 'geeksforgeeks'
# time.sleep(1)

# driver.find_element(By.CSS_SELECTOR, 'div[class="auth-bar__item auth-bar__item--text"]').click()
# time.sleep(1)
# driver.find_element(By.XPATH, "//input[@class='auth-input auth-input_primary auth-input_base auth-form__input auth-form__input_width_full']").send_keys('arina')
# time.sleep(2)
# driver.find_element(By.XPATH, "//input[@class='auth-input auth-input_primary auth-input_base auth-form__input auth-form__input_width_full']").clear()
# time.sleep(1)
# element = driver.find_element(By.XPATH, "//input[@class='auth-input auth-input_primary auth-input_base auth-form__input auth-form__input_width_full']").get_attribute('placeholder')
# print(element)
# time.sleep(1)
# element = driver.find_element(By.XPATH, "//input[@class='auth-input auth-input_primary auth-input_base auth-form__input auth-form__input_width_full']").is_displayed()
# assert element == True
#
#
# driver.execute_script("""window.open('https://logbook.itstep.org')""")
# time.sleep(2)


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://hoster.by/')
keyword = 'geeksforgeeks'
time.sleep(1)

driver.find_element(By.XPATH, "//input[@class='m-input m-b1']").send_keys('adsfg')
time.sleep(1)
driver.find_element(By.XPATH, "//button[@class='m-button red']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//button[@class='btnBorder redBtn small  toCart gmt-active-to-basket']").click()
time.sleep(2)
# driver.find_element(By.XPATH, "").click()
element = driver.find_element(By.XPATH, "//button[@class='btnBorder redBtn small  toCart gmt-active-to-basket']").is_displayed()
assert element == True

driver.save_screenshot()