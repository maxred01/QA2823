from selenium.common import NoSuchElementException
from Alexey_Zabrodsky.diplom.pages.base_page import BasePage
from Alexey_Zabrodsky.diplom.pages.locators import home_page_locators
import allure


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        with allure.step("Перейти на главную страницу"):
            self.driver.get('https://www.dollar.by/')

# <---О магазине--->
    def header_o_magazine(self):
        with allure.step("Нажать кнопку о магазине на главном экране"):
            self.find_element(home_page_locators.button_o_magazine).click()

    def header_o_magazine_text(self):
        with allure.step("Проверка текста кнопки о магазине"):
            return self.find_element(home_page_locators.button_o_magazine).text

# <---Доставка и оплата--->
    def header_dostavka_i_oplata(self):
        with allure.step("Нажать кнопку Доставка и оплата на главном экране"):
            self.find_element(home_page_locators.button_dostavka_i_oplata).click()

    def header_dostavka_i_oplata_text(self):
        with allure.step("Проверка текста кнопки Доставка и оплата"):
            return self.find_element(home_page_locators.button_dostavka_i_oplata).text

# <---Гарантия--->
    def header_garantiya(self):
        with allure.step("Нажать кнопку Гарантия на главном экране"):
            self.find_element(home_page_locators.button_garantiya).click()

    def header_garantiya_text(self):
        with allure.step("Проверка текста кнопки Гарантия"):
            return self.find_element(home_page_locators.button_garantiya).text

# <---Телеграм--->
    def header_telegram(self):
        with allure.step("Нажать кнопку Телеграм на главном экране"):
            self.find_element(home_page_locators.button_telegram).click()

# <---Вайбер--->
    def header_viber(self):
        with allure.step("Нажать кнопку Вайбер на главном экране"):
            self.find_element(home_page_locators.button_viber).click()

# <---whatsapp--->
    def header_whatsapp(self):
        with allure.step("Нажать кнопку whatsapp на главном экране"):
            self.find_element(home_page_locators.button_watsapp).click()

    def header_whatsapp_number(self):
        with allure.step("Проверяем одинаковый ли номер whatsapp и номер на сайте"):
            return self.find_element(home_page_locators.number_velcom).text

# <---instagram--->
    def header_instagram(self):
        with allure.step("Нажать кнопку instagram на главном экране"):
            self.find_element(home_page_locators.button_instagram).click()

# <---Facebook--->
    def header_facebook(self):
        with allure.step("Нажать кнопку facebook на главном экране"):
            self.find_element(home_page_locators.button_facebook).click()

# <---VK--->
    def header_vk(self):
        with allure.step("Нажать кнопку vk на главном экране"):
            self.find_element(home_page_locators.button_vk).click()

# <---velcom--->
    def header_number_velcom(self):
        with allure.step("Проверка текста номера velcom"):
            return self.find_element(home_page_locators.number_velcom).text

# <---mts--->
    def header_number_mts(self):
        with allure.step("Проверка текста номера mts"):
            return self.find_element(home_page_locators.number_mts).text

# <---city--->
    def header_number_city(self):
        with allure.step("Проверка текста номера city"):
            return self.find_element(home_page_locators.number_city).text

# <---Корзина--->
    def header_korzina(self):
        with allure.step("Нажать кнопку Корзина на главном экране"):
            self.find_element(home_page_locators.button_korzina).click()

    def header_korzina_mobile(self):
        with allure.step("Нажать кнопку Корзина на главном экране"):
            self.find_element(home_page_locators.button_korzina_mobile).click()

    def header_korzina_text(self):
        with allure.step("Проверка текста кнопки Корзина"):
            return self.find_element(home_page_locators.button_korzina).text

# <---Поиск--->
    def header_poisk(self):
        with allure.step("Проверка поля Поиска"):
            self.find_element(home_page_locators.input_poisk).click()
            self.find_element(home_page_locators.input_poisk).send_keys('Лампочка')
            self.find_element(home_page_locators.button_poisk).click()

# <---Поиск мобильный--->
    def header_poisk_mobile(self):
        with allure.step("Проверка поля Поиска при скролле страницы"):
            self.find_element(home_page_locators.input_poisk_mobile).click()
            self.find_element(home_page_locators.input_poisk_mobile).send_keys('Лампочка')
            self.find_element(home_page_locators.button_poisk_mobile).click()

# <--- Левое МЕНЮ --->
# <--- Новинки --->
    def left_menu_novinki(self):
        with allure.step("Нажать кнопку Новинки в левом меню"):
            self.find_element(home_page_locators.button_novinki).click()

