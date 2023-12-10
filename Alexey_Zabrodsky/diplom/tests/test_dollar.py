import time

import pytest

import pytest_check as check
from Alexey_Zabrodsky.diplom.pages.home_page import HomePage
from Alexey_Zabrodsky.diplom.conftest import driver
from selenium.webdriver.common.action_chains import ActionChains
import allure


# <---О магазине--->
@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'О магазине'")
def test_link_header_1(driver):
    page = HomePage(driver)
    page.open()
    page.header_o_magazine()
    page.check_for_url_is_changed(page.get_current_url(), 'https://www.dollar.by/about')


@allure.suite("Валидность текста")
@allure.title("Проверка валидности текста кнопки 'О магазине'")
def test_link_header_1_1(driver):
    page = HomePage(driver)
    page.open()
    check.equal(page.header_o_magazine_text(), 'О магазине')


# <---Доставка и оплата--->
@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Доставка и оплата'")
def test_link_header_2(driver):
    page = HomePage(driver)
    page.open()
    page.header_dostavka_i_oplata()
    page.check_for_url_is_changed(page.get_current_url(), 'https://www.dollar.by/orders')


@allure.suite("Валидность текста")
@allure.title("Проверка валидности текста кнопки 'Доставка и оплата'")
def test_link_header_2_1(driver):
    page = HomePage(driver)
    page.open()
    check.equal(page.header_dostavka_i_oplata_text(), 'Доставка и оплата')


# <---Гарантия--->
@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Гарантия'")
def test_link_header_3(driver):
    page = HomePage(driver)
    page.open()
    page.header_garantiya()
    page.check_for_url_is_changed(page.get_current_url(), 'https://www.dollar.by/garantiya')


@allure.suite("Валидность текста")
@allure.title("Проверка валидности текста кнопки 'Гарантия'")
def test_link_header_3_1(driver):
    page = HomePage(driver)
    page.open()
    check.equal(page.header_garantiya_text(), 'Гарантия')


# <---Телеграм--->
@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Телеграм'")
def test_link_header_4(driver):
    page = HomePage(driver)
    page.open()
    page.header_telegram()
    driver.switch_to.window(driver.window_handles[1])
    page.check_for_url_is_changed(page.get_current_url(), 'https://t.me/dollar_by')


# <---Вайбер--->
@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Вайбер'")
def test_link_header_5(driver):
    page = HomePage(driver)
    page.open()
    page.header_viber()
    driver.switch_to.window(driver.window_handles[1])
    page.check_for_url_is_changed(page.get_current_url(), 'https://invite.viber.com/'
                                                          '?g2=AQBIWbyAVgCbg0%2B1SCjEk6Bag5eggt%'
                                                          '2FlNWuDPWLjmgnpuFeMEH5DJmQf93uWJwJK&'
                                                          'lang=ru')


# <---whatsapp--->
@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'whatsapp'")
def test_link_header_6(driver):
    page = HomePage(driver)
    page.open()
    page.header_whatsapp()
    driver.switch_to.window(driver.window_handles[1])
    page.check_for_url_is_changed(page.get_current_url(), 'https://api.whatsapp.com/'
                                                          'send/?phone=%2B375296041133&text&type='
                                                          'phone_number&app_absent=0')


@allure.suite("Валидность номера")
@allure.title("Проверка валидности номера в телеграм")
def test_link_header_6_1(driver):
    page = HomePage(driver)
    page.open()
    page.header_whatsapp()
    time.sleep(2)
    number = page.header_whatsapp_number()
    driver.switch_to.window(driver.window_handles[1])
    check.equal(number, '+375 29 604-11-33')


# <---Инстаграм--->
@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Инстаграм'")
def test_link_header_7(driver):
    page = HomePage(driver)
    page.open()
    page.header_instagram()
    page.check_for_url_is_changed(page.get_current_url(), 'https://www.instagram.com/dollar_by/')


