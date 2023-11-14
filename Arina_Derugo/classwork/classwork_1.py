# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# import time
# option = Options()
# # option.add_argument('--window-size=1000,800')
# # driver = webdriver.Chrome(options=option)
# driver = webdriver.Chrome()
# driver.maximize_window()
#
# # keyword = 'geeksforgeeks'
#
# driver.get('https://www.geeksforgeeks.org/')
#
# element = driver.find_element(By.XPATH, '//div[@class="ant-row ant-row-center gfg_home_page_search_heading"]')
# time.sleep(10)
# print(driver.title)
# вернет название сайта
# print(driver.current_url) вернет ссылку
# print(driver.page_source) вернет дом-дерево




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# import time
#
# driver = webdriver.Chrome()
# driver.get('https://www.onliner.by/')
# keyword = 'geeksforgeeks'
#
# element = driver.find_element(By.XPATH, "//div[@class='b-main-page-grid-4 b-main-page-news-2']//*[text()='Кошелек']").text
# print(driver.title)
# print(element)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome()
driver.get('https://www.onliner.by/')
keyword = 'geeksforgeeks'

element = driver.find_element(By.XPATH, "//div[@class='b-main-page-grid-4 b-main-page-news-2']//*[text()='Кошелек']")
print(driver.title)
print(element)