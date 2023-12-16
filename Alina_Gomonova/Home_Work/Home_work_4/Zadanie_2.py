from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.youtube.com/")
element = driver.find_element(By.XPATH, '(//a[@id="video-title-link"])[1]').text


print(element)
print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.close()
driver.quit()