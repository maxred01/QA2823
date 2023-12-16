from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#1
driver.get("https://www.google.com/")
element = driver.find_element(By.XPATH, '//div[@id="SIvCob"]').text

#2
# driver.get("https://www.youtube.com/")
# element = driver.find_element(By.XPATH, '//div[@id="info-container"]//yt-formatted-string[@id="video-title"]').text

#3
# driver.get("https://ru-ru.facebook.com/")
# element = driver.find_element(By.XPATH, '//h2[@class="_8eso"]').text

#4
# driver.get("https://www.instagram.com/")
# element = driver.find_element(By.XPATH, '//p[@class="_ab25"]').text

#5
# driver.get("https://twitter.com/")
# element = driver.find_element(By.XPATH, "//span[text()='Присоединяйтесь сегодня.']").text

#6
# driver.get("https://www.baidu.com/")
# element = driver.find_element(By.XPATH, '(//span[@class="title-content-title"])[3]').text

#7
# driver.get("https://www.wikipedia.org/")
# element = driver.find_element(By.XPATH, '//strong[@class="jsl10n localized-slogan"]').text

#8
# driver.get("https://www.yahoo.com/")
# element = driver.find_element(By.XPATH, '//a[@class="_yb_io0r2 _yb_1hru9 _yb_1jh73 _yb_1gfxm"]').text

#9
# driver.get("https://www.whatsapp.com/")
# element = driver.find_element(By.XPATH, '//p[text()="Простой и надёжный способ конфиденциально обмениваться сообщениями и совершать бесплатные* звонки в любой точке мира."]').text

#10
# driver.get("https://www.amazon.com/)
# element = driver.find_element(By.XPATH, '//a[text()="Registry"]').text

#11
# driver.get("https://www.tiktok.com/")
# element = driver.find_element(By.XPATH, '//h2[@id="login-modal-title"]').text

print(element)
print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.close()
driver.quit()