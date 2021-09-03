import requests
import csv


def response(url):
    respons = requests.get(url)
    html_page = respons.json()
    return html_page


def writer_csv(data):
    with open('football.csv', 'a') as f:
        write = csv.writer(f)
        write.writerow([data['name'],
                        data['city'],
                        data['region'],
                        data['poind'],
                        data['game']])


def get_item(html):
    main_item = html['items'][0]['data'][0]['standings']

    for i in main_item:
        name = i['team']['title']
        city = i['team']['city']['title']
        region = i['team']['region']['title']
        game = i['total']['played']
        poinds = i['total']['points']

        data = {
            'name': name,
            'city': city,
            'region': region,
            'game': game,
            'poind':poinds
        }
        writer_csv(data)


def main():
    list_wed = ['league-1', 'bundesliga', 'seria-a', 'primera-division',
                'epl', 'russia-cup', 'fnl', 'rpl']

    for i in range(len(list_wed)):
        url = f'https://api.sport24.ru/hub/v1/statistics/widget/competitions/{list_wed[i]}/standings?seasonUrn=2021-22'
        get_item(response(url))


if __name__ == '__main__':
    main()