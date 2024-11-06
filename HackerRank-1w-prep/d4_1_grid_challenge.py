def gridChallenge(grid):
    for idx, val in enumerate(grid):
        grid[idx] = ''.join(sorted(val))

    n = len(grid)
    m = len(grid[0])
    for col_idx in range(m):
        for row_idx in range(n):
            if row_idx == 0:
                continue
            else:
                if grid[row_idx][col_idx] < grid[row_idx-1][col_idx]:
                    return 'NO'
    return 'YES'

print(gridChallenge(['abc', 'ade', 'efg']))
print(gridChallenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']))