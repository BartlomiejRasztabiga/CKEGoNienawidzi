def anagram(a, b):
    sortA = "".join(sorted(a))
    sortB = "".join(sorted(b))
    return sortA == sortB
