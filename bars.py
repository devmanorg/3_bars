import json
import sys


def load_data(filepath):
    with open(filepath, "r") as file_json:
        json_loaded = json.load(file_json)
    return json_loaded


def get_coordinates(bar):
    return bar['geometry']['coordinates']


def get_seat_count(bar):
    return bar["properties"]["Attributes"]["SeatsCount"]


def get_name(bar):
    return bar['properties']['Attributes']['Name']


def get_address(bar):
    return bar["properties"]["Attributes"]["Address"]


def get_biggest_bar(bar):
    return max(bar, key=lambda bar: get_seat_count(bar))


def get_smallest_bar(bar):
    return min(bar, key=lambda bar: get_seat_count(bar))


def get_closest_bar(bars, longitude, latitude):
    return min(bars, key=lambda
        bar: get_distance_of_two_points(get_coordinates(bar), [longitude, latitude]))


def get_distance_of_two_points(bar_coordinate, your_coordinate):
    return (bar_coordinate[0] - your_coordinate[0]) ** 2 + \
           (bar_coordinate[1] - your_coordinate[1]) ** 2


if __name__ == '__main__':
    try:
        bars = load_data(sys.argv[1])['features']
        longitude = float(input("Введите долготу: "))
        latitude = float(input("Введите широту: "))
        biggest_bar = get_biggest_bar(bars)
        smallest_bar = get_smallest_bar(bars)
        closest_bar = get_closest_bar(bars, longitude, latitude)
        print("Самый большой бар: " + get_name(biggest_bar))
        print("Самый маленький бар: " + get_name(smallest_bar))
        print("Самый ближайший бар: {} . Находиться по адресу: {}"
              .format(get_name(closest_bar), get_address(closest_bar)))
    except (FileNotFoundError, IndexError):
        print('Некоректно указан путь к файлу или файл не существует')
    except json.decoder.JSONDecodeError:
        print('Не корректное содержимое JSON файла')