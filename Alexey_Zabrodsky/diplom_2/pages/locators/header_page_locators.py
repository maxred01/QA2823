import os
from Alexey_Zabrodsky.diplom_2.pages.base_page import WebPage
from Alexey_Zabrodsky.diplom_2.pages.elements import WebElement
from Alexey_Zabrodsky.diplom_2.pages.elements import ManyWebElements


class HeaderBtn(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("HEADER") or 'https://www.dollar.by/'

        super().__init__(web_driver, url)

    # О магазине
    button_o_magazine = WebElement(css_selector='div.header__menu__item:nth-of-type(1) a')
    # Доставка и оплата
    button_dostavka_i_oplata = WebElement(css_selector='div.header__menu__item:nth-of-type(2) a')
    # Гарантия
    button_garantiya = WebElement(css_selector='div.header__menu__item:nth-of-type(3) a')
    # Инстаграм
    button_instagram = WebElement(css_selector='div.header div.header__social_links a:nth-of-type(1)')
    # Фейсбук
    button_facebook = WebElement(css_selector='div.header div.header__social_links a:nth-of-type(2)')