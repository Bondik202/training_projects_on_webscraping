import requests
from bs4 import BeautifulSoup
import csv

def response_main_link(url):
    response = requests.get(url).text
    return response


def writer_csv(data):
    with open('baseyni.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([data['name'],
                         data['link'],
                         data['price'],
                         data['manual']])


def link_category_product(html):
    soup = BeautifulSoup(html, 'lxml')
    section = soup.find('section', class_='elementor-section elementor-top-section elementor-element elementor-element-90ec1a4 elementor-section-boxed elementor-section-height-default elementor-section-height-default')
    ul_li_elements = section.find('div', class_='jet-woo-products-wrapper').find('ul', class_='jet-woo-builder-categories--columns products').find_all('li')

    for lis in ul_li_elements:
        li = lis.find('div', class_='elementor-widget-container').find('a').get('href')
        for i in range(1, 4 + 1):
            soup_category_product(response_link_product(li + f'page/{i}/'))


def response_link_product(url):
    response = requests.get(url).text
    return response


def soup_category_product(html):
    soup = BeautifulSoup(html, 'lxml')

    try:
        section = soup.find('section', class_='elementor-section elementor-top-section elementor-element elementor-element-90ec1a4 elementor-section-boxed elementor-section-height-default elementor-section-height-default')
        all_elenents = section.find('div', class_='elementor-widget-wrap')
        ul_li_elenents = all_elenents.find('div', class_='jet-woo-products-wrapper').find('ul').find_all('li')

        for li in ul_li_elenents:
            global link_card_product
            link_card_product = li.find('div', class_='elementor-widget-container').find('span', class_='jet-woo-builder-archive-product-title').find('a').get('href')
            all_data_main_product(response_card_product(link_card_product))
    except Exception as error:
        print(error)


def response_card_product(url):
    response = requests.get(url).text
    return response


def all_data_main_product(html):
    soup = BeautifulSoup(html, 'lxml')

    name_product = soup.find('section', class_='elementor-section elementor-top-section elementor-element elementor-element-6e4a055 elementor-section-boxed elementor-section-height-default elementor-section-height-default').find('div', class_='elementor-widget-container').find('h2').text

    all_elements = soup.find('section', class_='elementor-section elementor-top-section elementor-element elementor-element-5b05afd elementor-section-boxed elementor-section-height-default elementor-section-height-default').find('div', class_='elementor-row')

    price_product = all_elements.find('section', class_='elementor-section elementor-inner-section elementor-element elementor-element-6a91976 elementor-section-boxed elementor-section-height-default elementor-section-height-default').find('span').find('bdi').text.strip('₽').split()
    price_product = ''.join(price_product)

    link_product_card = link_card_product

    manual_text = all_elements.find('div', class_='woocommerce-product-details__short-description').find('p').text

    data = {
        'name': name_product,
        'price': price_product,
        'link': link_product_card,
        'manual': manual_text
    }
    writer_csv(data)
    print(data)


def main():
    url = 'https://zodiac-store.ru/shop/'
    link_category_product(response_main_link(url))


if __name__ == '__main__':
    main()