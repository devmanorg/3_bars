import json


def load_data(filepath):
    my_file = open(filepath, mode="r", encoding='utf-8')
    json_data = json.load(my_file)
    my_file.close()
    return json_data


def get_biggest_bar(data):
    bar_list = ()
    max_seats_count = 0
    for bar in data:
        if bar['Cells']['SeatsCount'] > max_seats_count:
            max_seats_count = bar['Cells']['SeatsCount']
    for bar in json_data:
        if bar['Cells']['SeatsCount'] == max_seats_count:
            bar_list.append(bar['Cells']['Name'])
    if bar_list.count() > 1:
        print("---------------------------------------")
        print()


        for x in bar_list:
            print(x)
    elif bar_list.count() <= 0:
        print("Больших баров не найдено!")


def get_smallest_bar(data):
    pass


def get_closest_bar(data, longitude, latitude):
    pass


if __name__ == '__main__':
    json_data = load_data('Бары.json')
