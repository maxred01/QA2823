import os
from Alexey_Zabrodsky.diplom_2.pages.base_page import WebPage
from Alexey_Zabrodsky.diplom_2.pages.elements import WebElement
from Alexey_Zabrodsky.diplom_2.pages.elements import ManyWebElements


class FuterBtn(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("FUTER") or 'https://onliner.by/'

        super().__init__(web_driver, url)

    # О компании
    btn_futer_about = WebElement(xpath='//footer//a[@href="https://blog.onliner.by/about"]')

    # Контакты редакции
    btn_futer_contacts = WebElement(xpath='//footer//a[@href="https://people.onliner.by/contacts"]')
