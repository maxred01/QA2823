import json
import time

import allure
import pytest_check as check
import requests

def test_func():

  url = "https://www.onliner.by/"

  payload = {}
  headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'stid=b415db1da8ec5a55caba6a7b5aa510dab3f2a6b6b38845386790768213b260c7; _ym_uid=1699984348686418250; _ym_d=1699984348; _ga=GA1.1.117778634.1699984348; tmr_lvid=3a960b0e3bf4692ff04509e64e37b48f; tmr_lvidTS=1699984348027; ouid=snyBDGV4lUR2vz0BA+t5Ag==; _ga_4Y6NQKE48G=GS1.1.1702401352.3.1.1702403037.60.0.0; _ym_isad=2; ADC_REQ_2E94AF76E7=B4D16C465D4FE99DA9AA7676627C795F099B92EEFABEC7687BF5BC89A31FCF2E8607748D74F841AA; _ga_9FSEQ8JYKN=GS1.1.1703007792.7.1.1703007793.0.0.0; _ga_NG54S9EFTD=GS1.1.1703007792.6.1.1703007793.59.0.0; _ga_KPSB9MHYED=GS1.1.1703007792.7.1.1703007793.59.0.0; _ym_visorc=b; tmr_detect=0%7C1703007796487',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  with allure.step('Проверка статус кода'):
    assert response.status_code == 200
    print(response.headers)

  with allure.step('Проверка Content-Type'):
    check.equal(response.headers['Content-Type'], 'text/html; charset=utf-8', 'Content type отсутствует')

  with allure.step('Проверка метода'):
    check.equal(response.request.method, 'GET', 'Метод не GET')

  with allure.step('Проверка скорости ответа сервера'):
    start_time = time.time()
    requests.request("GET", url, headers=headers, data=payload)
    end_time = time.time()
    final_time = end_time - start_time
    check.less(final_time, 0.2, 'долго отвечает')

def test_func_2():

  url = "https://catalog.onliner.by/api/seo"

  payload = json.dumps({
    "url": "https://catalog.onliner.by/washingmachine?mfr%5B0%5D=atlant"
  })
  headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Cookie': 'stid=b415db1da8ec5a55caba6a7b5aa510dab3f2a6b6b38845386790768213b260c7; _ym_uid=1699984348686418250; _ym_d=1699984348; _ga=GA1.1.117778634.1699984348; tmr_lvid=3a960b0e3bf4692ff04509e64e37b48f; tmr_lvidTS=1699984348027; ouid=snyBDmVWTHq3byHsBLXJAg==; _ym_isad=2; catalog_session=yWb6xCOcEvXQbEyEdthUAiUyR7NsKnIMVgRpVh8W; ADC_REQ_2E94AF76E7=12A282FB122FF49D561B530D323FD80A7F867BC75221A44E9A44B60814B60FD997FC319F3DC23956; _gcl_au=1.1.1693568075.1703009587; _fbp=fb.1.1703009587288.2085379274; _tt_enable_cookie=1; _ttp=Cywqp6sX4gH0UXFPGu2hMYHaFHC; delivery_boarding_showed=true; detached_cart_id=6bf5e5b6-9e9b-11ee-ad2f-44a8423a93d9; detached_state_id=1473408e-f614-5aa8-a03a-1b5652549bc2; fingerprint=cc96140c-3ad0-42f0-8e69-8789db98673d; compare=[%22onebladeqp252020%22]; _ga_SMLMFQCWFM=GS1.1.1703011551.1.1.1703011916.60.0.0; __gads=ID=03bbf47d19957520:T=1703009587:RT=1703011916:S=ALNI_Mak2SQOv1LDEhMdScccM0H177KauA; __gpi=UID=00000d21c047def4:T=1703009587:RT=1703011916:S=ALNI_Ma7N5VUIZzHV1ERp27HO9-qFg779A; tmr_detect=0%7C1703011919902; _ym_visorc=b; _ga_9FSEQ8JYKN=GS1.1.1703011932.8.1.1703012068.0.0.0; _ga_KPSB9MHYED=GS1.1.1703011932.8.1.1703012079.60.0.0; _ga_NG54S9EFTD=GS1.1.1703007792.6.1.1703012079.60.0.0; _ga_4Y6NQKE48G=GS1.1.1703009581.4.1.1703012092.36.0.0; fingerprint=cc96140c-3ad0-42f0-8e69-8789db98673d',
    'Origin': 'https://catalog.onliner.by',
    'Referer': 'https://catalog.onliner.by/washingmachine?mfr%5B0%5D=atlant',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.text)

  with allure.step('Проверка статус кода'):
    assert response.status_code == 200

  with allure.step('Проверка сообщения об ошибке'):
    pass