from selenium.webdriver.common.by import By

#header
search_field = (By.CSS_SELECTOR, '[placeholder="Введите запрос"]')
search_button = (By.CSS_SELECTOR, '[id="search-icon-legacy"]')
burger_button = (By.XPATH, '//div[@id="start"]//yt-icon-button[@id="guide-button"]')
keyboard_button = (By.CSS_SELECTOR, '[id="gs_st50"]')
options_button = (By.CSS_SELECTOR, '[class="style-scope ytd-topbar-menu-button-renderer style-default"]')
header_login_button = (By.XPATH, '(//a[@aria-label="Войти"]//div[@class="yt-spec-touch-feedback-shape__fill"])[1]')
voice_search_button = (By.CSS_SELECTOR, '[class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--overlay-touch-response"]')

#header_settings
your_data_button = (By.CSS_SELECTOR, '[href="https://myaccount.google.com/u/0/yourdata/youtube?hl=ru"]')
theme_button = (By.CSS_SELECTOR, '[role="option"]')
language_button = (By.XPATH, '(//div[@id="items"]//ytd-compact-link-renderer[@class="style-scope yt-multi-page-menu-section-renderer"])[2]')
safemode_button = (By.XPATH, '(//div[@id="items"]//ytd-compact-link-renderer[@class="style-scope yt-multi-page-menu-section-renderer"])[3]')
country_button = (By.XPATH, '(//div[@id="items"]//ytd-compact-link-renderer[@class="style-scope yt-multi-page-menu-section-renderer"])[4]')
hotkeys_button = (By.XPATH, '(//div[@id="items"]//ytd-compact-link-renderer[@class="style-scope yt-multi-page-menu-section-renderer"])[5]')
inner_options_button = (By.XPATH, '(//div[@id="items"]//ytd-compact-link-renderer[@class="style-scope yt-multi-page-menu-section-renderer"])[6]')
inner_about_button = (By.XPATH, '(//div[@id="items"]//ytd-compact-link-renderer[@class="style-scope yt-multi-page-menu-section-renderer"])[7]')
inner_send_report_button = (By.XPATH, '(//div[@id="items"]//ytd-compact-link-renderer[@class="style-scope yt-multi-page-menu-section-renderer"])[8]')

#left menu
history_button = (By.XPATH, '(//a[@href="/feed/history"])[1]')
subscriptions_button = (By.XPATH, '(//a[@href="/feed/subscriptions"])[1]')
shorts_button = (By.XPATH, '(//a[@id="endpoint" and @title="Shorts"])[1]')
left_login_button = (By.XPATH, '(//a[@aria-label="Войти"]//div[@class="yt-spec-touch-feedback-shape__fill"])[2]')
main_button = (By.XPATH, '(//a[@href="/" and @title="Главная"])[1]')
you_button = (By.XPATH, '(//a[@href="/feed/you" and @title="Вы"])[1]')
trend_button = (By.XPATH, '(//a[@title="В тренде"])[1]')
music_button = (By.XPATH, '(//a[@title="Музыка"])[1]')
translations_button = (By.XPATH, '(//a[@title="Трансляции"])[1]')
videogames_button = (By.XPATH, '(//a[@title="Видеоигры"])[1]')
sport_button = (By.XPATH, '(//a[@title="Спорт"])[1]')
catalogue_button = (By.CSS_SELECTOR, '[href="/feed/guide_builder"]')
premium_button = (By.CSS_SELECTOR, '[href="/premium"]')
yt_music_button = (By.CSS_SELECTOR, '[href="https://music.youtube.com/"]')
yt_kids_button = (By.CSS_SELECTOR, '[href="https://www.youtubekids.com/?source=youtube_web"]')
settings_button = (By.XPATH, '//a[@href="/account" and @title="Настройки"]')
reports_button = (By.XPATH, '//a[@href="/reporthistory"]')
about_button = (By.XPATH, '//a[@title="Справка"]')
send_report_button = (By.XPATH, '//a[@title="Отправить отзыв"]')

#left menu close buttons

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

#videos
videos = (By.XPATH, '//div[@class="style-scope ytd-rich-item-renderer"]')
videos_img = (By.XPATH, '//div[@id="content"]//img[@style="background-color: transparent;"]')

