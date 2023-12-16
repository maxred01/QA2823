import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/radio-button")

driver.find_element(By.CSS_SELECTOR,'[for="yesRadio"]') \
    .click()
time.sleep(5)
element = driver.find_element(By.XPATH, "//span[@class='text-success']")
assert element.text == 'Yes'
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,'[for="impressiveRadio"]') \
    .click()
time.sleep(5)
element = driver.find_element(By.XPATH, "//span[@class='text-success']")
assert element.text == 'Impressive'
time.sleep(3)

driver.close()
driver.quit()
