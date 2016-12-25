from functions import *

if __name__ == '__main__':
    print("Загрузить массив баров с портала открытых данных правительства Москвы: - 1")
    print("Самостоятельно выбрать файл на жестком диске: - 2")
    answer = int(input())
    json_data = load_json_data(answer)
    get_biggest_bar(json_data)
    get_smallest_bar(json_data)
    my_x = 37.193582
    my_y = 56.005560
    print('Вы хотите ввести координаты с клавиатуры - 1\nИспользовать координаты по умолчанию: %s, %s - 2' % (my_y, my_x))
    if input(" 1 / 2  \n") == "1":
        my_y = float(input("Широта: "))
        my_x = float(input("Долгота: "))
    get_closest_bar(json_data, my_x, my_y)

