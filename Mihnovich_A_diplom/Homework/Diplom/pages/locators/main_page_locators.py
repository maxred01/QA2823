from selenium.webdriver.common.by import By

TITLE_LOGO = (By.XPATH, '//div[@class="center-logo"]//a[@href="https://www.whitehouse.gov/"]')
LOGO = (By.CSS_SELECTOR, 'svg[id="holiday-2022-20"]')
ADMINISTRATION = (
    By.XPATH, '//li[@id="menu-item-61"]//a[@href="https://www.whitehouse.gov/administration/"]'
)
PRIORITIES = (
    By.XPATH, '//li[@id="menu-item-64"]//a[@href="https://www.whitehouse.gov/priorities/"]'
)
THE_RECORD = (
    By.XPATH, '//li[@id="menu-item-65469"]//a[@href="https://www.whitehouse.gov/therecord/"]'
)
BRIEFING = (
    By.XPATH, '//li[@id="menu-item-2787"]//a[@href="https://www.whitehouse.gov/briefing-room/"]'
)
LANGUAGE = (By.CSS_SELECTOR, 'li[id="menu-item-199"]')
MENU_BUTTON = (By.CSS_SELECTOR, 'span[id="mm-label"]')
SEARCH_BUTTON = (By.XPATH, '//main//button[@class="search-icon"]')
SEARCH_BUTTON_SUBMIT = (By.XPATH, '//main//button[@class="search-submit"]')
SEARCH_BUTTON_CLOSE = (By.XPATH, '//main//button[@class="search-close-icon"]')
SEARCH_FIELD = (By.XPATH, '//main//input[@class="search-field"]')

HEADER_MENU_ITEM = (By.XPATH, '//ul[@id="primary-navigation"]//li')
TOPICS = (By.XPATH, '//div[@class="homepage-taskbar-topics"]//li')