# <---Facebook--->
@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Facebook'")
def test_link_header_8(driver):
    page = HomePage(driver)
    page.open()
    page.header_facebook()
    page.check_for_url_is_changed(page.get_current_url(), 'https://www.facebook.com/'
                                                          'shop.dollarby?_rdc=1&_rdr')


# <---VK--->
@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'VK'")
def test_link_header_9(driver):
    page = HomePage(driver)
    page.open()
    page.header_vk()
    page.check_for_url_is_changed(page.get_current_url(), 'https://vk.com/dollar_by')


# <---Номер velcom--->
@allure.suite("Валидность номера")
@allure.title("Проверка валидности текста номера 'velcom'")
def test_link_header_10_1(driver):
    page = HomePage(driver)
    page.open()
    check.equal(page.header_number_velcom(), '+375 29 604-11-33')


# <---Номер mts--->
@allure.suite("Валидность номера")
@allure.title("Проверка валидности текста номера 'mts'")
def test_link_header_10_2(driver):
    page = HomePage(driver)
    page.open()
    check.equal(page.header_number_mts(), '+375 29 882-11-33')


# <---Номер city--->
@allure.suite("Валидность номера")
@allure.title("Проверка валидности текста номера 'city'")
def test_link_header_10_3(driver):
    page = HomePage(driver)
    page.open()
    check.equal(page.header_number_city(), '+375 17 242-37-77')


# <---Корзина--->
@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Корзина'")
def test_link_header_11(driver):
    page = HomePage(driver)
    page.open()
    page.header_korzina()
    page.check_for_url_is_changed(page.get_current_url(), 'https://www.dollar.by/shopcart')


@allure.suite("Валидность текста")
@allure.title("Проверка валидности текста кнопки 'Корзина'")
def test_link_header_11_1(driver):
    page = HomePage(driver)
    page.open()
    check.equal(page.header_korzina_text(), 'Корзина:')


@allure.suite("Работа ссылок при скролле")
@allure.title("Проверка работы ссылки при скролле 'Корзина'")
def test_link_header_11_2(driver):
    page = HomePage(driver)
    page.open()
    driver.execute_script("window.scrollTo(0, 200)")
    page.header_korzina_mobile()
    page.check_for_url_is_changed(page.get_current_url(), 'https://www.dollar.by/shopcart')


# <---Поиск--->
@allure.suite("Работа поля поиска")
@allure.title("Проверка работы поля ввода 'Поиск'")
def test_link_header_12(driver):
    page = HomePage(driver)
    page.open()
    page.header_poisk()
    page.check_for_url_is_changed(page.get_current_url(), 'https://www.dollar.by/'
                                                          'search?q=%D0%9B%D0%B0%D0%BC%D0%BF%D'
                                                          '0%BE%D1%87%D0%BA%D0%B0')


# <---Поиск мобильный--->
@allure.suite("Работа поля поиска при скролле")
@allure.title("Проверка работы поля ввода 'Поиск'")
def test_link_header_12_1(driver):
    page = HomePage(driver)
    page.open()
    driver.execute_script("window.scrollTo(0, 200)")
    page.header_poisk_mobile()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/'
                                  'search?q=%D0%9B%D0%B0%D0%BC%D0%BF%D'
                                  '0%BE%D1%87%D0%BA%D0%B0')


# <--- Левое МЕНЮ --->
@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Новинки'")
def test_link_left_menu_1(driver):
    page = HomePage(driver)
    page.open()
    page.left_menu_novinki()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/Novinki')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Подарочные наборы'")
def test_link_left_menu_2(driver):
    page = HomePage(driver)
    page.open()
    page.left_menu_podarochnyye_nabor()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/podarochnyie-naboryi')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Распродажа'")
def test_link_left_menu_3(driver):
    page = HomePage(driver)
    page.open()
    page.left_menu_rasprodazha()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/rasprodazha')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Подарки для женщин'")
