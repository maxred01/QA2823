from selenium.webdriver.common.by import By

# <---header--->
button_logo = (By.XPATH, '//div[@class="header__logo__image"]')
button_o_magazine = (By.CSS_SELECTOR, 'div.header__menu__item:nth-of-type(1)')
button_dostavka_i_oplata = (By.CSS_SELECTOR, 'div.header__menu__item:nth-of-type(2)')
button_garantiya = (By.CSS_SELECTOR, 'div.header__menu__item:nth-of-type(3)')
button_korzina = (By.CSS_SELECTOR, 'div.header__wrapper a#id__header__shopcart__title__link')
input_poisk = (By.CSS_SELECTOR, 'div.header__search input.top-search-input')
button_poisk = (By.CSS_SELECTOR, 'div.header__search button#id__top__search__button')

# <---header_mobile--->
button_korzina_mobile = (By.CSS_SELECTOR, 'div.mobile__navbar.active '
                                          'a#id__header__shopcart__title__link')
input_poisk_mobile = (By.CSS_SELECTOR, 'div.mobile__navbar__search input.top-search-input')
button_poisk_mobile = (By.CSS_SELECTOR, 'div.mobile__navbar.active button#id__top__search__button')
button_logo_mobile = (By.CSS_SELECTOR, 'div.mobile__navbar__logo')

# <---menu left--->
button_novinki = (By.CSS_SELECTOR, 'div.menu_catalog [data-id="19860"]')
button_podarochnyye_nabory = (By.CSS_SELECTOR, 'div.menu_catalog [data-id="21347"]')
button_rasprodazha = (By.CSS_SELECTOR, 'div.menu_catalog [data-id="7189"]')
button_podarki_dlya_zhenshchin = (By.CSS_SELECTOR, 'div.menu_catalog [data-id="20080"]')
button_profitable_proposition = (By.CSS_SELECTOR, 'div.menu_catalog [data-id="19556"]')
button_podarki_dlya_muzhchin = (By.CSS_SELECTOR, 'div.menu_catalog [data-id="18274"]')
button_vesenniye_skidki = (By.CSS_SELECTOR, 'div.menu_catalog [data-id="18275"]')
button_novogodniye_tovary = (By.CSS_SELECTOR, 'div.menu_catalog [data-id="5436"]')
button_tovary_dlya_shkoly = (By.CSS_SELECTOR, 'div.menu_catalog [data-id="17740"]')
button_tovary_dlya_kukhni = (By.CSS_SELECTOR, 'div.menu_catalog [data-id="766"]')
button_tovary_dlya_doma = (By.CSS_SELECTOR, 'div.menu_catalog [data-id="943"]')
button_sportivnyye_tovary = (By.CSS_SELECTOR, 'div.menu_catalog [data-id="954"]')
button_krasota_i_zdorovye = (By.CSS_SELECTOR, 'div.menu_catalog [data-id="959"]')
button_sumki_klatchi_ryukzaki = (By.CSS_SELECTOR, 'div.menu_catalog [data-id="18931"]')
button_gadzhety = (By.CSS_SELECTOR, 'div.menu_catalog [data-id="965"]')
button_detskiy_mir = (By.CSS_SELECTOR, 'div.menu_catalog [data-id="969"]')
button_podarki = (By.CSS_SELECTOR, 'div.menu_catalog [data-id="976"]')
button_avto = (By.CSS_SELECTOR, 'div.menu_catalog [data-id="981"]')
button_elektroinstrument = (By.CSS_SELECTOR, 'div.menu_catalog [data-id="984"]')
button_turizm_i_otdykh = (By.CSS_SELECTOR, 'div.menu_catalog [data-id="735"]')
button_vse_dlya_doma_i_dachi = (By.CSS_SELECTOR, 'div.menu_catalog [data-id="734"]')
button_vse_dlya_selskogo_khozyaystva = (By.CSS_SELECTOR, 'div.menu_catalog [data-id="7936"]')
button_mikroklimaticheskaya_tekhnika = (By.CSS_SELECTOR, 'div.menu_catalog [data-id="1565"]')
button_suvenirnaya_produktsiya = (By.CSS_SELECTOR, 'div.menu_catalog [data-id="2277"]')
button_vse_dlya_pitomtsev = (By.CSS_SELECTOR, 'div.menu_catalog [data-id="5246"]')
button_odezhda_i_obuv = (By.CSS_SELECTOR, 'div.menu_catalog [data-id="5675"]')
button_stroymaterialy = (By.CSS_SELECTOR, 'div.menu_catalog [data-id="18957"]')
button_utsenonnyye_tovary = (By.CSS_SELECTOR, 'div.menu_catalog [data-id="5386"]')
# <---assert menu--->
assert_novinki = (By.CSS_SELECTOR, '[page_id="19860"]')
assert_podarochnyye_nabory = (By.CSS_SELECTOR, '[page_id="21347"]')
assert_rasprodazha = (By.CSS_SELECTOR, '[page_id="7189"]')
assert_podarki_dlya_zhenshchin = (By.CSS_SELECTOR, '[page_id="20080"]')
assert_profitable_proposition = (By.CSS_SELECTOR, '[page_id="19556"]')
assert_podarki_dlya_muzhchin = (By.CSS_SELECTOR, '[page_id="18274"]')
assert_vesenniye_skidki = (By.CSS_SELECTOR, '[page_id="18275"]')
assert_novogodniye_tovary = (By.CSS_SELECTOR, '[page_id="5436"]')
assert_tovary_dlya_shkoly = (By.CSS_SELECTOR, '[page_id="17740"]')
assert_tovary_dlya_kukhni = (By.CSS_SELECTOR, '[page_id="766"]')
assert_tovary_dlya_doma = (By.CSS_SELECTOR, '[page_id="943"]')
assert_sportivnyye_tovary = (By.CSS_SELECTOR, '[page_id="954"]')
assert_krasota_i_zdorovye = (By.CSS_SELECTOR, '[page_id="959"]')
assert_sumki_klatchi_ryukzaki = (By.CSS_SELECTOR, '[page_id="18931"]')
assert_gadzhety = (By.CSS_SELECTOR, '[page_id="965"]')
assert_detskiy_mir = (By.CSS_SELECTOR, '[page_id="969"]')
assert_podarki = (By.CSS_SELECTOR, '[page_id="976"]')
assert_avto = (By.CSS_SELECTOR, '[page_id="981"]')
assert_elektroinstrument = (By.CSS_SELECTOR, '[page_id="984"]')
assert_turizm_i_otdykh = (By.CSS_SELECTOR, '[page_id="735"]')
assert_vse_dlya_doma_i_dachi = (By.CSS_SELECTOR, '[page_id="734"]')
assert_vse_dlya_selskogo_khozyaystva = (By.CSS_SELECTOR, '[page_id="7936"]')
assert_mikroklimaticheskaya_tekhnika = (By.CSS_SELECTOR, '[page_id="1565"]')
assert_suvenirnaya_produktsiya = (By.CSS_SELECTOR, '[page_id="2277"]')
assert_vse_dlya_pitomtsev = (By.CSS_SELECTOR, '[page_id="5246"]')
assert_odezhda_i_obuv = (By.CSS_SELECTOR, '[page_id="5675"]')
assert_stroymaterialy = (By.CSS_SELECTOR, '[page_id="18957"]')
assert_utsenonnyye_tovary = (By.CSS_SELECTOR, '[page_id="5386"]')

