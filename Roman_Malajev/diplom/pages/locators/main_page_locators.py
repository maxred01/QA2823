from selenium.webdriver.common.by import By

#header
search_field = (By.CSS_SELECTOR, '[placeholder="Введите запрос"]')
search_button = (By.CSS_SELECTOR, '[id="search-icon-legacy"]')
burger_button = (By.XPATH, '//div[@id="start"]//yt-icon-button[@id="guide-button"]')
keyboard_button = (By.CSS_SELECTOR, '[id="gs_st50"]')
options_button = (By.CSS_SELECTOR, '[class="style-scope ytd-topbar-menu-button-renderer style-default"]')
header_login_button = (By.XPATH, '(//a[@aria-label="Войти"]//div[@class="yt-spec-touch-feedback-shape__fill"])[1]')

#left menu
history_button = (By.XPATH, '(//a[@href="/feed/history"])[1]')
subscriptions_button = (By.XPATH, '(//a[@href="/feed/subscriptions"])[1]')
shorts_button = (By.XPATH, '(//a[@id="endpoint" and @title="Shorts"])[1]')
left_login_button = (By.XPATH, '(//a[@aria-label="Войти"]//div[@class="yt-spec-touch-feedback-shape__fill"])[2]')
main_button = (By.XPATH, '(//a[@href="/" and @title="Главная"])[1]')
you_button = (By.XPATH, '(//a[@href="/feed/you" and @title="Вы"])[1]')

#categories
categoria_music_button = (By.XPATH, '//yt-formatted-string[@id="text" and @title="Музыка"]')
categoria_videogames_button = (By.XPATH, '//yt-formatted-string[@id="text" and @title="Видеоигры"]')
categoria_streams_button = (By.XPATH, '//yt-formatted-string[@id="text" and @title="Сейчас в эфире"]')
categoria_sitcoms_button = (By.XPATH, '//yt-formatted-string[@id="text" and @title="Ситкомы"]')
categoria_sketch_button = (By.XPATH, '//yt-formatted-string[@id="text" and @title="Скетч-шоу"]')
categoria_animation_button = (By.XPATH, '//yt-formatted-string[@id="text" and @title="Анимация"]')
categoria_rap_button = (By.XPATH, '//yt-formatted-string[@id="text" and @title="Рэп"]')
categoria_action_and_adventures_button = (By.XPATH, '//yt-formatted-string[@id="text" and @title="Экшен и приключения"]')
categoria_nature_button = (By.XPATH, '//yt-formatted-string[@id="text" and @title="Природа"]')
categoria_recently_published_button = (By.XPATH, '//yt-formatted-string[@id="text" and @title="Недавно опубликованные"]')
