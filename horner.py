def horner(wspolczynniki, stopien, x):
    wynik = wspolczynniki[0]

    i = 1
    while i <= stopien:
        wynik = wynik * x + wspolczynniki[i]
        i += 1
    return wynik
