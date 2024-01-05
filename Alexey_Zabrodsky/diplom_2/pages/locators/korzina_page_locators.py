import os
from Alexey_Zabrodsky.diplom_2.pages.base_page import WebPage
from Alexey_Zabrodsky.diplom_2.pages.elements import WebElement
from Alexey_Zabrodsky.diplom_2.pages.elements import ManyWebElements


class KorzinaBtn(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("KORZINA") or 'https://www.dollar.by/'

        super().__init__(web_driver, url)


