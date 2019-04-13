import string


def cezar(slowo, n):
    alfabet = string.ascii_lowercase * 2
    szyfr = ""
    n = n % 26
    for letter in slowo:
        x = alfabet.find(letter)
        y = x + n
        szyfr += alfabet[y]
    return szyfr
