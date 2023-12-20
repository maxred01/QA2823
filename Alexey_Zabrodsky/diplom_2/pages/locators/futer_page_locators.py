import os
from Alexey_Zabrodsky.diplom_2.pages.base_page import WebPage
from Alexey_Zabrodsky.diplom_2.pages.elements import WebElement
from Alexey_Zabrodsky.diplom_2.pages.elements import ManyWebElements


class FuterBtn(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("FUTER") or 'https://www.dollar.by/'

        super().__init__(web_driver, url)


    button_glavnaya = WebElement(css_selector='div.footer__menu__item [title="Главная"]')
    button_novosti = WebElement(css_selector='div.footer__menu__item [title="Новости"]')
    button_stati = WebElement(css_selector='div.footer__menu__item [title="Статьи"]')
    button_o_magazine_foot = WebElement(css_selector='div.footer__menu__item [title="О магазине"]')
    button_dostavka_i_oplata_foot = WebElement(css_selector='div.footer__menu__item '
                                                        '[title="Доставка и оплата"]')
    button_kontakty = WebElement(css_selector='div.footer__menu__item [title="Контакты"]')
