import json


def load_data(filepath):
    with open('data.json') as data_file:
        data = json.load(data_file)
    return data


def get_biggest_bar(data):
    max_seats = 0
    for bar in data:
        if bar['SeatsCount'] > max_seats:
            max_seats = bar['SeatsCount']
            biggest_bar = bar
    return "Biggest bar is:", biggest_bar


def get_smallest_bar(data):
    min_seats = data[0]['SeatsCount']
    for bar in data:
        if bar['SeatsCount'] < min_seats:
            min_seats = bar['SeatsCount']
            smallest_bar = bar       
    return 'Smallest bar is:', smallest_bar

def get_closest_bar(data, longitude, latitude):
    coordinates = data[0]['geoData']['coordinates']
    length = ((coordinates[0] - longitude)**2 + (coordinates[1] - latitude)**2)**0.5
    for bar in data:
        coordinates = bar['geoData']['coordinates']
        tmp = ((coordinates[0] - longitude)**2 + (coordinates[1] - latitude)**2)**0.5
        if tmp < length:
            closest_bar = bar
            length = tmp
    return "Closest bar is:", closest_bar

if __name__ == '__main__':
    data = load_data(input("Путь:"))
    longitude = float(input("Longitude:"))
    latitude = float(input("Latitude:"))
    print(get_biggest_bar(data))
    print(get_smallest_bar(data))
    print(get_closest_bar(data, longitude, latitude))
    
