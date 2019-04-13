def f(x):
    return 2 * x ** 2 - 4 * x - 2


def zerowe(a, b, dokladnosc):
    if f(a) == 0: return a
    if f(b) == 0: return b
    while abs(b - a) > dokladnosc:
        srodek = (a + b) / 2
        if f(srodek) == 0: return srodek
        if f(a) * f(srodek) < 0:
            b = srodek
        else:
            a = srodek
    return (a + b) / 2
