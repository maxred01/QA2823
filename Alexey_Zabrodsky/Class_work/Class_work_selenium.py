from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# option = Options()
# option.add_argument("--window-size=2000,800") #разрешение экрана
# driver = webdriver.Chrome(options=option)
driver = webdriver.Chrome()
driver.maximize_window()

# driver.get("https://www.onliner.by/")
# driver.get("https://hoster.by/")
# driver.get("https://www.tesla.com/")
# driver.get("https://www.tesla.com/")
driver.get("https://5element.by/")
time.sleep(0)

# element = driver.find_element(By.CSS_SELECTOR, 'div#onliner-catalog-purchases header h2').text
# element = driver.find_element(By.XPATH, '//div[@class="main-page"]//h1').text
# element = driver.find_element(By.CSS_SELECTOR, 'div#block-tesla-frontend-content section#tesla-hero-parallax-3042 h1').text
element = driver.find_element(By.XPATH, "//*[contains(text(),'Популярные категории')]").text



print(element)
# print(element)
# print(element)
print(driver.title)
print(driver.current_url) # Выводит URL
# print(driver.page_source) # тот же поисковик что и devtools

driver.close() # закрыть все вкладки браузера после тестинга
driver.quit() # выходит с браузера
