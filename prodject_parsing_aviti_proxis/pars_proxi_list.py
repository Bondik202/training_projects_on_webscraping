import requests
from bs4 import BeautifulSoup
from random import choice


def proxi_adress():
    html = requests.get('https://free-proxy-list.net/').text
    soup = BeautifulSoup(html, 'lxml')

    main_list = soup.find('table', class_='table table-striped table-bordered').find('tbody').find_all('tr')
    proxis = []

    for i in main_list:
        td = i.find_all('td')
        id_adress = td[0].text.strip()
        port = td[1].text.strip()

        if td[6].text.strip() == 'yes':
            arhcetictura = 'https'
        else:
            arhcetictura = 'http'

        proxi = {'arhcetictura' : arhcetictura,
                 'addres': id_adress + ':' + port
                 }

        proxis.append(proxi)
    return choice(proxis)


def main():
    proxi_adress()

random_proxis_address = proxi_adress()
proxi_address = {random_proxis_address['arhcetictura']: random_proxis_address['addres']}


if __name__ == '__main__':
    main()