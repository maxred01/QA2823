from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://twitter.com/")
element = driver.find_element(By.XPATH, "//span[text()='Присоединяйтесь сегодня.']").text

print(element)
print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.close()
driver.quit()