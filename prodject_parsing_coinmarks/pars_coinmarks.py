import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    response = requests.get(url)
    return response.text


def get_all_links(html):
    soup = BeautifulSoup(html, 'lxml')
    links = soup.find('tbody').find_all('tr')
    lis = []
    for i in links:
        td = 'https://coinmarketcap.com/ru' + i.find('a').get('href')
        lis.append(td)
    return lis


def main_response(urls):
    for i in range(len(urls)):
        url = urls[i]
        response = requests.get(url).text
        get_soup(response)


def csv_writer(data):
    with open('datas.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([data['Рейтинг'],
                         data['Логотип'],
                         data['Имя'],
                         data['Ссылка на сайт']])


def get_soup(response):
    soup = BeautifulSoup(response, 'lxml')
    try:
        name = soup.find('div', class_='sc-103s2w8-0 eAmmwa').find('span').text
    except:
        name = 'Имя продукта отсутствует'
    try:
        logo = soup.find('div', class_='sc-16r8icm-0 gpRPnR nameHeader___27HU_').find('small').text
    except:
        logo = 'Логотип продукта отсутствует'
    try:
        link_web_site = soup.find('ul', class_='content___MhX1h').find('li').find('a').get('href')
    except:
        link_web_site = 'Вэб сайт продукта отсутствует'
    try:
        reiteng = soup.find('div', class_='sc-16r8icm-0 bILTHz').find('div', class_='namePill___3p_Ii namePillPrimary___2-GWA').text
    except:
        reiteng = 'Рейтинг продукта отсутствует'

    data = {
        'Рейтинг': reiteng,
        'Логотип': logo,
        'Имя': name,
        'Ссылка на сайт': link_web_site,
    }
    csv_writer(data)

def main():

    for i in range(1, 57 + 1):
        url = f'https://coinmarketcap.com/ru/?page={i}'
        print('КОЛИЧЕСТВО СТРАНИЦ ПРОШЕДШИХ ОБРАБОТКУ', i)
        main_response(get_all_links(get_html(url)))


if __name__ == '__main__':
    main()
