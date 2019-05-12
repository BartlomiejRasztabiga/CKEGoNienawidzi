def f(x):
    return x * x


def prostokatow(a, b, n):
    pole = 0
    szerokosc = (b - a) / n
    srodek = a + (szerokosc / 2)

    i = 0
    while i < n:
        pole += f(srodek) * szerokosc
        srodek += szerokosc
        i += 1
    return pole


def trapezow(a, b, n):
    pole = 0
    szerokosc = (b - a) / n

    poczatek = a
    koniec = poczatek + szerokosc

    i = 0
    while i < n:
        pole += (f(poczatek) + f(koniec)) * szerokosc / 2
        poczatek += szerokosc
        koniec += szerokosc
        i += 1
    return pole
