def min_max(tablica):
    min = tablica[0]
    max = tablica[0]

    for liczba in tablica:
        if liczba > max:
            max = liczba
        if liczba < min:
            min = liczba
    return min, max

# da sie zrobic bardziej optymalny
