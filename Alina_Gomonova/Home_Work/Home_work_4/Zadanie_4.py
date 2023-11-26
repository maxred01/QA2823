from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.instagram.com/")
element = driver.find_element(By.XPATH, '//p[@class="_ab25"]').text

print(element)
print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.close()
driver.quit()