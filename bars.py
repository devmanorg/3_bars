import json
from math import sqrt


def load_data(filepath):
    my_file = open(filepath, mode="r", encoding='utf-8')
    json_data = json.load(my_file)
    my_file.close()
    return json_data


def get_biggest_bar(data):
    max_seats_count = 0
    bar_list = []
    for bar in data:
        if bar['Cells']['SeatsCount'] > max_seats_count:
            max_seats_count = bar['Cells']['SeatsCount']
    for bar in json_data:
        if bar['Cells']['SeatsCount'] == max_seats_count:
            bar_list.append(bar['Cells']['Name'])
    if len(bar_list) >= 2:
        print('Самые большие бары Москвы: ')
        for x in bar_list:
            print('   ' + x)
    elif len(bar_list) <= 0:
        print("Больших баров не найдено!")
    else:
        print('Самый большой бар в Москве: ' + bar_list[0])


def get_smallest_bar(data):
    max_seats_count = 0
    bar_list = []
    for bar in data:
        if bar['Cells']['SeatsCount'] > max_seats_count:
            max_seats_count = bar['Cells']['SeatsCount']
    min_seats_count = max_seats_count
    for bar in data:
        if bar['Cells']['SeatsCount'] < min_seats_count:
            min_seats_count = bar['Cells']['SeatsCount']
    for bar in json_data:
        if bar['Cells']['SeatsCount'] == min_seats_count:
            bar_list.append(bar['Cells']['Name'])
    if len(bar_list) >= 2:
        print('Самые маленькие бары Москвы: ')
        for x in bar_list:
            print('   ' + x)
    elif len(bar_list) <= 0:
        print("Баров не найдено!")
    else:
        print('Самый маленький бар в Москве: ' + bar_list[0])


def get_closest_bar(data, longitude, latitude):
    my_X = longitude
    my_Y = latitude
    bar_dict = []
    for bar in data:
        x = float(bar['Cells']['geoData']['coordinates'][0])
        y = float(bar['Cells']['geoData']['coordinates'][1])
        distance = sqrt((my_X - x) ** 2 + (my_Y - y) ** 2)
        distance_for_bar = {
            'Id': bar['Id'],
            'name': bar['Cells']['Name'],
            'distance': distance,
        }
        bar_dict.append(distance_for_bar)
    min_distance = 100
    nearly_bars = []
    for x in bar_dict:
        if x['distance'] < min_distance:
            min_distance = x['distance']
    for x in bar_dict:
        if min_distance == x['distance']:
            nearly_bars.append(x['name'])
    print("Ближайшие бары: ")
    for x in nearly_bars:
        print('   ' + str(x))


if __name__ == '__main__':
    json_data = load_data('Бары.json')
    get_biggest_bar(json_data)
    get_smallest_bar(json_data)
    my_X = 37.193582
    my_Y = 56.005560
    print('Вы хотите ввести координаты с клавиатуры - 1\nИспользовать координаты по умолчанию: %s, %s - 2' % (my_Y, my_X))
    if input(" 1 / 2  \n") == "1":
        my_Y = float(input("Широта: "))
        my_X = float(input("Долгота: "))
    get_closest_bar(json_data, my_X, my_Y)
