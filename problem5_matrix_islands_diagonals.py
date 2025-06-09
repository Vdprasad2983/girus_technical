def count_islands(matrix):
    def dfs(r, c):
        if r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix[0]) or matrix[r][c] != 1:
            return
        matrix[r][c] = -1
        for dr in [-1,0,1]:
            for dc in [-1,0,1]:
                if dr != 0 or dc != 0:
                    dfs(r+dr, c+dc)

    count = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 1:
                dfs(r, c)
                count += 1
    return count

# Test Case
matrix = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1]
]
print("Number of Islands:", count_islands(matrix))
