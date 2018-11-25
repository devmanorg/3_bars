import json
import sys


def load_data(filepath):
    with open(filepath, "r") as file_json:
        json_loaded = json.load(file_json)
    return json_loaded


def get_coordinates(bar):
    return bar['geometry']['coordinates']


def get_seats_count(bar):
    return bar["properties"]["Attributes"]["SeatsCount"]


def get_name(bar):
    return bar['properties']['Attributes']['Name']


def get_address(bar):
    return bar["properties"]["Attributes"]["Address"]


def get_biggest_bar(bar):
    return max(bar, key=get_seats_count)


def get_smallest_bar(bar):
    return min(bar, key=get_seats_count)


def get_closest_bar(bars, longitude, latitude):
    return min(bars, key=lambda
        bar: get_distance_of_two_points(get_coordinates(bar), [longitude, latitude]))


def get_distance_of_two_points(bar_coordinate, your_coordinate):
    return (bar_coordinate[0] - your_coordinate[0]) ** 2 + (bar_coordinate[1] - your_coordinate[1]) ** 2


if __name__ == '__main__':
    try:
        bars = load_data(sys.argv[1])['features']
        longitude = float(input("Введите долготу: "))
        latitude = float(input("Введите широту: "))
    except (FileNotFoundError, IndexError):
        print("Некоректно указан путь к файлу или файл не существует")
    except json.decoder.JSONDecodeError:
        print("Не корректное содержимое JSON файла")
    except ValueError:
        print("Координаты введены некорректно")
    selected_bars = {
        'Самый большой бар:': get_biggest_bar(bars),
        'Самый маленький бар:': get_smallest_bar(bars),
        'Самый ближайший бар:': get_closest_bar(bars, longitude, latitude)
    }
    for title, bar in selected_bars.items():
        print("{} {}. Находиться по адресу: {} и может вмещать посетителей: {}".format(
            title, get_name(bar), get_address(bar), get_seats_count(bar)))
