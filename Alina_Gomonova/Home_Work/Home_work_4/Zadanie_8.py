from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.yahoo.com/")
element = driver.find_element(By.XPATH, '//a[@class="_yb_192kn _yb_1iov6 _yb_h5twg _yb_14fn0"]').text

print(element)
print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.close()
driver.quit()