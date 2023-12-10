import os
from QA2823.maksim_tsybulko.class_work.example.diplom.pages.base_page import WebPage
from QA2823.maksim_tsybulko.class_work.example.diplom.pages.elements import WebElement
from QA2823.maksim_tsybulko.class_work.example.diplom.pages.elements import ManyWebElements


class FuterBtn(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("FUTER") or 'https://onliner.by/'

        super().__init__(web_driver, url)

    # О компании
    btn_futer_about = WebElement(xpath='//footer//a[@href="https://blog.onliner.by/about"]')

    # Контакты редакции
    btn_futer_contacts = WebElement(xpath='//footer//a[@href="https://people.onliner.by/contacts"]')
