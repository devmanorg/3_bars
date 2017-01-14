import json
import os
import sys

def load_data(filepath):
    with open(filepath) as bars_json:
        bars_json = json.load(bars_json)
    return bars_json


def get_biggest_bar(bars_json):
    max_seats = 0
    for bar in bars_json:
        if bar['SeatsCount'] > max_seats:
            max_seats = bar['SeatsCount']
            biggest_bar = bar
    return "Biggest bar is " +biggest_bar['Name']


def get_smallest_bar(bars_json):
    min_seats = bars_json[0]['SeatsCount']
    for bar in bars_json:
        if bar['SeatsCount'] < min_seats:
            min_seats = bar['SeatsCount']
            smallest_bar = bar       
    return 'Smallest bar is ' + smallest_bar['Name']

def get_closest_bar(bars_json, longitude, latitude):
    coordinates = bars_json[0]['geoData']['coordinates']
    length = ((coordinates[0] - longitude)**2 + (coordinates[1] - latitude)**2)**0.5
    for bar in bars_json:
        coordinates = bar['geoData']['coordinates']
        tmp = ((coordinates[0] - longitude)**2 + (coordinates[1] - latitude)**2)**0.5
        if tmp < length:
            closest_bar = bar
            length = tmp
    return "Closest bar is " + closest_bar['Name']

if __name__ == '__main__':
    bars_json = load_data(input('Путь:\n'))
    longitude = float(input("Longitude:\n"))
    latitude = float(input("Latitude:\n"))
    print(get_biggest_bar(bars_json))
    print(get_smallest_bar(bars_json))
    print(get_closest_bar(bars_json, longitude, latitude))
    
