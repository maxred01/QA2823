import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/radio-button")

driver.find_element(By.XPATH,
                    "(//div[@class='custom-control custom-radio custom-control-inline'])[1]") \
    .click()
time.sleep(5)
element1 = driver.find_element(By.XPATH, "//span[@class='text-success']")
assert element1.text == 'Yes'
time.sleep(3)

driver.find_element(By.XPATH,
                    "(//div[@class='custom-control custom-radio custom-control-inline'])[2]") \
    .click()
time.sleep(5)
element1 = driver.find_element(By.XPATH, "//span[@class='text-success']")
assert element1.text == 'Impressive'
time.sleep(3)

driver.close()
driver.quit()
