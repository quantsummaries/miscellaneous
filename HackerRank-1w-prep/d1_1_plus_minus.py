# reference: https://www.geeksforgeeks.org/precision-handling-python/

def plusMinus(arr):
    n = len(arr)
    pos = 0
    neg = 0
    zero = 0
    for x in arr:
        if x > 0:
            pos += 1
        elif x < 0:
            neg += 1
        else:
            zero += 1

    for cnt in [pos, neg, zero]:
        print("%.6f" % (cnt/n))

plusMinus([-4, 3, -9, 0, 4, 1])