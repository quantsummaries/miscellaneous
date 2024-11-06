def superDigit(n, k):
    # do the addition first to avoid overflow in values
    p = str(sum([int(x) for x in n]) * k)

    def findSuperDigit(p):
        if len(p) == 1:
            return int(p)
        else:
            next_p = str(sum([int(x) for x in p]))
            return findSuperDigit(next_p)

    return findSuperDigit(p)

print(superDigit(n='9875', k=4))