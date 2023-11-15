from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()

keyword = 'itstep'
print()
driver.get('https://www.google.com/')
time.sleep(10)
element = driver.find_element(By.CSS_SELECTOR, '[id="SIvCob"]').text
print(element)
print()
driver.get('https://www.youtube.com/')
time.sleep(10)
element = driver.find_element(By.XPATH, '(//div[@class="style-scope ytd-rich-item-renderer"])[1]//yt-formatted-string[@id="video-title"]').text
print(element)
print()
driver.get('https://www.facebook.com/')
time.sleep(10)
element = driver.find_element(By.CSS_SELECTOR, '[class="_8eso"]').text
print(element)
print()
driver.get('https://www.instagram.com/')
time.sleep(10)
element = driver.find_element(By.CSS_SELECTOR, '[class="_ab25"]').text
print(element)
print()
driver.get('https://twitter.com/')
time.sleep(10)
element = driver.find_element(By.XPATH, '//div[@class="css-901oao r-1nao33i r-fm7h5w r-1yjpyg1 r-b88u0q r-ueyrd6 r-zd98yo r-bcqeeo r-qvutc0"]//span[@class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"]').text
print(element)
print()
driver.get('http://www.baidu.com/')
time.sleep(10)
element = driver.find_element(By.XPATH, '//li[@data-index="1"]//span[@class="title-content-title"]').text
print(element)
print()
driver.get('https://www.wikipedia.org/')
time.sleep(10)
element = driver.find_element(By.CSS_SELECTOR, '[data-jsl10n="portal.slogan"]').text
print(element)
print()
driver.get('https://www.yahoo.com/')
time.sleep(10)
element = driver.find_element(By.CSS_SELECTOR, '[data-rapid_p="97"]').text
print(element)
print()
# driver.get('https://yandex.ru/')
# time.sleep(2)
# element = driver.find_element(By.XPATH, '(//main//span[@class="card-news-story__text-3F"])[1]').text
# print(element)
# print()
driver.get('https://www.whatsapp.com/')
time.sleep(10)
element = driver.find_element(By.CSS_SELECTOR, 'span[class="_9vg3 _9sep _aj1b"]>div>p').text
print(element)
print()
# driver.get('https://www.amazon.com/')
# time.sleep(10)
# element = driver.find_element(By.CSS_SELECTOR, '[data-csa-c-content-id="nav_cs_registry"]').text
# print(element)
# print()
driver.get('https://www.tiktok.com/')
time.sleep(10)
element_click = driver.find_element(By.CSS_SELECTOR, '[id="header-login-button"]').click()
time.sleep(2)
element = driver.find_element(By.CSS_SELECTOR, '[id="login-modal-title"]').text
print(element)
driver.quit()

