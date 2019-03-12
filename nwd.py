def nwd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def nwd_optimal(a, b):
    while b != 0:
        pom = b
        b = a % b
        a = pom

    return a


def nww(a, b):
    return a * b / nwd(a, b)
