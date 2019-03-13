def wydawanie(doWydania):
    nominaly = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    wydaneNominaly = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    index = 0
    while doWydania > 0:
        if doWydania >= nominaly[index]:
            iloscBanknotow = doWydania // nominaly[index]
            doWydania -= iloscBanknotow * nominaly[index]
            wydaneNominaly[index] = iloscBanknotow
        else:
            index += 1
    return wydaneNominaly
