import json


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)
    pass


def get_biggest_bar(data):
    pass


def get_smallest_bar(data):
    pass


def get_closest_bar(data, longitude, latitude):
    pass


def main():
    data = load_data('bars.json')


if __name__ == '__main__':
    main()
    pass
