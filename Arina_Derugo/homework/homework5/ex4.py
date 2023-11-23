from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://demoqa.com/')
time.sleep(1)


driver.find_element(By.XPATH, '//div[@class="card-body"]//*[text()="Elements"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//li[@id="item-4"]//*[text()="Check Box"]').click()
time.sleep(1)
element = driver.find_element(By.XPATH, '// *[ @ id = "doubleClickBtn"]')
element1 = driver.find_element(By.XPATH, '// *[ @ id = "rightClickBtn"]')
driver.find_element(By.XPATH, '// *[ @ id = "eFoUd"]').click()


action = ActionChains(driver)
action.double_click(element).perform()
action.context_click(element1).perform()