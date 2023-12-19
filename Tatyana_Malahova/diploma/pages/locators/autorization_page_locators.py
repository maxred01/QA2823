from selenium.webdriver.common.by import By

picture_autorization = (
By.XPATH, '(//*[@id="header-user-actions-container"]//div[@role="presentation" and @aria-haspopup="true"])[1]')
log_in_in_window = (By.CSS_SELECTOR, "//span[@class='_ZDS_REF_SCOPE_ smZi2j']")
new_client_in_window = (By.CSS_SELECTOR, "//span[@class='_ZDS_REF_SCOPE_ smZi2j']")
text_welcome = (By.CSS_SELECTOR, "//div[@class='Wn-EjT']")
e_mail_address_second = (By.CSS_SELECTOR, "//input[@id='login.email']")
password_second = (By.CSS_SELECTOR, "//input[@id='login.secret']")
log_in = (By.CSS_SELECTOR, "//button[@data-testid='login_button']")
forgot_password = (By.CSS_SELECTOR, "//span[@class='KxHAYs _2kjxJ6 dgII7d sxs3x9']")
register = (By.CSS_SELECTOR, "//button[@data-testid='toggle_register_button']")
text_first_time_here = (By.CSS_SELECTOR, "(//h3[@class='KxHAYs gr9aYh FxZV-M _4F506m'])[2]")
text_privacy_policy = (By.CSS_SELECTOR, "//li[@data-testid='footer_privacy_policy']")
text_reglament = (By.CSS_SELECTOR, "//li[@data-testid='terms_of_use']")
text_company_data = (By.CSS_SELECTOR, "//li[@data-testid='footer_legal_notice']")
name = (By.CSS_SELECTOR, "//input[@name='register.first_name']")
name_continued = (By.CSS_SELECTOR, "//input[@name='register.last_name']")
e_mail_address_first = (By.CSS_SELECTOR, "//input[@name='register.email']")
password_first = (By.CSS_SELECTOR, "//input[@name='register.secret']")
female_fashion = (By.CSS_SELECTOR, "(//label[@class='sjPORp KxHAYs _2kjxJ6 FxZV-M JT3_zV _5Yd-hZ _4F506m RKlRH1'])[1]")
male_fashion = (By.CSS_SELECTOR, "(//label[@class='sjPORp KxHAYs _2kjxJ6 FxZV-M JT3_zV _5Yd-hZ _4F506m RKlRH1'])[2]")
no_preference = (By.CSS_SELECTOR, "(//label[@class='sjPORp KxHAYs _2kjxJ6 FxZV-M JT3_zV _5Yd-hZ _4F506m RKlRH1'])[3]")
button_register = (By.CSS_SELECTOR, "//button[@data-name='sso_register_register']")
agree_rules = (By.CSS_SELECTOR, "//label[@class='RyEgWR KxHAYs _2kjxJ6 FxZV-M r1svAh JT3_zV _5Yd-hZ _4F506m IxoCOT']")
