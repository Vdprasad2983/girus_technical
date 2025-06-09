def is_valid_sudoku(board, zones):
    def is_unique(group):
        nums = [x for x in group if x != '.']
        return len(nums) == len(set(nums))

    for i in range(9):
        if not is_unique(board[i]) or not is_unique([board[j][i] for j in range(9)]):
            return False

    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            square = [board[r+i][c+j] for i in range(3) for j in range(3)]
            if not is_unique(square):
                return False

    for zone in zones:
        if not is_unique([board[r][c] for r, c in zone]):
            return False

    return True

# Test Case
board = [
    ['5','3','.','.','7','.','.','.','.'],
    ['6','.','.','1','9','5','.','.','.'],
    ['.','9','8','.','.','.','.','6','.'],
    ['8','.','.','.','6','.','.','.','3'],
    ['4','.','.','8','.','3','.','.','1'],
    ['7','.','.','.','2','.','.','.','6'],
    ['.','6','.','.','.','.','2','8','.'],
    ['.','.','.','4','1','9','.','.','5'],
    ['.','.','.','.','8','.','.','7','9']
]
zones = [[(i,j) for j in range(9)] for i in range(9)]
print("Sudoku Valid:", is_valid_sudoku(board, zones))
