from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://xmlsearch.yandex.by/")
element = driver.find_element(By.XPATH, '//a[@class="home-link2 headline__personal-enter \
headline__personal-enter home-link2_color_black"]').text


print(element)
print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.close()
driver.quit()