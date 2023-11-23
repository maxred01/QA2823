import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
actions = ActionChains(driver)

driver.get("https://demoqa.com/")


# Задание 1
driver.find_element(By.XPATH, '//div[@class="card mt-4 top-card"] [last()-5]').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, '//div[@class="element-list collapse show"]/ul/li[last()-8]').click()
driver.implicitly_wait(5)

driver.execute_script("window.scrollTo(0, 200)")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, 'input#userName').send_keys('Алексей')
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, 'input#userEmail').send_keys('LeshaZabrodsky@mail.ru')
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, 'textarea#currentAddress').send_keys('Минск, ул. Некрасова 61')
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, 'textarea#permanentAddress').send_keys('Минск, ул. 50 лет Победы 69')
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, 'button#submit').click()
time.sleep(2)


# Задание 2
driver.find_element(By.XPATH, '//div[@class="element-list collapse show"]/ul/li[last()-7]').click()
driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR, 'span.rct-checkbox').click()
driver.implicitly_wait(5)
element = driver.find_element(By.CSS_SELECTOR, 'span.rct-checkbox').is_displayed()
assert element == 1
time.sleep(2)

# Задание 3
driver.find_element(By.CSS_SELECTOR, 'span.rct-checkbox').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, '//button[@class="rct-collapse rct-collapse-btn"]').click()
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, 'div#tree-node ol ol li:nth-of-type(1) button').click()
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, 'div#tree-node ol ol li:nth-of-type(2) button').click()
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, 'div#tree-node ol ol li:nth-of-type(3) button').click()
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, 'div#tree-node ol ol ol li:nth-of-type(1) button').click()
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, 'div#tree-node ol ol ol li:nth-of-type(2) button').click()
driver.implicitly_wait(5)
driver.execute_script("window.scrollTo(0, 300)")
driver.find_element(By.XPATH, '(//span[@class="rct-checkbox"])[3]').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, '(//span[@class="rct-checkbox"])[4]').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, '(//span[@class="rct-checkbox"])[7]').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, '(//span[@class="rct-checkbox"])[8]').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, '(//span[@class="rct-checkbox"])[9]').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, '(//span[@class="rct-checkbox"])[11]').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, '(//span[@class="rct-checkbox"])[12]').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, '(//span[@class="rct-checkbox"])[13]').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, '(//span[@class="rct-checkbox"])[14]').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, '(//span[@class="rct-checkbox"])[16]').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, '(//span[@class="rct-checkbox"])[17]').click()
time.sleep(2)


# Задание 4
driver.find_element(By.CSS_SELECTOR, 'li#item-4 span').click()
time.sleep(1)

double_click = driver.find_element(By.XPATH, '//button[@id="doubleClickBtn"]')
actions.double_click(double_click).perform()
driver.implicitly_wait(5)

right_click = driver.find_element(By.XPATH, '//button[@id="rightClickBtn"]')
actions.context_click(right_click).perform()
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//button[text()='Click Me']").click()
time.sleep(2)


# Задание 5
driver.execute_script("window.scrollTo(0, 300)")
driver.find_element(By.CSS_SELECTOR, 'li#item-7 span').click()
time.sleep(3)

file_patch = 'D:/QA2823/Alexey_Zabrodsky/Home_work/home_work_2.txt'
file_input = driver.find_element(By.CSS_SELECTOR, 'input#uploadFile')
file_input.send_keys(file_patch)
element = driver.find_element(By.CSS_SELECTOR, 'p#uploadedFilePath').is_displayed()
assert element == 1
time.sleep(1)

driver.close()
driver.quit()
