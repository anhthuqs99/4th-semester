def LeftSide(y, h):
    result = []
    for i in range(len(y)):
        if not i:
            result.append("-")
        else:
            result.append(((y[i] - y[i - 1]) / h))
    return result


def CenterDiff(y, h):
    result = []
    for i in range(len(y)):
        if (not i) or (i == len(y) - 1):
            result.append("-")
        else:
            result.append((y[i + 1] - y[i - 1]) / (2 * h))
    return result


def RungeLeft(y, h):
    result = []
    for i in range(0, len(y)):
        if i < 2:
            result.append("-")
        else:
            result.append(2 * ((y[i] - y[i - 1]) / h) - ((y[i] - y[i - 2]) / (2 * h)))

    return result


def Alignment(x, y, h):
    result = []
    for i in range(0, len(y)):
        if i > len(y) - 2:
            result.append("-")
        else:
            result.append((1 / y[i + 1] - 1 / y[i]) / (1 / x[i + 1] - 1 / x[i]) * (y[i] ** 2) / (x[i] ** 2))

    return result


def SecondDiff(y, h):
    result = []
    for i in range(0, len(y)):
        if (not i) or (i > len(y) - 2):
            result.append("-")
        else:
            result.append((y[i - 1] - 2 * y[i] + y[i + 1]) / (h ** 2))

    return result


def PrintResult(table):
    print("{:^9}{:^9}{:^9}{:^9}{:^9}{:^9}{:^9}".format("x", "y", "(1)", "(2)", "(3)", "(4)", "(5)"))
    N = len(table[1])
    for i in range(N):
        for result in table:
            if result[i] == "-":
                print("{:^9}".format(result[i]), end="")
            else:
                print("{:^9.3f}".format(result[i]), end="")
        print()


def main():
    h = 1
    x = [i for i in range(1, 7)]
    y = [0.571, 0.889, 1.091, 1.231, 1.333, 1.412]

    left_side = LeftSide(y, h)
    center_diff = CenterDiff(y, h)
    runge_left = RungeLeft(y, h)
    alignment = Alignment(x, y, h)
    second_diff = SecondDiff(y, h)

    table = [x, y, left_side, center_diff, runge_left, alignment, second_diff]
    PrintResult(table)

main()
