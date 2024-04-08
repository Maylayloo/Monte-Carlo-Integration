from math import *
from random import uniform


def find_extremes(infimum, supremum, expression, points):
    max_value = float('-inf')
    min_value = float('inf')
    for i in range(points):
        x = uniform(infimum, supremum)
        tmp_value = eval(expression)
        if tmp_value > max_value:
            max_value = tmp_value
        if tmp_value < min_value:
            min_value = tmp_value
    return min_value, max_value


def is_point_under_curve(x, yp, expression):
    expression_y = eval(expression)
    if yp > 0 and expression_y > 0:
        if yp < expression_y:
            return True
    elif yp < 0 and expression_y < 0:
        if yp > expression_y:
            return True

    return False


belongs = 0

expression = input("Please provide an expression: ")
interval = input("Provide an interval, e.g. 0 2: ").split()
points = int(input("Specify the number of points to be randomized: "))

infimum = int(interval[0])
supremum = int(interval[1])

extremes = find_extremes(infimum, supremum, expression, points)
min_value = extremes[0]
max_value = extremes[1]

for i in range(points):
    x0 = uniform(infimum, supremum)
    y0 = uniform(min_value, max_value)

    if is_point_under_curve(x0, y0, expression):
        belongs += 1

ratio = belongs / points
rectangle_area = abs((supremum - infimum) * (max_value - min_value))

result = ratio * rectangle_area

print("Result: ", result)
