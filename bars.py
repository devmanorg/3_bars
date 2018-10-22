import json

#there would be a function to load data using API

def load_data(filepath):
    with open(filepath, encoding='utf-8') as data_file:
        return json.loads(data_file.read())


def get_biggest_bar(data):
    maximum_seats = max(bar['SeatsCount'] for bar in data)
    biggest_bars = []
    for bar in data:
        if bar['SeatsCount'] == maximum_seats:
            biggest_bars.append(bar)
    return biggest_bars


def get_smallest_bar(data):
    minimum_seats = min(bar['SeatsCount'] for bar in data)
    smallest_bars = []
    for bar in data:
        if bar['SeatsCount'] == minimum_seats:
            smallest_bars.append(bar)
    return smallest_bars


def get_closest_bar(data, longitude, latitude):
    return min(data, key=lambda bar:
               (bar['geoData']['coordinates'][1] - latitude) ** 2 +
               (bar['geoData']['coordinates'][0] - longitude) ** 2)


if __name__ == '__main__':
    filepath = input('Где лежит таблица с файлами? Укажи путь:')
    bars_data = load_data(filepath)
    biggest_bars = get_biggest_bar(bars_data)
    smallest_bars = get_smallest_bar(bars_data)
    for bar in biggest_bars:
        print('самый большой бар: %s, %s посадочных места'
              % (bar['Name'], bar['SeatsCount']))
    for bar in smallest_bars:
        print('самый маленький бар: %s, %s посадочных места'
              % (bar['Name'], bar['SeatsCount']))

    print('А теперь давай узнаем, какой бар ближе. Введи свои координаты.')
    print('Узнай в гугле, на какой широте ты находишься:')
    latitude = float(input())
    print('Отично, теперь узнай в гугле, на какой долготе ты находишься:')
    longitude = float(input())
    nearest_bar = get_closest_bar(bars_data, longitude, latitude)
    print('Ближайший бар: %s, находится по адресу: %s'
          % (nearest_bar['Name'], nearest_bar['Address']))
