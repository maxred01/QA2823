from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://ru-ru.facebook.com/")
element = driver.find_element(By.XPATH, '//h2[@class="_8eso"]').text

print(element)
print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.close()
driver.quit()