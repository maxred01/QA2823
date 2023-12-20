import time
import pytest_check as check
import allure

from Alexey_Zabrodsky.diplom_2.pages.locators.header_page_locators import HeaderBtn
from Alexey_Zabrodsky.diplom_2.pages.locators.futer_page_locators import FuterBtn

from Alexey_Zabrodsky.diplom_2.conftest import web_browser


@allure.feature('Смоук тест')
@allure.story('Имитация скролла в низ экрана и нажатия кнопок хедера')
def test_header_btn_1(web_browser):
    """ Убеждаемся, что ссылки/кнопки хедера
        кликабельные и переход на страницу корректный. """

    page = HeaderBtn(web_browser)

    # with allure.step("Проверка кнопки 'О магазине'"):
    #     if check.equal(page.button_o_magazine.get_text(), 'О магазине'):
    #         check.equal(page.button_o_magazine.get_attribute('href'), 'https://www.dollar.by/about')
    #         page.button_o_magazine.click(1)
    #         page1 = page.get_current_url()
    #         check.equal(page1, 'https://www.dollar.by/about')
    #         check.is_true(page.button_o_magazine.wait_for_visibility())
    #         check.is_true(page.button_o_magazine.wait_to_be_clickable())
    #
    # with allure.step("Проверка кнопки 'Доставка и оплата'"):
    #     if check.equal(page.button_dostavka_i_oplata.get_text(), 'Доставка и оплата'):
    #         check.equal(page.button_dostavka_i_oplata.get_attribute('href'), 'https://www.dollar.by/orders')
    #         page.button_dostavka_i_oplata.click(1)
    #         page1 = page.get_current_url()
    #         check.equal(page1, 'https://www.dollar.by/orders')
    #         check.is_true(page.button_dostavka_i_oplata.wait_for_visibility())
    #         check.is_true(page.button_dostavka_i_oplata.wait_to_be_clickable())
    #
    # with allure.step("Проверка кнопки 'Гарантия'"):
    #     if check.equal(page.button_garantiya.get_text(), 'Гарантия'):
    #         check.equal(page.button_garantiya.get_attribute('href'), 'https://www.dollar.by/garantiya')
    #         page.button_garantiya.click(1)
    #         page1 = page.get_current_url()
    #         check.equal(page1, 'https://www.dollar.by/garantiya')
    #         check.is_true(page.button_garantiya.wait_for_visibility())
    #         check.is_true(page.button_garantiya.wait_to_be_clickable())
    #
    # with allure.step("Проверка кнопки 'Корзина'"):
    #     if check.equal(page.button_korzina.get_text(), 'Корзина:'):
    #         check.equal(page.button_korzina.get_attribute('href'), 'https://www.dollar.by/shopcart')
    #         page.button_korzina.click(1)
    #         page1 = page.get_current_url()
    #         check.equal(page1, 'https://www.dollar.by/shopcart')
    #         check.is_true(page.button_korzina.wait_for_visibility())
    #         check.is_true(page.button_korzina.wait_to_be_clickable())
    #
    # with allure.step("Проверка кнопки 'Лого'"):
    #     if check.equal(page.button_logo.get_attribute('href'), 'https://www.dollar.by/'):
    #         page.button_logo.click(1)
    #         page1 = page.get_current_url()
    #         check.equal(page1, 'https://www.dollar.by/')
    #         check.is_true(page.button_logo.wait_for_visibility())
    #         check.is_true(page.button_logo.wait_to_be_clickable())
    #
    # with allure.step("Проверка кнопки 'Поиск'"):
    #     if check.equal(page.button_poisk.get_text(), 'Поиск'):
    #         page.button_poisk.click(1)
    #         page1 = page.get_current_url()
    #         check.equal(page1, 'https://www.dollar.by/search?q=')
    #         check.is_true(page.button_poisk.wait_for_visibility())
    #         check.is_true(page.button_poisk.wait_to_be_clickable())
    #         time.sleep(4)
    #
    # with allure.step("Проверка кнопки Header-mini 'Лого'"):
    #     page.execute_script("window.scrollTo(0, 200)")
    #     time.sleep(4)
    #     if check.equal(page.button_logo_mini.get_attribute('href'), 'https://www.dollar.by/'):
    #         check.is_true(page.button_logo_mini.wait_for_visibility())
    #         check.is_true(page.button_logo_mini.wait_to_be_clickable())
    #         page.button_logo_mini.click(1)
    #         page1 = page.get_current_url()
    #         check.equal(page1, 'https://www.dollar.by/')
    #
    # with allure.step("Проверка кнопки Header-mini 'Поиск'"):
    #     page.execute_script("window.scrollTo(0, 200)")
    #     if check.equal(page.button_poisk_mini.get_text(), 'Поиск'):
    #         check.is_true(page.button_poisk_mini.wait_for_visibility())
    #         check.is_true(page.button_poisk_mini.wait_to_be_clickable())
    #         page.button_poisk_mini.click(1)
    #         page1 = page.get_current_url()
    #         check.equal(page1, 'https://www.dollar.by/search?q=')
    #
    # with allure.step("Проверка кнопки Header-mini 'Корзина'"):
    #     page.execute_script("window.scrollTo(0, 200)")
    #     if check.equal(page.button_korzina_mini.get_attribute('href'), 'https://www.dollar.by/shopcart'):
    #         check.equal(page.button_korzina_mini.get_text(), 'Корзина:')
    #         check.is_true(page.button_korzina_mini.wait_for_visibility())
    #         check.is_true(page.button_korzina_mini.wait_to_be_clickable())
    #         page.button_korzina_mini.click(1)
    #         page1 = page.get_current_url()
    #         check.equal(page1, 'https://www.dollar.by/shopcart')
    #
    # with allure.step("Проверка раскрывающего окна при наведении Header-mini 'Информация с номерами'"):
    #     page.execute_script("window.scrollTo(0, 200)")
    #     if check.is_true(page.button_info_mini.wait_for_visibility()):
    #         check.is_true(page.button_info_mini.wait_to_be_clickable())
    #         page.button_info_mini.move_to()
    #         page.button_info_mini.wait_for_clickability_and_visibility()
    #
    # with allure.step("Проверка номера 'А1' Header and Header-mini"):
    #     if check.equal(page.number_A1.get_attribute('title'), '+375296041133'):
    #         check.is_true(page.number_A1.wait_for_visibility())
    #         num = page.number_A1.get_attribute('title')
    #         page.execute_script("window.scrollTo(0, 200)")
    #         page.button_info_mini.move_to()
    #         check.is_true(page.number_A1_mini.wait_for_visibility())
    #         check.equal(num, page.number_A1_mini.get_attribute('title'))
    #
    with allure.step("Проверка номера 'mts' Header and Header-mini"):
        if check.equal(page.number_mts.get_attribute('title'), '+375298821133'):
            check.is_true(page.number_mts.wait_for_visibility())
            num = page.number_mts.get_attribute('title')
            page.execute_script("window.scrollTo(0, 200)")
            page.button_info_mini.move_to()
            check.is_true(page.number_mts_mini.wait_for_visibility())
            check.equal(num, page.number_mts_mini.get_attribute('title'))


