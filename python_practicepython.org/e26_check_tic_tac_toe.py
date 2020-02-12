# https://www.practicepython.org/exercise/2015/11/16/26-check-tic-tac-toe.html
# tic tac toe game using lists

def check_winner(grid):
    # row
    for row in range(3):
        i = set([grid[row][0], grid[row][1], grid[row][2]])
        if len(i) == 1 and grid[row][0] != 0:
            return grid[row][0]

    # col
    for col in range(3):
        i = set([grid[0][col], grid[1][col], grid[2][col]])
        if len(i) == 1 and grid[0][col] != 0:
            return grid[0][col]

    # diagonal
    diagonal1 = set([grid[0][0], grid[1][1], grid[2][2]])
    diagonal2 = set([grid[0][2], grid[1][1], grid[2][0]])
    if len(diagonal1) == 1 or len(diagonal2) == 1 and grid[1][1] != 0:
        return grid[1][1]

    return 0

winner_is_2 = [[2, 2, 0],
            [2, 1, 0],
                [2, 1, 1]]

winner_is_1 = [[1, 2, 0],
            [2, 1, 0],
                [2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
            [2, 1, 0],
                [2, 1, 1]]

no_winner = [[1, 2, 0],
            [2, 1, 0],
                [2, 1, 2]]

also_no_winner = [[1, 2, 0],
            [2, 1, 0],
                [2, 1, 0]]

print(check_winner(also_no_winner)) # substitute here
