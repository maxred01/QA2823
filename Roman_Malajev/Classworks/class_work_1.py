from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


# option = Options()
# option.add_argument('--window-size=2000,800')

driver = webdriver.Chrome()

# driver.maximize_window()

keyword = 'itstep'

driver.get('https://www.onliner.by/')
element = driver.find_element(By.CSS_SELECTOR, 'header[class="b-main-page-blocks-header-2 cfix"]>h2>a[href="https://money.onliner.by"]').text
print(element)

driver.get('https://hoster.by/')
element = driver.find_element(By.CSS_SELECTOR, '[class="intro-title m-font-hl1"]').text
print(element)

driver.get('https://5element.by/')
element = driver.find_element(By.CSS_SELECTOR, 'main>div[class="section section--first"]>div[class="container"]>div[class="section-part"]>div[class="section-heading"]>div[class="section-heading__title"]').text
print(element)

driver.get('https://www.tesla.com/')
element = driver.find_element(By.XPATH, '//section[@id="tesla-hero-parallax-3042"]//div//h1').text
print(element)


# print()
# print(driver.title)
# print()
# print(driver.current_url)
# print()
# print(driver.page_source)

driver.close()