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

# interval = input("Please provide integration interval, e.g. 0 3 \n")
print(calculate_min_max_value(-1,2,"2*x**5", 1000))
# x = 3
# expression = eval(test)

# print(expression)
# for i in range(3):
#     x0 = uniform(0, 2)
#     for j in range(3):
#         y0 = uniform(0, 1)
#
#     print(x0, y0, is_point_under_curve(x0, y0, "sin(x)"))

# expression = input()
test_expression = "sin(x)"
x = uniform(0, 2)
# y = uniform(
# print(x)