# <--- Подарочные наборы --->
    def left_menu_podarochnyye_nabor(self):
        with allure.step("Нажать кнопку Подарочные наборы в левом меню"):
            self.find_element(home_page_locators.button_podarochnyye_nabory).click()

# <--- Распродажа --->
    def left_menu_rasprodazha(self):
        with allure.step("Нажать кнопку Распродажа в левом меню"):
            self.find_element(home_page_locators.button_rasprodazha).click()

# <--- Подарки для женщин --->
    def left_menu_podarki_dlya_zhenshchin(self):
        with allure.step("Нажать кнопку Подарки для женщин в левом меню"):
            self.find_element(home_page_locators.button_podarki_dlya_zhenshchin).click()

# <--- Выгодное предложение --->
    def left_menu_profitable_proposition(self):
        with allure.step("Нажать кнопку Выгодное предложение в левом меню"):
            self.find_element(home_page_locators.button_profitable_proposition).click()

# <--- Подарки для мужчин --->
    def left_menu_podarki_dlya_muzhchin(self):
        with allure.step("Нажать кнопку Подарки для мужчин в левом меню"):
            self.find_element(home_page_locators.button_podarki_dlya_muzhchin).click()

# <--- Весенние скидки! --->
    def left_menu_vesenniye_skidki(self):
        with allure.step("Нажать кнопку Весенние скидки! в левом меню"):
            self.find_element(home_page_locators.button_vesenniye_skidki).click()

# <--- Новогодние товары --->
    def left_menu_novogodniye_tovary(self):
        with allure.step("Нажать кнопку Новогодние товары в левом меню"):
            self.find_element(home_page_locators.button_novogodniye_tovary).click()

# <--- Товары для школы --->
    def left_menu_tovary_dlya_shkoly(self):
        with allure.step("Нажать кнопку Товары для школы в левом меню"):
            self.find_element(home_page_locators.button_tovary_dlya_shkoly).click()

# <--- Товары для кухни --->
    def left_menu_tovary_dlya_kukhni(self):
        with allure.step("Нажать кнопку Товары для кухни в левом меню"):
            self.find_element(home_page_locators.button_tovary_dlya_kukhni).click()

# <--- Товары для дома --->
    def left_menu_tovary_dlya_doma(self):
        with allure.step("Нажать кнопку Товары для дома в левом меню"):
            self.find_element(home_page_locators.button_tovary_dlya_doma).click()

# <--- Спортивные товары --->
    def left_menu_sportivnyye_tovary(self):
        with allure.step("Нажать кнопку Спортивные товары в левом меню"):
            self.find_element(home_page_locators.button_sportivnyye_tovary).click()

# <--- Красота и здоровье --->
    def left_menu_krasota_i_zdorovye(self):
        with allure.step("Нажать кнопку Красота и здоровье в левом меню"):
            self.find_element(home_page_locators.button_krasota_i_zdorovye).click()

# <--- Сумки, клатчи, рюкзаки --->
    def left_menu_sumki_klatchi_ryukzaki(self):
        with allure.step("Нажать кнопку Сумки, клатчи, рюкзаки в левом меню"):
            self.find_element(home_page_locators.button_sumki_klatchi_ryukzaki).click()

# <--- Гаджеты --->
    def left_menu_gadzhety(self):
        with allure.step("Нажать кнопку Гаджеты в левом меню"):
            self.find_element(home_page_locators.button_gadzhety).click()

# <--- Детский мир --->
    def left_menu_detskiy_mir(self):
        with allure.step("Нажать кнопку Детский мир в левом меню"):
            self.find_element(home_page_locators.button_detskiy_mir).click()

# <--- Подарки --->
    def left_menu_podarki(self):
        with allure.step("Нажать кнопку Подарки в левом меню"):
            self.find_element(home_page_locators.button_podarki).click()

# <--- Авто --->
    def left_menu_avto(self):
        with allure.step("Нажать кнопку Авто в левом меню"):
            self.find_element(home_page_locators.button_avto).click()

# <--- Электроинструмент --->
    def left_menu_elektroinstrument(self):
        with allure.step("Нажать кнопку Электроинструмент в левом меню"):
            self.find_element(home_page_locators.button_elektroinstrument).click()

# <--- Туризм и Отдых --->
    def left_menu_turizm_i_otdykh(self):
        with allure.step("Нажать кнопку Туризм и Отдых в левом меню"):
            self.find_element(home_page_locators.button_turizm_i_otdykh).click()

