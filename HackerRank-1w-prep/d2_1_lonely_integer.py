def lonelyIntegr(a):
    ints = dict()
    for x in a:
        if x in ints:
            ints[x] += 1
        else:
            ints[x] = 1

    for k, v in ints.items():
        if v == 1:
            return k

print(lonelyIntegr([1, 2, 3, 4, 3, 2, 1]))