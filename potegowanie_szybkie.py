def szybkie(podstawa, wykladnik):
    if wykladnik == 0:
        return 1
    if wykladnik % 2 == 1:
        return podstawa * szybkie(podstawa, wykladnik - 1)
    w = szybkie(podstawa, wykladnik / 2)
    return w * w
