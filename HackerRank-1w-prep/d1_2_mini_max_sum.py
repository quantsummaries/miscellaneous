def miniMaxSum(arr):
    total = 0
    min_idx = 0
    max_idx = 0
    for idx, x in enumerate(arr):
        total += x
        if x < arr[min_idx]:
            min_idx = idx
        if x > arr[max_idx]:
            max_idx = idx

    print(total - arr[max_idx], total - arr[min_idx])

miniMaxSum([1, 2, 3, 4, 5])
