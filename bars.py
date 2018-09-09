import sys
import json
import inspect
import argparse


def load_data(filepath):
    with open(filepath) as file_handler:
        return json.load(file_handler)['features']


def get_biggest_bar(bar_data):
    return max(bar_data, key=lambda x: x['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(bar_data):
    return min(bar_data, key=lambda x: x['properties']['Attributes']['SeatsCount'])


def get_distance(bar_data, longitude, latitude):
    longitude2, latitude2 = bar_data['geometry']['coordinates']
    return ((longitude2 - longitude) ** 2 + (latitude2 - latitude) ** 2) ** 0.5


def get_closest_bar(bar_data, longitude, latitude):
    return min(bar_data, key=lambda x: get_distance(x, longitude, latitude))


def print_bar(bar_found):
    # Get the calling function name to pick up an adjective
    # from the features dictionary
    caller = inspect.stack()[1].code_context[0]
    features = {
        'biggest': 'большой',
        'smallest': 'маленький',
        'closest': 'близкий',
    }
    adj = [desc for feat, desc in features.items() if feat in caller][0]
    print(
        'Самый {0} бар: {1},'.format(adj, bar_found['properties']['Attributes']['Name']),
        'мест: {0}'.format(bar_found['properties']['Attributes']['SeatsCount']),
        '\nАдрес: {0}'.format(bar_found['properties']['Attributes']['Address']),
    )
    return None


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('longitude', type=float, default=0)
    parser.add_argument('latitude', type=float, default=0)
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    try:
        bar_list = load_data(args.file)
    except json.decoder.JSONDecodeError:
        print('Please specify valid JSON file')
    else:
        print_bar(get_biggest_bar(bar_list))
        print_bar(get_smallest_bar(bar_list))
    if args.longitude and args.latitude:
        print_bar(get_closest_bar(bar_list, args.longitude, args.latitude))

    # 37.511560 55.745634