def test_link_left_menu_4(driver):
    page = HomePage(driver)
    page.open()
    page.left_menu_podarki_dlya_zhenshchin()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/Podarki-na-8-marta')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Выгодное предложение'")
def test_link_left_menu_5(driver):
    page = HomePage(driver)
    page.open()
    page.left_menu_profitable_proposition()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/Vygodnoe-predlozhenie')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Подарки для мужчин'")
def test_link_left_menu_6(driver):
    page = HomePage(driver)
    page.open()
    page.left_menu_podarki_dlya_muzhchin()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/18274')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Весенние скидки!'")
def test_link_left_menu_7(driver):
    page = HomePage(driver)
    page.open()
    page.left_menu_vesenniye_skidki()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/18275')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Новогодние товары'")
def test_link_left_menu_8(driver):
    page = HomePage(driver)
    page.open()
    page.left_menu_novogodniye_tovary()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/Novogodnie-tovary')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Товары для школы'")
def test_link_left_menu_9(driver):
    page = HomePage(driver)
    page.open()
    page.left_menu_tovary_dlya_shkoly()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/Tovary_dlya_shkoly')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Товары для кухни'")
def test_link_left_menu_10(driver):
    page = HomePage(driver)
    page.open()
    page.left_menu_tovary_dlya_kukhni()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/Tovary_dlya_kukhni')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Товары для дома'")
def test_link_left_menu_11(driver):
    page = HomePage(driver)
    page.open()
    page.left_menu_tovary_dlya_doma()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/the-goods-for-the-house')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Спортивные товары'")
def test_link_left_menu_12(driver):
    page = HomePage(driver)
    page.open()
    page.left_menu_sportivnyye_tovary()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/the-sports-goods')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Красота и здоровье'")
def test_link_left_menu_13(driver):
    page = HomePage(driver)
    page.open()
    page.left_menu_krasota_i_zdorovye()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/beauty-and-health')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Сумки, клатчи, рюкзаки'")
def test_link_left_menu_14(driver):
    page = HomePage(driver)
    page.open()
    page.left_menu_sumki_klatchi_ryukzaki()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/sumki-klatchi-ryukzaki')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Гаджеты'")
def test_link_left_menu_15(driver):
    page = HomePage(driver)
    page.open()
    page.left_menu_gadzhety()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/electronic-gadget')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Детский мир'")
def test_link_left_menu_16(driver):
    page = HomePage(driver)
    page.open()
    page.left_menu_detskiy_mir()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/the-childrens-world')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Подарки'")
def test_link_left_menu_17(driver):
    page = HomePage(driver)
    page.open()
    page.left_menu_podarki()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/gifts')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Авто'")
def test_link_left_menu_18(driver):
    page = HomePage(driver)
    page.open()
    page.left_menu_avto()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/car')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Электроинструмент'")
def test_link_left_menu_19(driver):
    page = HomePage(driver)
    page.open()
    page.left_menu_elektroinstrument()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/electric-instrument')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Туризм и Отдых'")
def test_link_left_menu_20(driver):
    page = HomePage(driver)
    page.open()
    page.left_menu_turizm_i_otdykh()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/turizm')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Все для дома и дачи'")
def test_link_left_menu_21(driver):
    page = HomePage(driver)
    page.open()
    page.left_menu_vse_dlya_doma_i_dachi()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/vse-dlja-doma-i-dachi')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Все для сельского хозяйства'")
def test_link_left_menu_22(driver):
    page = HomePage(driver)
    page.open()
    page.left_menu_vse_dlya_selskogo_khozyaystva()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/7936')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Микроклиматическая техника'")
def test_link_left_menu_23(driver):
    page = HomePage(driver)
    page.open()
    page.left_menu_mikroklimaticheskaya_tekhnika()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/1565')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Сувенирная продукция'")