# <--- Все для дома и дачи --->
    def left_menu_vse_dlya_doma_i_dachi(self):
        with allure.step("Нажать кнопку Все для дома и дачи в левом меню"):
            self.find_element(home_page_locators.button_vse_dlya_doma_i_dachi).click()

# <--- Все для сельского хозяйства --->
    def left_menu_vse_dlya_selskogo_khozyaystva(self):
        with allure.step("Нажать кнопку Все для сельского хозяйства в левом меню"):
            self.find_element(home_page_locators.button_vse_dlya_selskogo_khozyaystva).click()

# <--- Микроклиматическая техника --->
    def left_menu_mikroklimaticheskaya_tekhnika(self):
        with allure.step("Нажать кнопку Микроклиматическая техника в левом меню"):
            self.find_element(home_page_locators.button_mikroklimaticheskaya_tekhnika).click()

# <--- Сувенирная продукция --->
    def left_menu_suvenirnaya_produktsiya(self):
        with allure.step("Нажать кнопку Сувенирная продукция в левом меню"):
            self.find_element(home_page_locators.button_suvenirnaya_produktsiya).click()

# <--- Все для питомцев --->
    def left_menu_vse_dlya_pitomtsev(self):
        with allure.step("Нажать кнопку Все для питомцев в левом меню"):
            self.find_element(home_page_locators.button_vse_dlya_pitomtsev).click()

# <--- Одежда и обувь --->
    def left_menu_odezhda_i_obuv(self):
        with allure.step("Нажать кнопку Одежда и обувь в левом меню"):
            self.find_element(home_page_locators.button_odezhda_i_obuv).click()

# <--- Стройматериалы --->
    def left_menu_stroymaterialy(self):
        with allure.step("Нажать кнопку Стройматериалы в левом меню"):
            self.find_element(home_page_locators.button_stroymaterialy).click()

# <--- Уценённые товары --->
    def left_menu_utsenonnyye_tovary(self):
        with allure.step("Нажать кнопку Уценённые товары в левом меню"):
            self.find_element(home_page_locators.button_utsenonnyye_tovary).click()

# <--- Все статьи --->
    def left_menu_stati(self):
        with allure.step("Нажать кнопку Все статьи в левом меню"):
            self.find_element(home_page_locators.button_vse_stati).click()

# <--- Все новости --->
    def left_menu_novosti(self):
        with allure.step("Нажать кнопку Все новости в левом меню"):
            self.find_element(home_page_locators.button_vse_novosti).click()

# <--- Разделы левого меню --->
# <--- Осенняя распродажа --->
    def left_menu_rasprodazha_mob_2(self):
        with allure.step("Нажать кнопку Осенняя распродажа в левом меню"):
            self.find_element(home_page_locators.rasprodazha_osen).click()

    def left_menu_rasprodazha_mob_1(self):
        with allure.step("Навести на кнопку Распродажа в левом меню"):
            return self.find_element(home_page_locators.button_rasprodazha)

# <--- Распродажа новогодних товаров --->
    def left_menu_novogodnikh_tovarov_mob_1_1(self):
        with allure.step("Нажать кнопку Распродажа новогодних товаров в левом меню"):
            self.find_element(home_page_locators.rasprodazha_novogodnikh_tovarov).click()

    def left_menu_novogodnikh_tovarov_mob_1_2(self):
        with allure.step("Навести на кнопку Новогодние товары в левом меню"):
            return self.find_element(home_page_locators.button_novogodniye_tovary)

# <--- Новогодние деревья (ели и сосны) и гирлянды --->
    def left_menu_novogodnikh_tovarov_mob_2_1(self):
        with allure.step("Нажать кнопку Новогодние деревья (ели и сосны) и гирлянды в левом меню"):
            self.find_element(home_page_locators.novogodniye_derevya).click()

    def left_menu_novogodnikh_tovarov_mob_2_2(self):
        with allure.step("Навести на кнопку Новогодние товары в левом меню"):
            return self.find_element(home_page_locators.button_novogodniye_tovary)

# <--- Новогодние гирлянды и венки --->
    def left_menu_novogodnikh_tovarov_mob_3_1(self):
        with allure.step("Нажать кнопку Новогодние гирлянды и венки в левом меню"):
            self.find_element(home_page_locators.girlyandy_i_venki).click()

    def left_menu_novogodnikh_tovarov_mob_3_2(self):
        with allure.step("Навести на кнопку Новогодние товары в левом меню"):
            return self.find_element(home_page_locators.button_novogodniye_tovary)

