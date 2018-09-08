import sys
import json
import inspect


def load_data(filepath):
    with open(filepath) as file_handler:
        return json.load(file_handler)['features']


def get_biggest_bar(bar_data):
    biggest_bar = max(bar_data, key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return biggest_bar


def get_smallest_bar(bar_data):
    smallest_bar = min(bar_data, key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return smallest_bar


def get_distance(bar_data, longitude, latitude):
        longitude2, latitude2 = bar_data['geometry']['coordinates']
        distance = ((longitude2 - longitude) ** 2 +
                    (latitude2 - latitude) ** 2) ** 0.5
        return distance


def get_closest_bar(bar_data, longitude, latitude):
    closest_bar = min(bar_data, key=lambda x: get_distance(x, longitude, latitude))
    return closest_bar


def print_bar(category, bar_found):
    print(
        inspect.stack()[1].code_context,
        category,
        bar_found['properties']['Attributes']['Name'],
        'Мест: {},'.format(bar_found['properties']['Attributes']['SeatsCount']),
        'Адрес: {}'.format(bar_found['properties']['Attributes']['Address']),
    )


if __name__ == '__main__':
    try:
        bar_list = load_data(sys.argv[1])
        longitude = float(sys.argv[2])
        latitude = float(sys.argv[3])
    except IndexError:
        print('Пожалуйста укажите все параметры')
    except FileNotFoundError:
        print('Файл не найден')
    # except ValueError:
    #     print('Это не файл JSON')
    else:
        print_bar('Самый большой бар:', get_biggest_bar(bar_list))
        # print_bar('Самый маленький бар:', get_smallest_bar(bar_list))
        # print_bar('Самый близкий бар:', get_closest_bar(bar_list, longitude, latitude))
