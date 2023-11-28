from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
action = ActionChains(driver)
driver.maximize_window()

url = 'https://demoqa.com/'

# 1. Tex Box

# driver.get(url)
# element = driver.find_element(
#     By.XPATH, '//div[@class="avatar mx-auto white"]//*[@viewBox="0 0 448 512"]'
# )
# element.click()
# text_box = driver.find_element(By.XPATH, '//*[text()="Text Box"]')
# text_box.click()
# name = driver.find_element(By.CSS_SELECTOR, '#userName')
# name.send_keys('Alexey')
# email = driver.find_element(By.CSS_SELECTOR, '#userEmail')
# email.send_keys('1@1.com')
# cur_address = driver.find_element(By.CSS_SELECTOR, '#currentAddress')
# cur_address.send_keys('Minsk')
# perm_address = driver.find_element(By.ID, 'permanentAddress')
# perm_address.send_keys('Minsk, 1')
# submit_button = driver.find_element(By.ID, 'submit')
# time.sleep(3)
# submit_button.click()
# driver.close()
# driver.quit()

# 2. Radio Button

driver.get(url)
driver.find_element(By.XPATH, '//div[@class="avatar mx-auto white"]//*[@viewBox="0 0 448 512"]').click()
# driver.find_element(By.CSS_SELECTOR, '#item-2.active').click()
driver.find_element(By.XPATH, '//span[text()="Radio Button"]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//label[@for="yesRadio"]').click()
time.sleep(2)
test_button = driver.find_element(By.XPATH, '//label[@class="custom-control-label"][@for="yesRadio"]').text
radio_button = "Yes"
assert radio_button == test_button, f'Test failed, Radio Button: {test_button}'
driver.close()
driver.quit()

# 3. Check Box

# driver.get(url)
# driver.find_element(By.XPATH, '//div[@class="avatar mx-auto white"]//*[@viewBox="0 0 448 512"]').click()
# time.sleep(2)
# driver.find_element(By.XPATH, '//span[text()="Check Box"]').click()
# time.sleep(2)
# driver.find_element(By.XPATH, '//button[@title="Expand all"]').click()
# time.sleep(3)
# all_check_box = WebDriverWait(
#     driver, timeout=5
# ).until(expected_conditions.visibility_of_all_elements_located((By.XPATH, '//span[@class="rct-checkbox"]')))
# for check_box in all_check_box:
#     check_box.click()
#     time.sleep(1)
# driver.close()
# driver.quit()

# "тут ошибка, потому что надо скролить т.к нехватает области видимости"

# 4. Buttons

# driver.get(url)
# driver.find_element(By.XPATH, '//div[@class="avatar mx-auto white"]//*[@viewBox="0 0 448 512"]').click()
# time.sleep(1)
# driver.find_element(By.XPATH, '//span[text()="Buttons"]').click()
# time.sleep(1)
# double = driver.find_element(By.CSS_SELECTOR, 'button#doubleClickBtn')
# action.double_click(double)
# action.perform()
# time.sleep(1)
# right = driver.find_element(By.CSS_SELECTOR, 'button#rightClickBtn')
# action.context_click(right)
# action.perform()
# time.sleep(1)
# driver.find_element(By.XPATH, '//button[text()="Click Me"]').click()
# time.sleep(1)
# driver.close()
# driver.quit()

# 5. Upload and Download


