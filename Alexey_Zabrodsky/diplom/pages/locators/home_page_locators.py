from selenium.webdriver.common.by import By

# header
button_domains = (By.CSS_SELECTOR, 'div.menu-item:nth-of-type(1)')
button_hosting = (By.CSS_SELECTOR, 'div.menu-item:nth-of-type(2)')
button_cloud = (By.CSS_SELECTOR, 'div.menu-item:nth-of-type(3)')
button_solutions = (By.CSS_SELECTOR, 'div.menu-item:nth-of-type(4)')
button_outsourcing = (By.CSS_SELECTOR, 'div.menu-item:nth-of-type(5)')
button_email = (By.CSS_SELECTOR, 'div.menu-item:nth-of-type(6)')
button_security = (By.CSS_SELECTOR, 'div.menu-item:nth-of-type(7)')
button_company = (By.CSS_SELECTOR, 'div.menu-item:nth-of-type(8)')
button_img_hoster = (By.CSS_SELECTOR, 'a.m-header-left-item')
button_voyti = (By.ID, 'menu_auth')
button_kontakty = (By.XPATH, '//span[@class="contacts-text m-font-l1"]')
button_korzina = (By.XPATH, '//div[@class="cart-icon right-icon m-icon-wrapper cart-button"]')
