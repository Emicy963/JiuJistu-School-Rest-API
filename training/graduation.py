import math

order_belt = {'Branca': 0, 'Azul': 1, 'Roxa': 2, 'Marrom': 3, 'Preta': 4 }


def calculate_lesson_to_upgrade(n):
    d = 1.47
    k = 30 / math.log(d)
    class_ = k*math.log(n + d)
    return round(class_)
