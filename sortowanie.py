def babelek_sort(tablica):
    n = len(tablica)
    a = n - 1
    poczatek = 0
    while poczatek < n:
        while a > poczatek:
            if tablica[a] < tablica[a - 1]:
                temp = tablica[a - 1]
                tablica[a - 1] = tablica[a]
                tablica[a] = temp
            a -= 1

        poczatek += 1
        a = n - 1
    return tablica
