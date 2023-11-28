# https://maxkorzh.live/ - music tab
"""//div[@class="menu tablet_hide mobile_hide"]//*[@href="muzyika/"]"""

# https://www.fpp.net/work/ https://share.cleanshot.com/LZDmbQkZ - search num '2'
'//*[@class="relative w-full"]//*[text()="2"]'

# https://www.awwwards.com/ https://share.cleanshot.com/y44tLHBP - button 404
'a[href$="/websites/404-pages/"]'

# https: // www.pttrns.com / https: // share.cleanshot.com / cdv5jCzf - trial button
'[class="gspb-buttonbox-title"]'




from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

url = "https://www.pttrns.com/"

try:
    driver.get(url)
    time.sleep(3)
    search_num = driver.find_element(
        By.CSS_SELECTOR, '[class="gspb-buttonbox-title"]'
    ).click()
    time.sleep(4)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
