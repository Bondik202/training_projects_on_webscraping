import requests
from data_api_vk import OWNER_ID, TOKEN, V, DOMAIN, COUNT, URL, ALBUM_ID, ALBUM_IDS
import time
import re
import csv
import datetime


def writer_csv(data):

    with open('data_user.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([data['user-link'],
                         data['link_comment_photos'],
                         data['name_user'],
                         data['name_produkt'],
                         data['price_rub'],
                         data['title_album'],
                         data['data_time']])


def main():

    response_photos_get_all_comments = requests.get(URL + 'photos.getAllComments', params={
        'owner_id': OWNER_ID,
        'access_token': TOKEN,
        'v': V,
        'count': COUNT,
        'album_id': ALBUM_ID
    })

    response_photos_get_all_comments_json = response_photos_get_all_comments.json()
    all_comments_text = response_photos_get_all_comments_json['response']['items']

    time.sleep(1)

    for j in all_comments_text:

        user_link = j['from_id']
        comment_text = j['pid']

        response_user_name = requests.get(URL + 'users.get', params={
            'user_ids': user_link,
            'access_token': TOKEN,
            'v': V,
            'count': COUNT
        })

        response_user_name_json = response_user_name.json()
        response_all = response_user_name_json['response'][0]
        first_name = response_all['first_name']
        last_name = response_all['last_name']
        name_user = last_name + ' ' + first_name

        user = 'https://vk.com/id' + str(user_link)  # ссылка на страницу юзера
        link_comment_photos = 'https://vk.com/photo-17557338_' + str(comment_text)  # ссылка на фотографию с комментарием юзера
        time_stamp = j['date']
        data_time = datetime.datetime.fromtimestamp(time_stamp)

        response_get_photos = requests.get(URL + 'photos.get', params={
                    'owner_id': OWNER_ID,
                    'access_token': TOKEN,
                    'v': V,
                    'count': 1,
                    'album_id': ALBUM_ID,
                    'photo_ids': comment_text
                    })

        response_json_get_photos = response_get_photos.json()
        text_photos = response_json_get_photos['response']['items']  # все эллементы метода(фото)

        response_album_id = requests.get(URL + 'photos.getAlbums', params={
            'owner_id': OWNER_ID,
            'access_token': TOKEN,
            'v': V,
            'count': COUNT,
            'album_ids': ALBUM_ID
        })
        response_album_id_json = response_album_id.json()
        title_album = response_album_id_json['response']['items'][0]['title']

        time.sleep(1)

        for i in text_photos:
            text1 = i['text']
            name_produkt = i['text'][:i['text'].find('\n'):]  # получаем название продукта
            price_rub_spisok = re.findall(r'[-+]?\d+ руб', text1)  # получаем цену списком

            try:
                price_rub = price_rub_spisok[0] # распоковываем список с ценой
                price_rub_str = price_rub.split(' ') #сплитуем по пробелу
                price_rub_int = price_rub_str[0]
                price_rub_int = int(price_rub_int)
            except:
                price_rub_int = 'цены на странице нет'

        data = {
            'user-link': user,
            'link_comment_photos': link_comment_photos,
            'name_user': name_user,
            'name_produkt': name_produkt,
            'price_rub': price_rub_int,
            'data_time': data_time,
            'title_album': title_album
        }
        print(data)
        writer_csv(data)

    time.sleep(1)


if __name__ == '__main__':
    main()