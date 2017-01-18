import json


def load_data(filepath):
    with open(filepath) as bars_json:
        bars_json = json.load(bars_json)
    return bars_json


def get_biggest_bar(bars_json):
    return max(bars_json, key=lambda x: x['SeatsCount'])

def get_smallest_bar(bars_json):
    return min(bars_json, key=lambda x: x['SeatsCount'])

def get_closest_bar(bars_json, longitude, latitude):
    return min(bars_json, key=lambda x: ((x['geoData']['coordinates'][0] - longitude)**2 +
                                         (x['geoData']['coordinates'][1] - latitude)**2)**0.5)

if __name__ == '__main__':
    bars_json = load_data(input('Путь:\n'))
    longitude = float(input("Longitude:\n"))
    latitude = float(input("Latitude:\n"))
    biggest_bar = get_biggest_bar(bars_json)['Name']
    smallest_bar = get_smallest_bar(bars_json)['Name']
    closest_bar = get_closest_bar(bars_json, longitude, latitude)['Name']
    print('The biggest bar is {0}, the smallest is {1}.'.format(biggest_bar,smallest_bar))
    print("Closest bar is {0}".format(closest_bar))
    