@allure.feature('Смоук тест')
@allure.story('Имитация скролла в низ экрана и нажатие кнопоки Инстаграм')
def test_header_btn_2(web_browser):
    """ Убеждаемся, что ссылка/кнопка Инстаграм
        кликабельна и переход на страницу корректный. """

    page = HeaderBtn(web_browser)

    with allure.step("Проверка кнопки 'Инстаграм'"):
        if check.equal(page.button_instagram.get_attribute('href'), 'https://www.instagram.com/dollar_by'):
            check.is_true(page.button_instagram.wait_for_visibility())
            check.is_true(page.button_instagram.wait_to_be_clickable())
            page.button_instagram.click(1)
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.instagram.com/dollar_by')


@allure.feature('Смоук тест')
@allure.story('Имитация скролла в низ экрана и нажатие кнопоки Фейсбук')
def test_header_btn_3(web_browser):
    """ Убеждаемся, что ссылка/кнопка Фейсбук
        кликабельна и переход на страницу корректный. """

    page = HeaderBtn(web_browser)
    with allure.step("Проверка кнопки 'Фейсбук'"):
        if check.equal(page.button_facebook.get_attribute('href'), 'https://web.facebook.com/shop.dollarby'):
            check.is_true(page.button_facebook.wait_for_visibility())
            check.is_true(page.button_facebook.wait_to_be_clickable())
            page.button_facebook.click(1)
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.facebook.com/shop.dollarby?_rdc=1&_rdr')
            time.sleep(3)


