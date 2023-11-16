import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()

# # ----------------------------------------------------Задание 1
driver.get("https://www.google.com/")
time.sleep(1)


print(driver.page_source)
print(driver.title)
print(driver.current_url)
element = driver.find_element(By.XPATH, "//*[contains(text(),'Сервисы Google')]").text

print(element)

driver.close()
driver.quit()

# # ----------------------------------------------------Задание 2
# driver.get("https://www.youtube.com/")
# time.sleep(1)
#
#
# print(driver.page_source)
# print(driver.title)
# print(driver.current_url)
# element = driver.find_element(By.XPATH,
# '(//div[@class="style-scope ytd-rich-item-renderer"])[1]//yt-formatted-string
# [@id="video-title"]').text
#
# print(element)
#
# driver.close()
# driver.quit()
#
# # ----------------------------------------------------Задание 3
# driver.get("https://www.facebook.com/")
# time.sleep(1)
#
#
# print(driver.page_source)
# print(driver.title)
# print(driver.current_url)
# element = driver.find_element(By.CSS_SELECTOR, "div#globalContainer h2").text
#
# print(element)
#
# driver.close()
# driver.quit()
#
# # ----------------------------------------------------Задание 4
# driver.get("https://www.instagram.com/")
# time.sleep(1)
#
#
# print(driver.page_source)
# print(driver.title)
# print(driver.current_url)
# element = driver.find_element(By.CSS_SELECTOR, "div._ab1y p").text
#
# print(element)
#
# driver.close()
# driver.quit()
#
# # ----------------------------------------------------Задание 5
# driver.get("https://twitter.com/")
# time.sleep(0)
#
#
# print(driver.page_source)
# print(driver.title)
# print(driver.current_url)
# element = driver.find_element(By.XPATH, "//*[contains(text(),'Присоединяйтесь сегодня')]").text
#
# print(element)
#
# driver.close()
# driver.quit()
#
# # ----------------------------------------------------Задание 6
# driver.get("https://baidu.com/")
# time.sleep(1)
#
#
# print(driver.page_source)
# print(driver.title)
# print(driver.current_url)
# element = driver.find_element(By.XPATH, "(//span[@class='title-content-title'])[3]").text
#
# print(element)
#
# driver.close()
# driver.quit()
#
# ----------------------------------------------------Задание 7
# driver.get("https://www.wikipedia.org/")
# time.sleep(1)
#
#
# print(driver.page_source)
# print(driver.title)
# print(driver.current_url)
# element = driver.find_element(By.CSS_SELECTOR, "body#www-wikipedia-org div h1 strong").text
#
# print(element)
#
# driver.close()
# driver.quit()
#
# ----------------------------------------------------Задание 8
# driver.get("https://www.yahoo.com/")
# time.sleep(1)
#
# print(driver.page_source)
# print(driver.title)
# print(driver.current_url)
# element = driver.find_element(By.CSS_SELECTOR, '[data-rapid_p="97"]').text
#
# print(element)
#
# driver.close()
# driver.quit()
#
# ----------------------------------------------------Задание 9
# driver.get("https://dzen.ru/")
# time.sleep(25)
#
#
# print(driver.page_source)
# print(driver.title)
# print(driver.current_url)
# element = driver.find_element(By.XPATH, '(//span[@class="card-news-story__text-3F"])[1]').text
#
# print(element)
#
# driver.close()
# driver.quit()
#
# ----------------------------------------------------Задание 10
# driver.get("https://www.whatsapp.com/")
# time.sleep(1)
#
#
# print(driver.page_source)
# print(driver.title)
# print(driver.current_url)
# element = driver.find_element(By.XPATH, '//article//div[@class="_9t2c _afhu"]//p').text
#
# print(element)
#
# driver.close()
# driver.quit()

# ----------------------------------------------------Задание 11
# driver.get("https://www.amazon.com/")
# time.sleep(25)
#
#
# print(driver.page_source)
# print(driver.title)
# print(driver.current_url)
# element = driver.find_element(By.CSS_SELECTOR,
# 'div#nav-xshop [data-csa-c-slot-id="nav_cs_1"]').text
#
# print(element)
#
# driver.close()
# driver.quit()

# ----------------------------------------------------Задание 12
# driver.get("https://www.tiktok.com/")
#
#
# button = driver.find_element(By.CSS_SELECTOR, "button#header-login-button")
# button.click()
# time.sleep(5)
#
# print(driver.page_source)
# print(driver.title)
# print(driver.current_url)
#
#
# element = driver.find_element(By.CSS_SELECTOR, 'div#loginContainer h2').text
#
# print(element)
#
# driver.close()
# driver.quit()
