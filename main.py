from math import *
from random import uniform


def calculate_max_value(infimum, supremum, expression, points):
    max_value = float('-inf')
    for i in range(points):
        x = uniform(infimum, supremum)
        tmp_max = eval(expression)
        if tmp_max > max_value:
            max_value = tmp_max

    return round(max_value)


# interval = input("Please provide integration interval, e.g. 0 3 \n")
print(calculate_max_value(0,2,"sin(x)", 1000))
# x = 3
# expression = eval(test)

# print(expression)

# expression = input()
test_expression = "sin(x)"
x = uniform(0, 2)
# y = uniform(
# print(x)