# <---MENU in MENU--->
# <---РАСПРОДАЖА--->
rasprodazha = (By.CSS_SELECTOR, '[title="Осенняя распродажа"]')
# <---НОВОГОДНИЕ ТОВАРЫ--->
rasprodazha_novogodnikh_tovarov = (By.CSS_SELECTOR, '[title="Распродажа новогодних товаров"]')
novogodniye_derevya = (By.CSS_SELECTOR, '[title="Новогодние деревья (ели и сосны) и гирлянды"]')
girlyandy_i_venki = (By.CSS_SELECTOR, '[title="Новогодние гирлянды и венки"]')
yeli_i_sosny = (By.CSS_SELECTOR, '[title="Новогодние ели и сосны"]')
igrushki_statuetki = (By.CSS_SELECTOR, '[title="Новогодние игрушки, статуэтки и фигурки"]')
# <---ТОВАРЫ ДЛЯ КУХНИ--->

# <---footer--->
button_glavnaya = (By.CSS_SELECTOR, 'div.footer__menu__item [title="Главная"]')
button_novosti = (By.CSS_SELECTOR, 'div.footer__menu__item [title="Новости"]')
button_stati = (By.CSS_SELECTOR, 'div.footer__menu__item [title="Статьи"]')
button_o_magazine_foot = (By.CSS_SELECTOR, 'div.footer__menu__item [title="О магазине"]')
button_dostavka_i_oplata_foot = (By.CSS_SELECTOR, 'div.footer__menu__item'
                                                  '[title="Доставка и оплата"]')
button_kontakty = (By.CSS_SELECTOR, 'div.footer__menu__item [title="Контакты"]')

# <---assert footer and header--->
assert_novosti = (By.CSS_SELECTOR, '[page_id="5"]')
assert_stati = (By.CSS_SELECTOR, '[page_id="4"]')
assert_o_magazine_foot = (By.CSS_SELECTOR, '[page_id="47"]')
assert_dostavka_i_oplata_foot = (By.CSS_SELECTOR, '[page_id="48"]')
assert_kontakty = (By.CSS_SELECTOR, '[page_id="20"]')
assert_garantia = (By.CSS_SELECTOR, '[page_id="20621"]')
# <---zakazat--->
button_zakazat = (By.CSS_SELECTOR, '[class="teaser__catitem__list"] '
                                   'div.teaser__catitem:nth-of-type(1) div#id__buy__fast')
# <---assert zakazat--->
assert_zakazat = (By.CSS_SELECTOR, 'div.modal__window__title')

# <---dobavit_v_korzinu--->
button_dobavit_v_korzinu = (By.CSS_SELECTOR, '[class="teaser__catitem__list"] '
                                             'div.teaser__catitem:nth-of-type(1) a#id__add__to__cart')
# <---assert dobavit_v_korzinu--->
assert_dobavit_v_korzinu = (By.CSS_SELECTOR, '[page_id="14"]')
