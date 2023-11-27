import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/")

driver.find_element(By.XPATH, "(//div[@class='card mt-4 top-card'])[1]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[text()='Text Box']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='userName']").send_keys('Tatyana Malahova')
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys('something_email@mail.com')
time.sleep(1)
driver.find_element(By.XPATH, "//textarea[@id='currentAddress']") \
    .send_keys('Minsk,Independence Avenue, 123, 67')
time.sleep(1)
driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']") \
    .send_keys('Minsk,Independence Avenue, 123, 67')
time.sleep(1)
driver.find_element(By.XPATH, "//body").send_keys(Keys.END)
time.sleep(2)
driver.find_element(By.XPATH, "//button[@id='submit']").click()
time.sleep(2)

driver.close()
driver.quit()
