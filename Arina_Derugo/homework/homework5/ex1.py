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
driver.find_element(By.XPATH, '//li[@id="item-0"]//*[text()="Text Box"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '[id="userName"]').send_keys('Arina')
time.sleep(1)
driver.find_element(By.XPATH, '[id="userEmail"]').send_keys('arina1111@gmail.com')
time.sleep(1)
driver.find_element(By.XPATH, '[id="currentAddress"]').send_keys('street Kozlova 12')
time.sleep(1)
driver.find_element(By.XPATH, '[id="permanentAddress"]').send_keys('street Zaharova 21')
time.sleep(1)
driver.find_element(By.XPATH, "button[id='submit']").click()
time.sleep(1)

