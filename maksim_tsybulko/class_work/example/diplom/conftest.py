# import time, json, uuid, allure, pytest, requests, logging
#
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import base64
# from selenium.webdriver import DesiredCapabilities
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.proxy import *
#
#
# @allure.step("Waiting for resource availability {url}")
# def wait_url_data(url, timeout=11):
#     while timeout:
#         response = requests.get(url)
#         if not response.ok:
#             time.sleep(1)
#             timeout -= 1
#         else:
#             if 'video' in url:
#                 return response.content
#             else:
#                 return response.text
#     return None
#
#
# @pytest.fixture
# def chrome_options(chrome_options):
#     chrome_options.options = Options()
#     chrome_options.options.add_argument("--headless")
#     chrome_options.options.add_argument("--disable-gpu")
#     chrome_options.options.add_argument('--no-sandbox')
#     # chrome_options.add_argument('--log-level=DEBUG')
#     chrome_options.options.add_argument('--disable-dev-shm-usage')
#
#     return chrome_options
#
#
# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item):
#     # Эта функция помогает определить, что какой-то тест не прошел
#     # и передать эту информацию в отчет:
#
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item, "rep_" + rep.when, rep)
#     return rep
#
#
# def pytest_addoption(parser):
#     # parser.addoption("--browser", action="store", default="chrome")
#     parser.addoption("--browser")
#
#
# def download_video(session_id):
#     video_url = f"https://selenium.sandbox.hosterby.com/video/{session_id}.mp4"
#     response = requests.get(video_url)
#
#     if response.status_code == 200:
#         return base64.b64encode(response.content).decode("utf-8")
#     else:
#         print(f"Не удалось загрузить видео: {response.status_code}")
#         return None
#
#
# @pytest.fixture
# def web_browser(request, selenium):
#
#     browser = selenium
#     browser.set_window_size(1400, 1000)
#
#     # Вернуть экземпляр браузера в тестовый пример:
#     yield browser
#
#     if request.node.rep_call.failed:
#         # Сделать снимок экрана, если тест не прошёл:
#         try:
#             browser.execute_script("document.body.bgColor = 'white';")
#
#             # Сделать снимок экрана для локальной отладки:
#             browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')
#
#             # Прикрепить скриншот к отчету Allure:
#             allure.attach(browser.get_screenshot_as_png(),
#                           name=request.function.__name__,
#                           attachment_type=allure.attachment_type.PNG)
#
#             # Для отладки:
#             print('URL: ', browser.current_url)
#             print('Browser logs:')
#             for log in browser.get_log('browser'):
#                 print(log)
#
#         except:
#             pass  # игнорим все ошибки
#
#
# def get_test_case_docstring(item):
#     """ Эта функция получает строку документа из тестового примера и форматирует ее
#         отображая эту строку в документации вместо имени тестового примера в отчетах.
#     """
#
#     full_name = ''
#
#     if item._obj.__doc__:
#         # Удалить лишние пробелы из строки документа:
#         name = str(item._obj.__doc__.split('.')[0]).strip()
#         full_name = ' '.join(name.split())
#
#         # Сгенерировать список параметров для параметризованных тестовых случаев:
#         if hasattr(item, 'callspec'):
#             params = item.callspec.params
#
#             res_keys = sorted([k for k in params])
#             # Создать список на основе Dict:
#             res = ['{0}_"{1}"'.format(k, params[k]) for k in res_keys]
#             # Добавить dict со всеми параметрами к названию тестового примера:
#             full_name += ' Parameters ' + str(', '.join(res))
#             full_name = full_name.replace(':', '')
#
#     return full_name
#
#
# def pytest_itemcollected(item):
#     """ Эта функция изменяет имена тестовых случаев «на лету».
#         во время выполнения тест-кейсов.
#     """
#
#     if item._obj.__doc__:
#         item._nodeid = get_test_case_docstring(item)
#
#
# def pytest_collection_finish(session):
#     """ Эта функция изменяет имена тестовых случаев «на лету»
#         когда мы используем параметр --collect-only для pytest
#         (чтобы получить полный список всех существующих тестовых случаев).
#     """
#
#     if session.config.option.collectonly is True:
#         for item in session.items:
#             # Если в тестовом примере есть строка документа, нам нужно изменить ее имя на
#             # эту строку документа для отображения удобочитаемых отчетов и для
#             # автоматически импортировать тестовые случаи в систему управления тестированием.
#             if item._obj.__doc__:
#                 full_name = get_test_case_docstring(item)
#                 print(full_name)
#
#         pytest.exit('Done!')
#
#
# AUTHORIZATION_HEADERS = {
#     'Accept': 'application/json, text/plain, */*',
#     'Accept-Language': 'ru,en-US;q=0.9,en;q=0.8,ru-RU;q=0.7,pl;q=0.6',
#     'Connection': 'keep-alive',
#     'Origin': 'https://cp.hoster.by',
#     'Referer': 'https://cp.hoster.by/',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-site',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
#                   ' AppleWebKit/537.36 (KHTML, like Gecko)'
#                   ' Chrome/107.0.0.0 Safari/537.36',
#     'X-Origin': 'https://cp.hoster.by',
#     'sec-ch-ua': '"Google Chrome";v="107",'
#                  ' "Chromium";v="107",'
#                  ' "Not=A?Brand";v="24"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"macOS"',
#     'Cookie': 'BITRIX_SM_SALE_UID=49851516;'
#               ' user_227120=53013256;'
#               ' SOAPClient=unta60co0lil0u3sufj7n7vco7'
# }
#
#
# @pytest.fixture(scope='session')
# def token():
#     payload_authorization = {
#         "email": "maksim.tsibulko@hoster.by",
#         "password": "1qaz@WSX",
#         "remote": False,
#         "c_n_user": "227089",
#         "c_n_user_a": None
#     }
#
#     response_authorization = requests.post(
#         UrlLk.url_authorization,
#         headers=AUTHORIZATION_HEADERS,
#         json=payload_authorization,
#         timeout=10
#     ).json()
#
#     AUTHORIZATION_HEADERS.update({
#         'Authorization': f'Bearer {response_authorization["tokens"]["jwt_access"]}'
#     })
#
#     # response_refresh = requests.get(
#     #     UrlLk.url_refresh,
#     #     headers=AUTHORIZATION_HEADERS,
#     #     timeout=10
#     # ).json()
#
#     return response_authorization["tokens"]["jwt_access"]
#
#
# @pytest.fixture(scope='session')
# def base_header(token):
#     headers = AUTHORIZATION_HEADERS.copy()
#     headers['Authorization'] = f'Bearer {token}'
#     return headers
#
#
# @pytest.fixture(scope='session')
# def base_headers_for_registration():
#     """Fixture to provide base headers for registration."""
#     return AUTHORIZATION_HEADERS
