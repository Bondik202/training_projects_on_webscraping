import requests
from bs4 import BeautifulSoup
import csv


def writer_csv(data):
    with open('avto_bmw.csv', 'a') as f:
        write = csv.writer(f)
        write.writerow([data['headers_one'],
                        data['headers_two'],
                        data['headers_three']])


def main():
    list_cars = ['bmw1', 'bmw2', 'bmw3', 'bmw4', 'bmw5', 'bmw6', 'bmw7', 'bmw8', 'bmwi', 'bmwX1', 'bmwX2', 'bmwX3', 'bmwX4', 'bmwX5', 'bmwX6', 'bmwX7', 'bmwZ', 'mini', 'moto', 'rolls-royce']

    for i in range(len(list_cars)):
        try:
            url = f'https://cats.parts/{list_cars[i]}'
            response = requests.get(url).text
            soup = BeautifulSoup(response, 'lxml')
            main_item = soup.find('div', class_='etk-series-wrapper').find('div', class_='etk-series-box').find('div', class_='etk-series-cells').find_all('a')
        except:
            pass

        for j in main_item:
            try:
                link_car_moto_object = 'https://cats.parts' + j.get('href')
                response = requests.get(link_car_moto_object).text
                soup = BeautifulSoup(response, 'lxml')
                main_card_car = soup.find('div', class_='etk-models-bodies-layer').find_all('div')
            except:
                pass

            for g in main_card_car:
                try:
                    link_car_gard = link_car_moto_object + g.find('div').find('a').get('href') + 'all/'
                    mehanik_detal = requests.get(link_car_gard).text
                    soup_mehabik = BeautifulSoup(mehanik_detal, 'lxml')
                    main_sektion = soup_mehabik.find('div', class_='etk-hg-wrapper').find('ul', class_='etk-hg-list').find_all('li')

                except:
                    pass

                for k in main_sektion:
                    try:
                        elements = link_car_gard + k.find('a').get('href')
                        elements_groop = requests.get(elements).text
                        soup_element_groop = BeautifulSoup(elements_groop, 'lxml')
                        element = soup_element_groop.find('div', class_='etk-nodes-wrapper').find('ul', class_='etk-nodes-list').find_all('li')
                    except:
                        pass

                    for l in element:
                        try:
                            url_item_final = elements + l.find('a').get('href')
                            respons_final = requests.get(url_item_final).text
                            soup_final = BeautifulSoup(respons_final, 'lxml')

                            headers_one = soup_final.find('div', class_='page-caption etk-caption').find('h1').text

                            headers_two = soup_final.find('h2').text

                            headers_three = soup_final.find('h3').text

                            data = {
                                'headers_one': headers_one,
                                'headers_two': headers_two,
                                'headers_three': headers_three
                            }
                            writer_csv(data)

                        except:
                            pass


if __name__ == '__main__':
    main()