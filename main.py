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


# interval = input("Please provide integration interval, e.g. 0 3 \n")
print(calculate_min_max_value(-1,2,"2*x**5", 1000))
# x = 3
# expression = eval(test)

# print(expression)

# expression = input()
test_expression = "sin(x)"
x = uniform(0, 2)
# y = uniform(
# print(x)