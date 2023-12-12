from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

# 1.//hoster.by/service/cloud/ https://share.cleanshot.com/5pBnWx5j - Number of Cores
'//div[@class="hby-calculator-settings-item  hby-cpu"]//input [@class="hby-input-number"]'

# 2. https://www.21vek.by/ https://share.cleanshot.com/WvrT9NdF - search field
'//*[@id="catalogSearch"]'

# 3. https://www.epam.com/ https://share.cleanshot.com/tpwVh3nc - hamburger button
'//button[@class="hamburger-menu__button"]'

# 4. https://www.browserstack.com/ https://share.cleanshot.com/VV65ZJQj - button 'Demo'
'//*[@id="product-text-section"]//*[@class="btn btn-secondary btn-lg col-md-3"]'

# 5. https://www.whitehouse.gov/ - search button
'//div[@class="homepage-taskbar__search"]//button[@class="search-icon"]'

# try:
#     driver.get("https://hoster.by/service/cloud/")
#     time.sleep(3)
#     core_input = driver.find_element(
#         By.XPATH, '//div[@class="hby-calculator-settings-item  hby-cpu"]//input [@class="hby-input-number"]'
#     )
#     time.sleep(2)
#     core_input.clear()
#     time.sleep(1)
#     core_input.send_keys(4)
#     time.sleep(2)
#     test_1 = core_input = driver.find_element(
#         By.XPATH, '//div[@class="hby-calculator-settings-item  hby-cpu"]//input [@class="hby-input-number"]'
#     ).text
#     print(test_1)
#     core_num = 4
#     assert test_1 == core_num, f'Test failed: {test_1}'
# except Exception as ex:
#     print(ex)
# finally:
#     driver.close()
#     driver.quit()