# <--- Новогодние ели и сосны --->
    def left_menu_novogodnikh_tovarov_mob_4_1(self):
        with allure.step("Нажать кнопку Новогодние ели и сосны в левом меню"):
            self.find_element(home_page_locators.yeli_i_sosny).click()

    def left_menu_novogodnikh_tovarov_mob_4_2(self):
        with allure.step("Навести на кнопку Новогодние товары в левом меню"):
            return self.find_element(home_page_locators.button_novogodniye_tovary)

# <--- Новогодние игрушки, статуэтки и фигурки --->
    def left_menu_novogodnikh_tovarov_mob_5_1(self):
        with allure.step("Нажать кнопку Новогодние игрушки, статуэтки и фигурки в левом меню"):
            self.find_element(home_page_locators.igrushki_statuetki).click()

    def left_menu_novogodnikh_tovarov_mob_5_2(self):
        with allure.step("Навести на кнопку Новогодние товары в левом меню"):
            return self.find_element(home_page_locators.button_novogodniye_tovary)

# <--- Распродажа товаров для кухни --->
    def left_menu_tovary_dlya_kukhni_mob_1_1(self):
        with allure.step("Нажать кнопку Распродажа товаров для кухни в левом меню"):
            self.find_element(home_page_locators.rasprodazha_kukhni).click()

    def left_menu_tovary_dlya_kukhni_mob_1_2(self):
        with allure.step("Навести на кнопку Товаров для кухни в левом меню"):
            return self.find_element(home_page_locators.button_tovary_dlya_kukhni)

# <--- Наборы посуды --->
    def left_menu_tovary_dlya_kukhni_mob_2_1(self):
        with allure.step("Нажать кнопку Наборы посуды в левом меню"):
            self.find_element(home_page_locators.nabory_posudy).click()

    def left_menu_tovary_dlya_kukhni_mob_2_2(self):
        with allure.step("Навести на кнопку Товаров для кухни в левом меню"):
            return self.find_element(home_page_locators.button_tovary_dlya_kukhni)

# <--- Кастрюли --->
    def left_menu_tovary_dlya_kukhni_mob_3_1(self):
        with allure.step("Нажать кнопку Кастрюли в левом меню"):
            self.find_element(home_page_locators.kastryuli).click()

    def left_menu_tovary_dlya_kukhni_mob_3_2(self):
        with allure.step("Навести на кнопку Товаров для кухни в левом меню"):
            return self.find_element(home_page_locators.button_tovary_dlya_kukhni)

# <--- Кухонные, столовые принадлежности --->
    def left_menu_tovary_dlya_kukhni_mob_4_1(self):
        with allure.step("Нажать кнопку Кухонные, столовые принадлежности в левом меню"):
            self.find_element(home_page_locators.kukhonnyye_stolovyye).click()

    def left_menu_tovary_dlya_kukhni_mob_4_2(self):
        with allure.step("Навести на кнопку Товаров для кухни в левом меню"):
            return self.find_element(home_page_locators.button_tovary_dlya_kukhni)

# <--- Терки Овощерезки Кухонные --->
    def left_menu_tovary_dlya_kukhni_mob_5_1(self):
        with allure.step("Нажать кнопку Терки Овощерезки Кухонные в левом меню"):
            self.find_element(home_page_locators.terki_ovoshcherezki).click()

    def left_menu_tovary_dlya_kukhni_mob_5_2(self):
        with allure.step("Навести на кнопку Товаров для кухни в левом меню"):
            return self.find_element(home_page_locators.button_tovary_dlya_kukhni)

# <--- Наборы ножей --->
    def left_menu_tovary_dlya_kukhni_mob_6_1(self):
        with allure.step("Нажать кнопку Наборы ножей в левом меню"):
            self.find_element(home_page_locators.nabory_nozhey).click()

    def left_menu_tovary_dlya_kukhni_mob_6_2(self):
        with allure.step("Навести на кнопку Товаров для кухни в левом меню"):
            return self.find_element(home_page_locators.button_tovary_dlya_kukhni)

# <--- Для заточки ножей и ножниц --->
    def left_menu_tovary_dlya_kukhni_mob_7_1(self):
        with allure.step("Нажать кнопку Для заточки ножей и ножниц в левом меню"):
            self.find_element(home_page_locators.dlya_zatochki_nozhey).click()

    def left_menu_tovary_dlya_kukhni_mob_7_2(self):
        with allure.step("Навести на кнопку Товаров для кухни в левом меню"):
            return self.find_element(home_page_locators.button_tovary_dlya_kukhni)