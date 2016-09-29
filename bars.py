
import json
import os

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler: 
        return json.load(file_handler)


def get_biggest_bar(data):

    Biggest_Bar = None

    for bar in data:

        if Biggest_Bar == None:
            Biggest_Bar = bar

        if bar['Cells']['SeatsCount'] > Biggest_Bar['Cells']['SeatsCount']:
            Biggest_Bar = bar

    print ('Самый большой бар <%s>' % (Biggest_Bar['Cells']['Name']))


def get_smallest_bar(data):
    
    Smallest_Bar = None

    for bar in data:

        if Smallest_Bar == None:
            Smallest_Bar = bar

        if bar['Cells']['SeatsCount'] < Smallest_Bar['Cells']['SeatsCount']:
            Smallest_Bar = bar

    print ('Самый маленький бар <%s>' % (Smallest_Bar['Cells']['Name']))


def get_closest_bar(data, longitude, latitude):
    
    if longitude == None or latitude == None:
        
        print ('Неверно указаны координаты!') 

    else:

        Closest_Bar = None

        for bar in data:

            if Closest_Bar == None:
                Closest_Bar = bar

            if (abs(bar['Cells']['geoData']['coordinates'][0] - longitude) < abs(Closest_Bar['Cells']['geoData']['coordinates'][0] - longitude) and 
                    abs(bar['Cells']['geoData']['coordinates'][1] - latitude) < abs(Closest_Bar['Cells']['geoData']['coordinates'][1] - latitude)):
                Closest_Bar = bar

        print ('Самый близкий бар <%s>' % (Closest_Bar['Cells']['Name']))


if __name__ == '__main__':
    
    data_json = load_data('bars.json')
    
    get_biggest_bar(data_json)

    get_smallest_bar(data_json)

    try:

        my_longitude = float(input(u'Введите долготу:'))

    except Exception:

        my_longitude = None

    try:

       my_latitude = float(input('Введите широту:'))

    except Exception:

       my_latitude = None

    get_closest_bar(data_json, my_longitude, my_latitude)