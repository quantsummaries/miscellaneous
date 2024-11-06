def pairs(k, arr):
    # Write your code here
    arr.sort()
    s = set(arr)
    cnt = 0
    for i in arr:
        if (k+i) in s:
            cnt += 1
    return cnt

print(pairs(2, [1, 5, 3, 4, 2]))