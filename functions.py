
def load_json_data(variant):

    import requests
    import zipfile
    import os
    import json
    import sys
    import pprint

    if variant == 1:
        url = 'http://data.mos.ru/opendata/export/1796/json/2/1'
        tmp_file_name = 'tmp/tmp_file'
        tmp_path = 'tmp/'
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            os.mkdir(tmp_path)
            with open(tmp_file_name, 'wb') as code:
                code.write(r.content)
                r.close()
            if zipfile.is_zipfile(tmp_file_name):
                z = zipfile.ZipFile(tmp_file_name, 'r')
                z.extractall(tmp_path)
                z.close()
            for x in os.listdir(tmp_path):
                if '.json' in x:
                    file_name = tmp_path + x
                    f = open(file_name, 'r', encoding='utf_8')
                    data = json.load(f)
                    print('JSON успешно загружен.')
                    print('-----------------------------------------------------------')
                    f.close()
            os.remove(tmp_file_name)
            os.remove(file_name)
            os.rmdir(tmp_path)
        else:
            print('Запрошенная информация не доступна. Программа завершает работу.')
            exit()
    elif variant == 2:
        print("Введите путь до JSON-файла.")
        path = input()
        try:
            f = open(path, 'r', encoding='utf_8')
        except Exception:
            print('Файл не найден')
            print(sys.exc_info()[1])
            exit()
        else:
            try:
                data = json.load(f)
            except Exception:
                pprint(sys.exc_info())
                print('JSON не найден. Программа завершает работу.')
                exit()
            else:
                print('JSON успешно загружен.')
                print('-----------------------------------------------------------')
    else:
        print('The request is invalid. The program shuts down.')
        exit()
    return data


def get_biggest_bar(data):
    max_seats_count = 0
    bar_list = []
    for bar in data:
        if bar['Cells']['SeatsCount'] > max_seats_count:
            max_seats_count = bar['Cells']['SeatsCount']
    for bar in data:
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
    for bar in data:
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
    from math import sqrt
    my_x = longitude
    my_y = latitude
    bar_dict = []
    for bar in data:
        x = float(bar['Cells']['geoData']['coordinates'][0])
        y = float(bar['Cells']['geoData']['coordinates'][1])
        distance = sqrt((my_x - x) ** 2 + (my_y - y) ** 2)
        distance_for_bar = {
            'Id': bar['Id'],
            'name': bar['Cells']['Name'],
            'distance': distance,
        }
        bar_dict.append(distance_for_bar)
    min_distance = 10000
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
