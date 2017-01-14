import json


def load_data(filepath):
    with open(filepath, encoding='utf-8') as data_file:
        bar_data = json.loads(data_file.read())
    return bar_data


def get_biggest_bar(data):
    print('самый большой бар:')
    max_seats = 0
    for bar in data:
        if bar['SeatsCount'] > max_seats:
            max_seats = bar['SeatsCount']
    for bar in data:
        if bar['SeatsCount'] == max_seats:
            print(bar['Name'], ', ', max_seats, ' посадочных места')
    print(' ')


def get_smallest_bar(data):
    print('самый маленький бар:')
    min_seats = data[1]['SeatsCount']
    for bar in data:
        if bar['SeatsCount'] < min_seats:
            min_seats = bar['SeatsCount']
    for bar in data:
        if bar['SeatsCount'] == min_seats:
            print(bar['Name'], ', ', min_seats, ' посадочных места')


def get_closest_bar(data, longitude, latitude):
    bar_latitude = data[1]['geoData']['coordinates'][1]
    bar_longitude = data[1]['geoData']['coordinates'][0]
    shortest_distance = (bar_latitude - latitude) ** 2 + (bar_longitude - longitude) ** 2
    for bar in data:
        bar_latitude = bar['geoData']['coordinates'][1]
        bar_longitude = bar['geoData']['coordinates'][0]
        distance = (bar_latitude - latitude) ** 2 + (bar_longitude - longitude) ** 2
        if distance < shortest_distance:
            nearest_bar = bar['Name']
            nearest_bar_address = bar['Address']
            shortest_distance = distance
    print('Ближайший бар: ', nearest_bar)
    print(nearest_bar_address)


if __name__ == '__main__':
    # getting the path for datafile
    print('Где лежит таблица с файлами? Укажи путь:')
    filepath = str(input())
    # open data in json
    bar_data = load_data(filepath)
    get_biggest_bar(bar_data)
    get_smallest_bar(bar_data)
    # getting longitude
    print('А теперь давай узнаем, какой бар ближе. Введи свои координаты.')
    print('Узнай в гугле, на какой широте ты находишься:')
    latitude = float(input())
    print('Отично, теперь узнай в гугле, на какой долготе ты находишься:')
    longitude = float(input())
    get_closest_bar(bar_data, longitude, latitude)
