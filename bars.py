# -*- coding: utf-8 -*-
import json


def load_data(filepath):
    with open(filepath, encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    return data


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
    bar_la = data[1]['geoData']['coordinates'][1]
    bar_lo = data[1]['geoData']['coordinates'][0]
    shortest_dist = (bar_la - latitude) ** 2 + (bar_lo - longitude) ** 2
    for bar in data:
        bar_la = bar['geoData']['coordinates'][1]
        bar_lo = bar['geoData']['coordinates'][0]
        dist = (bar_la - latitude) ** 2 + (bar_lo - longitude) ** 2
        if dist < shortest_dist:
            nearest_bar = bar['Name']
            nearest_bar_address = bar['Address']
            shortest_dist = dist
    print('Ближайший бар: ', nearest_bar)
    print(nearest_bar_address)


if __name__ == '__main__':
    # getting the path for datafile
    print('Где лежит таблица с файлами? Укажи путь:')
    filepath = str(input())
    # open data in json
    data = load_data(filepath)
    get_biggest_bar(data)
    get_smallest_bar(data)
    # getting longitude
    print('А теперь давай узнаем, какой бар ближе. Введи свои координаты.')
    print('Узнай в гугле, на какой широте ты находишься:')
    latitude = float(input())
    print('Отично, теперь узнай в гугле, на какой долготе ты находишься:')
    longitude = float(input())
    get_closest_bar(data, longitude, latitude)
