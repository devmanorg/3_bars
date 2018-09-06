import sys
import json


def load_data(filepath):
    with open(filepath) as file_handler:
        return json.load(file_handler)['features']


def get_biggest_bar(data, *args):
    biggest_bar = max(data,
                      key=lambda x: x['properties']['Attributes']['SeatsCount']
                      )
    return biggest_bar


def get_smallest_bar(data, *args):
    smallest_bar = min(data,
                       key=lambda x: x['properties']['Attributes']['SeatsCount']
                       )
    return smallest_bar


def get_closest_bar(data, longitude, latitude):

    def get_distance(data, longitude, latitude):
        longitude2, latitude2 = data['geometry']['coordinates']
        distance = ((longitude2 - longitude) ** 2 +
                    (latitude2 - latitude) ** 2) ** 0.5
        return distance

    closest_bar = min(data, key=lambda x: get_distance(x, longitude, latitude))
    return closest_bar


if __name__ == '__main__':
    try:
        bar_list = load_data(sys.argv[1])
        longitude = float(sys.argv[2])
        latitude = float(sys.argv[3])
    except IndexError:
        print('Please specify all parameters')
    except FileNotFoundError:
        print('File not found')
    except ValueError:
        print('Not a valid JSON file')
    else:
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
