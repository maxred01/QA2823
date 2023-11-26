from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.wikipedia.org/")
element = driver.find_element(By.XPATH, '//strong[@class="jsl10n localized-slogan"]').text

print(element)
print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.close()
driver.quit()