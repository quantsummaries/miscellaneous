# reference: https://rcoh.me/posts/linear-time-median-finding/

import random

def findMedian(arr):
    k = (len(arr) - 1)//2

    def quickSelect(l, k):
        if len(l) == 1:
            if k != 0:
                print(k)
            assert k == 0
            return l[0]

        pivot = random.choice(l)
        lower = [x for x in l if x < pivot]
        higher = [x for x in l if x > pivot]
        equals = [x for x in l if x == pivot]

        if k < len(lower):
            return quickSelect(lower, k)
        elif k < len(lower) + len(equals):
            return pivot
        else:
            return quickSelect(higher, k - (len(lower)+len(equals)-1) - 1)

    return quickSelect(arr, k)

print(findMedian([1, 3, 0, 4, 2]))
print(findMedian([0, 1, 2, 4, 6, 5, 3]))
print(findMedian([5, 3, 1, 2, 4]))
