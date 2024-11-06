def diagonalDifference(arr):
    n = len(arr)
    s1 = 0
    s2 = 0
    for i in range(n):
        s1 += arr[i][i]
        s2 += arr[i][n-1-i]

    return abs(s1-s2)

print(diagonalDifference([[1, 2, 3], [4, 5, 6], [9, 8, 9]]))
print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))