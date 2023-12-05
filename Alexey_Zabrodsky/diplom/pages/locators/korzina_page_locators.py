from selenium.webdriver.common.by import By

button_info = (By.CSS_SELECTOR, 'div.page__shopcart__delivery_info__title__wrapper')
assert_info = (By.CSS_SELECTOR, 'div.page__shopcart__delivery_info__body__wrapper')

button_delet = (By.CSS_SELECTOR, 'td.page__shopcart__table__body__tools a')
assert_delet = (By.XPATH, '(//div[@class="main__content__body"]//p)[6]')

button_samovyvoz = (By.CSS_SELECTOR, 'div.page__shopcart__table__wrapper input#id_delivery_0')
button_dostavka = (By.CSS_SELECTOR, 'div.page__shopcart__table__wrapper input#id_delivery_1')
button_belpochta = (By.CSS_SELECTOR, 'div.page__shopcart__table__wrapper input#id_delivery_2')

button_nalichnymi = (By.CSS_SELECTOR, 'div.form__item.radio div:nth-of-type(1) input')
button_cards = (By.CSS_SELECTOR, 'div.form__item.radio div:nth-of-type(2) input')

# <---Форма заполнения данных--->
input_name = (By.CSS_SELECTOR, 'input#id_first_name')
input_number = (By.CSS_SELECTOR, 'input#id_phone')
input_adress = (By.CSS_SELECTOR, 'input#id_delivery_address')
input_comment = (By.CSS_SELECTOR, 'textarea#id_comment')
button_person_inf = (By.CSS_SELECTOR, 'input#id_i_agree')
button_podtverdit_zakaz = (By.CSS_SELECTOR, 'input#id__submit__an__order')
assert_vash_zakaz = (By.CSS_SELECTOR, 'div.thank')
