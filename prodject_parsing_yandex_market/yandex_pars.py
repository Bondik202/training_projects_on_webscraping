import requests
from bs4 import BeautifulSoup
import csv
import fake_useragent


def get_html(url):
    user = fake_useragent.UserAgent().random
    headers = {
        'user-agent': user
    }
    response = requests.get(url, headers=headers)
    return response.text


def refine_tic(s):
    return s.split(' ')[-1]


def write_csv(data):
    with open('data.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],
                         data['url'],
                         data['snipet_text'],
                         data['tic']))


def page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    lis = soup.find_all('li', class_='yaca-snippet')

    for li in lis:
        try:
            name = li.find('h2').text.strip()
        except:
            name = ''
        try:
            url = li.find('a').get('href')
        except:
            url = ''
        try:
            snipet_text = li.find('div', class_='yaca-snippet__text').text.strip()
        except:
            snipet_text = ''
        try:
            t = li.find('div', class_='yaca-snippet__cy').text.strip()
            tic = refine_tic(t)
        except:
            tic = ''

        data = {
            'name': name,
            'url': url,
            'snipet_text': snipet_text,
            'tic': tic
        }
        write_csv(data)


def main():

    for i in range(1, 4):
        url = f'https://yacca.ru/cat/Entertainment/{i}.html'

        page_data(get_html(url))


if __name__ == '__main__':
    main()