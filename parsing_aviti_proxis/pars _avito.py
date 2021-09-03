import requests
from bs4 import BeautifulSoup
import time
import csv
from pars_proxi_list import proxi_address
import fake_useragent


def get_response(url):
    fake_user_agent = fake_useragent.UserAgent().random
    headers = {
        'user-agent': fake_user_agent
    }
    response = requests.get(url, proxies=proxi_address, headers=headers)
    return response.text


def writer_csv(data):
    with open('telefon_avito.csv', 'a') as f:
        writ = csv.writer(f)
        writ.writerows([data['telefon']])


def get_html_link(html):
    soup = BeautifulSoup(html, 'lxml')
    links = soup.find('div', class_='items-items-kAJAg').find_all('div', class_='iva-item-root-Nj_hb photo-slider-slider-_PvpN iva-item-list-H_dpX iva-item-redesign-nV4C4 iva-item-responsive-gIKjW items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum')

    for i in links:
        time.sleep(1)
        card = 'https://www.avito.ru' + i.find('div', class_='iva-item-body-R_Q9c').find('div', class_='iva-item-titleStep-_CxvN').find('a').get('href')
        link_index = card[-1:-11:-1]
        link_index = link_index[-1:-11:-1]
    get_main_response(link_index)


def get_main_response(url):
        url_index = f'https://m.avito.ru/api/1/items/{url}/phone?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'
        r = requests.get(url_index)
        respons = r.json()
        try:
            namber = respons['result']['action']['uri']
            tel = namber[-1:-12:-1]
            tels = tel[-1:-12:-1]
        except Exception as e:
            print(str(e))

        data = {
            'telefon': tels
        }
        writer_csv(data)


def main():
    for i in range(1, 5 + 1):
        time.sleep(1)
        url = f'https://www.avito.ru/sankt-peterburg/avtomobili?radius=0&p={i}'
        get_html_link(get_response(url))


if __name__ == '__main__':
    main()

