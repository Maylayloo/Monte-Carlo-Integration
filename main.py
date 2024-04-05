from math import *
from random import uniform


def calculate_min_max_value(infimum, supremum, expression, points):
    max_value = float('-inf')
    min_value = float('inf')
    for i in range(points):
        x = uniform(infimum, supremum)
        tmp_value = eval(expression)
        if tmp_value > max_value:
            max_value = tmp_value
        if tmp_value < min_value:
            min_value = tmp_value
    return round(min_value), round(max_value)


def is_point_under_curve(x, yp, expression):
    expression_y = eval(expression)
    if yp > expression_y:
        return False

    return True


belongs = 0
for i in range(2500):
    x0 = uniform(0, 2)
    for j in range(2500):
        y0 = uniform(0, 1)

    if is_point_under_curve(x0, y0, "sin(x)"):
        belongs += 1

print((belongs / 2500) * 2)