@allure.feature('Смоук тест')
@allure.story('Имитация скролла в низ экрана и нажатие кнопоки Телеграм')
def test_header_btn_4(web_browser):
    """ Убеждаемся, что ссылка/кнопка Телеграм
        кликабельна и переход на страницу корректный. """

    page = HeaderBtn(web_browser)
    with allure.step("Проверка кнопки 'Телеграм'"):
        if check.equal(page.button_telegram.get_attribute('href'), 'https://t.me/dollar_by'):
            check.is_true(page.button_telegram.wait_for_visibility())
            check.is_true(page.button_telegram.wait_to_be_clickable())
            page.button_telegram.click(1)
            page.switch_to_window(1)
            page1 = page.get_current_url()
            check.equal(page1, 'https://t.me/dollar_by')


@allure.feature('Смоук тест')
@allure.story('Имитация скролла в низ экрана и нажатие кнопоки Вайбер')
def test_header_btn_5(web_browser):
    """ Убеждаемся, что ссылка/кнопка Вайбер
        кликабельна и переход на страницу корректный. """

    page = HeaderBtn(web_browser)
    with allure.step("Проверка кнопки 'Вайбер'"):
        if check.equal(page.button_viber.get_attribute('href'), 'https://invite.viber.com/'
                                                                '?g2=AQBIWbyAVgCbg0%2B1SCjEk6'
                                                                'Bag5eggt%2FlNWuDPWLjmgnpuFeM'
                                                                'EH5DJmQf93uWJwJK'):
            check.is_true(page.button_viber.wait_for_visibility())
            check.is_true(page.button_viber.wait_to_be_clickable())
            page.button_viber.click(1)
            page.switch_to_window(1)
            page1 = page.get_current_url()
            check.equal(page1, 'https://invite.viber.com/?g2=AQBIWbyAVgCbg0%2B'
                               '1SCjEk6Bag5eggt%2FlNWuDPWLjmgnpuFeMEH5DJmQf93uWJwJK&lang=ru')


@allure.feature('Смоук тест')
@allure.story('Имитация скролла в низ экрана и нажатие кнопоки Ватцап')
def test_header_btn_6(web_browser):
    """ Убеждаемся, что ссылка/кнопка Ватцап
        кликабельна и переход на страницу корректный. """

    page = HeaderBtn(web_browser)
    with allure.step("Проверка кнопки 'Ватцап'"):
        if check.equal(page.button_watsapp.get_attribute('href'), 'https://wa.me/+375296041133'):
            check.is_true(page.button_watsapp.wait_for_visibility())
            check.is_true(page.button_watsapp.wait_to_be_clickable())
            page.button_watsapp.click(1)
            page.switch_to_window(1)
            page1 = page.get_current_url()
            check.equal(page1, 'https://api.whatsapp.com/send/?phone=%2B375296041133&text&type'
                               '=phone_number&app_absent=0')


@allure.feature('Смоук тест')
@allure.story('Имитация скролла в низ экрана и нажатия кнопок футера')
def test_futer(web_browser):
    """ Убеждаемся, что ссылки/кнопки футера
        кликабельные и переход на страницу корректный. """

    page = FuterBtn(web_browser)

    with allure.step("Проверка кнопки 'Главная'"):
        if check.equal(page.button_glavnaya.get_text(), 'Главная'):
            check.equal(page.button_glavnaya.get_attribute('href'), 'https://www.dollar.by/')
            page.button_glavnaya.click(1)
            page1 = page.get_current_url()
            check.equal(page1, 'https://www.dollar.by/')
            check.is_true(page.button_glavnaya.wait_for_visibility())
            check.is_true(page.button_glavnaya.wait_to_be_clickable())

    # with allure.step("Проверка кнопки 'Доставка и оплата'"):
    #     if check.equal(page.button_dostavka_i_oplata.get_text(), 'Доставка и оплата'):
    #         check.equal(page.button_dostavka_i_oplata.get_attribute('href'), 'https://www.dollar.by/orders')
    #         page.button_dostavka_i_oplata.click(1)
    #         page1 = page.get_current_url()
    #         check.equal(page1, 'https://www.dollar.by/orders')
    #         check.is_true(page.button_dostavka_i_oplata.wait_for_visibility())
    #         check.is_true(page.button_dostavka_i_oplata.wait_to_be_clickable())