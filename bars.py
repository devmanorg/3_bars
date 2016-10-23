import json


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
    pass


if __name__ == '__main__':
    json_data = load_data('Бары.json')
    get_biggest_bar(json_data)
    get_smallest_bar(json_data)
