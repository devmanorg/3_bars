import sys
import json


def load_data(filepath):
    with open(filepath) as file_handler:
        return json.load(file_handler)['features']


def get_biggest_bar(bar_data, *args):
    biggest_bar = max(bar_data,
                      key=lambda x: x['properties']['Attributes']['SeatsCount']
                      )
    return biggest_bar


def get_smallest_bar(bar_data, *args):
    smallest_bar = min(bar_data,
                       key=lambda x: x['properties']['Attributes']['SeatsCount']
                       )
    return smallest_bar


def get_closest_bar(bar_data, longitude, latitude):

    def get_distance(bar_data, longitude, latitude):
        longitude2, latitude2 = bar_data['geometry']['coordinates']
        distance = ((longitude2 - longitude) ** 2 +
                    (latitude2 - latitude) ** 2) ** 0.5
        return distance

    closest_bar = min(bar_data, key=lambda x: get_distance(x, longitude, latitude))
    return closest_bar


def print_answer(bar_list, longitude, latitude):
    feature_list = {
        'большой': get_biggest_bar,
        'маленький': get_smallest_bar,
        'близкий': get_closest_bar
    }
    for adjective, feature in feature_list.items():
        bar_feature = feature(bar_list, longitude, latitude)
        print(
            "Самый {0} бар – {1},"
            .format(adjective, bar_feature['properties']['Attributes']['Name']),
            "Мест: {},".format(bar_feature['properties']['Attributes']['SeatsCount']),
            "Адрес: {}".format(bar_feature['properties']['Attributes']['Address'])
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
    except ValueError:
        print('Это не файл JSON')
    else:
        print_answer(bar_list, longitude, latitude)
