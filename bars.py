import json


def load_data(filepath):
    with open(filepath, 'r') as file_json:
        json_loaded = json.load(file_json)
    return json_loaded


def get_biggest_bar(data):
    return max(data["features"], key=lambda feature:
    feature["properties"]["Attributes"]["SeatsCount"])


def get_smallest_bar(data):
    return min(data["features"], key=lambda feature:
    feature["properties"]["Attributes"]["SeatsCount"])


def get_closest_bar(data, longitude, latitude):
    return min(data["features"], key=lambda feature:
    get_distance_of_two_points(feature["geometry"]["coordinates"], [longitude, latitude]))


def get_distance_of_two_points(bar_coordinate, your_coordinate):
    return (bar_coordinate[0] - your_coordinate[0]) ** 2 + (bar_coordinate[1] - your_coordinate[1]) ** 2


if __name__ == '__main__':
    data = load_data(input('Укажите путь к файлу: '))
    longitude = float(input("Введите долготу: "))
    latitude = float(input("Введите широту: "))
    biggest_bar = get_biggest_bar(data)
    smallest_bar = get_smallest_bar(data)
    closest_bar = get_closest_bar(data, longitude, latitude)
    print("Самый большой бар: " + biggest_bar["properties"]["Attributes"]["Name"])
    print("Самый маленький бар: " + smallest_bar["properties"]["Attributes"]["Name"])
    print("Самый ближайший бар: " + closest_bar["properties"]["Attributes"]["Name"] + '. Находиться по адресу: ' +
          closest_bar["properties"]["Attributes"]["Address"])
