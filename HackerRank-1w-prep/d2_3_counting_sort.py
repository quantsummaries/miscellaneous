def countingSort(arr):
    freq = [0] * 100
    for x in arr:
        freq[x] += 1

    return freq

print(countingSort([1, 1, 3, 2, 1]))