def pierwiastek(n, precyzja):
    a = 1.0
    b = n
    while abs(a - b) >= precyzja:
        a = (a + b) / 2.0
        b = n/a
    return a
