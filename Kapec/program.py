from algo import Point, intersect


def correct_coord(coord):
    coord = coord.split(',')
    return Point(int(coord[0]), int(coord[1])) 


def main():
    print("Проверка двух отрезков A и B на пересечение")
    print("Координаты вводить через запятую")

    line_1_point_start = input('Введите координаты начала отрезка A: ')
    line_1_point_end = input('Введите координаты конца отрезка A: ')

    line_2_point_start = input('Введите координаты начала отрезка B: ')
    line_2_point_end = input('Введите координаты начала отрезка B: ')

    line_1_point_start = correct_coord(line_1_point_start)
    line_1_point_end = correct_coord(line_1_point_end)
    line_2_point_start = correct_coord(line_2_point_start)
    line_2_point_end = correct_coord(line_2_point_end)
    
    result = intersect(line_1_point_start, line_1_point_end, line_2_point_start, line_2_point_end)
    print(result)