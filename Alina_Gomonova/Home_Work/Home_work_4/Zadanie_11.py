from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.amazon.com/")
element = driver.find_element(By.XPATH, '//a[@href="/gp/browse.html?node=16115931011&ref_=nav_cs_registry"]').text

print(element)
print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.close()
driver.quit()