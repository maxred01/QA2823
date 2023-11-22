import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

actionChains = ActionChains(driver)

driver.maximize_window()


# 1. Заполнение текстового поля

driver.get('https://demoqa.com/')
driver.implicitly_wait(5)
driver.execute_script('window.scrollBy(0,250)')
driver.implicitly_wait(5)
driver.find_element(By.XPATH, '//div[@class="card-body"]//*[text()="Elements"]').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, '//li[@id="item-0"]//*[text()="Text Box"]').click()
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, '[id="userName"]').send_keys('rom4ik228')
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, '[id="userEmail"]').send_keys('adad@dada.com')
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, '[id="currentAddress"]').send_keys('496 Nut Swamp Dr. Clarksville, TN 37040')
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, '[id="permanentAddress"]').send_keys('894 Mayfield Dr. Johnson City, TN 37601')
driver.implicitly_wait(5)
driver.execute_script('window.scrollBy(0,300)')
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, '[id="submit"]').click()

time.sleep(1)


# 2. Выбор радиокнопки

driver.find_element(By.XPATH, '//li[@id="item-2"]//*[text()="Radio Button"]').click()
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, '[for="yesRadio"]').click()
driver.implicitly_wait(5)
radio = driver.find_element(By.CSS_SELECTOR, '[id="yesRadio"]').is_selected()
assert radio == True

time.sleep(1)


# 3. Выбор опции из выпадающего списка

driver.find_element(By.XPATH, '//li[@id="item-1"]//*[text()="Check Box"]').click()
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, '[title="Expand all"]').click()
driver.implicitly_wait(5)
checkboxs = driver.find_elements(By.CSS_SELECTOR, '[class="rct-checkbox"]')
driver.implicitly_wait(5)
for box in checkboxs:
    box.click()
    box.click()
    driver.execute_script('window.scrollBy(0,35)')

time.sleep(2)


# 4. Редактировании и удалении формы

driver.find_element(By.XPATH, '//li[@id="item-4"]//*[text()="Buttons"]').click()
driver.implicitly_wait(5)
double = driver.find_element(By.CSS_SELECTOR, '[id="doubleClickBtn"]')
actionChains.double_click(double).perform()
driver.implicitly_wait(5)
right_click = driver.find_element(By.CSS_SELECTOR, '[id="rightClickBtn"]')
actionChains.context_click(right_click).perform()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, '''//button[@class="btn btn-primary" and text()='Click Me']''').click()

time.sleep(1)


# Доп задача

driver.execute_script('window.scrollBy(0,300)')
driver.implicitly_wait(5)
driver.find_element(By.XPATH, '//li[@id="item-7"]//*[text()="Upload and Download"]').click()
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, '[id="uploadFile"]').send_keys('C:/Users/roman/PycharmProjects/QA2823/homework.txt')
check_file = driver.find_element(By.CSS_SELECTOR, '[id="uploadedFilePath"]').is_displayed()
assert check_file == True

time.sleep(1)
