# The 24 Game
#
# Combine 4 numbers to make the number 24. You may add, subtract, multiply, or divide. You amy also use parentheses.
# You can't use any other symbols. You have to use each of the four numbers exactly once. - AoPS, Prealgebra.

import math


def isInteger(x: float) -> bool:
    frac, whole = math.modf(x)
    ret_val = not (frac > 0)
    return ret_val


def calc(x: list, y: int) -> bool:
    if len(x) == 2:
        if x[0] + x[1] == y:
            print(x[0], " + ", x[1], " = ", y)
            return True
        if x[0] - x[1] == y:
            print(x[0], " - ", x[1], " = ", y)
            return True
        if x[1] - x[0] == y:
            print(x[1], " - ", x[0], " = ", y)
            return True
        if x[0] * x[1] == y:
            print(x[0], " * ", x[1], " = ", y)
            return True
        if x[0] / x[1] == y:
            print(x[0], " / ", x[1], " = ", y)
            return True
        if x[1] / x[0] == y:
            print(x[1], " / ", x[0], " = ", y)
            return True
        return False

    for i in range(len(x)):
        new_x = [x[k] for k in range(len(x)) if k != i]

        # x[i] + y1 = y
        y1 = y - x[i]
        if y1 > 0 and calc(new_x, y1):
            print(x[i], " + ", y1, " = ", y)
            if len(x) != 4:
                return True
            else:
                print("one success for ", x)

        # y1 - x[i] = y
        y1 = y + x[i]
        if calc(new_x, y1):
            print(y1, " - ", x[i], " = ", y)
            if len(x) != 4:
                return True
            else:
                print("one success for ", x)

        # x[i] - y1 = y
        y1 = x[i] - y
        if y1 > 0 and calc(new_x, y1):
            print(x[i], " - ", y1, " = ", y)
            if len(x) != 4:
                return True
            else:
                print("one success for ", x)

        # y1 * x[i] = y
        y1 = y / x[i]
        if isInteger(y1) and calc(new_x, y1):
            print(y1, " * ", x[i], " = ", y)
            if len(x) != 4:
                return True
            else:
                print("one success for ", x)

        # x[i] / y1 = y
        y1 = x[i] / y
        if isInteger(y1) and calc(new_x, y1):
            print(x[i], " / ", y1, " = ", y)
            if len(x) != 4:
                return True
            else:
                print("one success for ", x)

        # y1 / x[i] = y
        y1 = y * x[i]
        if calc(new_x, y1):
            print(y1, " / ", x[i], " = ", y)
            if len(x) != 4:
                return True
            else:
                print("one success for ", x)



#calc([3, 8, 8, 1], 24)
calc([4, 1, 7, 6], 24)
calc([4, 1, 8, 5], 24)
calc([1, 1, 23, 22], 24)
calc([5, 1, 10, 7], 24)