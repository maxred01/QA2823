from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://demoqa.com/')
time.sleep(1)


driver.find_element(By.XPATH, '//div[@class="card-body"]//*[text()="Elements"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//li[@id="item-1"]//*[text()="Check Box"]').click()
time.sleep(1)