def test_link_left_menu_24(driver):
    page = HomePage(driver)
    page.open()
    page.left_menu_suvenirnaya_produktsiya()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/Suvenirnaya-produktsiya')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Все для питомцев'")
def test_link_left_menu_25(driver):
    page = HomePage(driver)
    page.open()
    page.left_menu_vse_dlya_pitomtsev()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/5246')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Одежда и обувь'")
def test_link_left_menu_26(driver):
    page = HomePage(driver)
    page.open()
    page.left_menu_odezhda_i_obuv()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/5675')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Стройматериалы'")
def test_link_left_menu_27(driver):
    page = HomePage(driver)
    page.open()
    page.left_menu_stroymaterialy()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/18957')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Уценённые товары'")
def test_link_left_menu_28(driver):
    page = HomePage(driver)
    page.open()
    page.left_menu_utsenonnyye_tovary()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/5386')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Все статьи'")
def test_link_left_menu_29(driver):
    page = HomePage(driver)
    page.open()
    page.left_menu_stati()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/articles')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Все новости'")
def test_link_left_menu_30(driver):
    page = HomePage(driver)
    page.open()
    page.left_menu_novosti()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/news')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Осенняя распродажа'")
def test_link_left_menu_3_1(driver):
    page = HomePage(driver)
    actions = ActionChains(driver)
    page.open()
    element = page.left_menu_rasprodazha_mob_1()
    actions.move_to_element(element).perform()
    page.left_menu_rasprodazha_mob_2()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/'
                                  'rasprodazha/vesennyaya-rasprodazha')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Распродажа новогодних товаров'")
def test_link_left_menu_8_1(driver):
    page = HomePage(driver)
    actions = ActionChains(driver)
    page.open()
    element = page.left_menu_novogodnikh_tovarov_mob_1_2()
    actions.move_to_element(element).perform()
    page.left_menu_novogodnikh_tovarov_mob_1_1()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/'
                                  'Novogodnie-tovary/Rasprodazha-novogodnikh-tovarov')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Новогодние деревья (ели и сосны) и гирлянды'")
def test_link_left_menu_8_2(driver):
    page = HomePage(driver)
    actions = ActionChains(driver)
    page.open()
    element = page.left_menu_novogodnikh_tovarov_mob_2_2()
    actions.move_to_element(element).perform()
    page.left_menu_novogodnikh_tovarov_mob_2_1()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/'
                                  'the-goods-for-cleaning/Novogodnie-tovary/'
                                  'Novogodnie-derevya-eli-i-sosny-i-girlyandy')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Новогодние гирлянды и венки'")
def test_link_left_menu_8_3(driver):
    page = HomePage(driver)
    actions = ActionChains(driver)
    page.open()
    element = page.left_menu_novogodnikh_tovarov_mob_3_2()
    actions.move_to_element(element).perform()
    page.left_menu_novogodnikh_tovarov_mob_3_1()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/'
                                  'the-goods-for-cleaning/Novogodnie-tovary/'
                                  'Novogodnie-derevya-eli-i-sosny-i-girlyandy/'
                                  'Novogodnie-girlyandy-i-venki')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Новогодние ели и сосны'")
def test_link_left_menu_8_4(driver):
    page = HomePage(driver)
    actions = ActionChains(driver)
    page.open()
    element = page.left_menu_novogodnikh_tovarov_mob_4_2()
    actions.move_to_element(element).perform()
    page.left_menu_novogodnikh_tovarov_mob_4_1()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/'
                                  'the-goods-for-cleaning/Novogodnie-tovary/'
                                  'Novogodnie-derevya-eli-i-sosny-i-girlyandy/'
                                  'Novogodnie-eli-i-sosny')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Новогодние игрушки, статуэтки и фигурки'")
