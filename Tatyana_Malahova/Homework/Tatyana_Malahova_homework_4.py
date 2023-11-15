import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
option = Options()
driver = webdriver.Chrome()
driver.maximize_window()


def print_webpage_data(url: str, locator: str):
    try:
        driver.get(url)
        element = driver.find_element(By.XPATH, locator).text
        print(element)
        print(driver.title)
        print(driver.current_url)
        # print(driver.page_source)
    except NoSuchElementException:
        print("NoSuchElementDetected on link:", url)
    finally:
        time.sleep(1)




google_url = "https://www.google.com/"
google_locator = "//div[@id='SIvCob']"
print_webpage_data(google_url, google_locator)

youtube_url = "https://www.youtube.com/"
youtube_locator = "(//yt-formatted-string[@id='video-title'])[1]"
print_webpage_data(youtube_url, youtube_locator)

facebook_url = "https://www.facebook.com/"
facebook_locator = "//h2[@class='_8eso']"
print_webpage_data(facebook_url, facebook_locator)

instagram_url = "https://www.instagram.com/"
instagram_locator = "//*[text()='У вас ещё нет аккаунта? ']"
print_webpage_data(instagram_url, instagram_locator)

twitter_url = "https://twitter.com/"
twitter_locator = "(//span[@class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'])[2]"
print_webpage_data(twitter_url, twitter_locator)

baidu_url = "https://www.baidu.com/"
baidu_locator = "(//span[@class='title-content-title'])[3]"
print_webpage_data(baidu_url, baidu_locator)

wikipedia_url = "https://www.wikipedia.org/"
wikipedia_locator = "//strong[@class='jsl10n localized-slogan']"
print_webpage_data(wikipedia_url, wikipedia_locator)

yahoo_url = "https://www.yahoo.com/?guccounter=1"
yahoo_locator = "//a[@class='_yb_io0r2 _yb_1hru9 _yb_1jh73 _yb_1gfxm']"
print_webpage_data(yahoo_url, yahoo_locator)

dzen_url = "https://dzen.ru/?yredirect=true"
dzen_locator = "(//span[@class='card-news-story__text-3F'])[1]"
print_webpage_data(dzen_url, dzen_locator)

whatsapp_url = "https://www.whatsapp.com/"
whatsapp_locator = "(//div[@class='_8l_f'])[6]"
print_webpage_data(whatsapp_url, whatsapp_locator)

amazon_url = "https://www.amazon.com/"
amazon_locator = "(//a[@class='nav-a  '])[2]"
print_webpage_data(amazon_url, amazon_locator)

tiktok_url = "https://www.tiktok.com/explore"
tiktok_locator = "//h2[@id='login-modal-title']"
print_webpage_data(tiktok_url, tiktok_locator)


driver.close()
driver.quit()