def test_link_left_menu_8_5(driver):
    page = HomePage(driver)
    actions = ActionChains(driver)
    page.open()
    element = page.left_menu_novogodnikh_tovarov_mob_5_2()
    actions.move_to_element(element).perform()
    page.left_menu_novogodnikh_tovarov_mob_5_1()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/'
                                  'the-goods-for-cleaning/Novogodnie-tovary/7496')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Распродажа товаров для кухни'")
def test_link_left_menu_10_1(driver):
    page = HomePage(driver)
    actions = ActionChains(driver)
    page.open()
    element = page.left_menu_tovary_dlya_kukhni_mob_1_2()
    actions.move_to_element(element).perform()
    page.left_menu_tovary_dlya_kukhni_mob_1_1()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/'
                                  'Tovary_dlya_kukhni/Rasprodazha-tovarov-dlya-kukhni')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Наборы посуды'")
def test_link_left_menu_10_2(driver):
    page = HomePage(driver)
    actions = ActionChains(driver)
    page.open()
    element = page.left_menu_tovary_dlya_kukhni_mob_2_2()
    actions.move_to_element(element).perform()
    page.left_menu_tovary_dlya_kukhni_mob_2_1()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/'
                                  'Tovary_dlya_kukhni/nabory-posudi')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Кастрюли'")
def test_link_left_menu_10_3(driver):
    page = HomePage(driver)
    actions = ActionChains(driver)
    page.open()
    element = page.left_menu_tovary_dlya_kukhni_mob_3_2()
    actions.move_to_element(element).perform()
    page.left_menu_tovary_dlya_kukhni_mob_3_1()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/Tovary_dlya_kukhni/931')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Кухонные, столовые принадлежности'")
def test_link_left_menu_10_4(driver):
    page = HomePage(driver)
    actions = ActionChains(driver)
    page.open()
    element = page.left_menu_tovary_dlya_kukhni_mob_4_2()
    actions.move_to_element(element).perform()
    page.left_menu_tovary_dlya_kukhni_mob_4_1()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/Tovary_dlya_kukhni/936')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Терки Овощерезки Кухонные'")
def test_link_left_menu_10_5(driver):
    page = HomePage(driver)
    actions = ActionChains(driver)
    page.open()
    driver.execute_script("window.scrollTo(0, 200)")
    element = page.left_menu_tovary_dlya_kukhni_mob_5_2()
    actions.move_to_element(element).perform()
    page.left_menu_tovary_dlya_kukhni_mob_5_1()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/Tovary_dlya_kukhni/937')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Терки Овощерезки Кухонные'")
def test_link_left_menu_10_5(driver):
    page = HomePage(driver)
    actions = ActionChains(driver)
    page.open()
    driver.execute_script("window.scrollTo(0, 200)")
    element = page.left_menu_tovary_dlya_kukhni_mob_5_2()
    actions.move_to_element(element).perform()
    page.left_menu_tovary_dlya_kukhni_mob_5_1()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/Tovary_dlya_kukhni/937')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Наборы ножей'")
def test_link_left_menu_10_6(driver):
    page = HomePage(driver)
    actions = ActionChains(driver)
    page.open()
    driver.execute_script("window.scrollTo(0, 200)")
    element = page.left_menu_tovary_dlya_kukhni_mob_6_2()
    actions.move_to_element(element).perform()
    page.left_menu_tovary_dlya_kukhni_mob_6_1()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/Tovary_dlya_kukhni/938')


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Для заточки ножей и ножниц'")
def test_link_left_menu_10_7(driver):
    page = HomePage(driver)
    actions = ActionChains(driver)
    page.open()
    driver.execute_script("window.scrollTo(0, 200)")
    element = page.left_menu_tovary_dlya_kukhni_mob_7_2()
    actions.move_to_element(element).perform()
    page.left_menu_tovary_dlya_kukhni_mob_7_1()
    page.check_for_url_is_changed(page.get_current_url(),
                                  'https://www.dollar.by/catalog/'
                                  'Tovary_dlya_kukhni/938/dlya-zatochki-nozhej-i-nozhnits')