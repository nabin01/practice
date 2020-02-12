# https://www.practicepython.org/exercise/2016/08/03/29-tic-tac-toe-game.html
# complete tic tac toe game

def draw_horizontal():
    print(' ---' * board_size)

def draw_vertical(index):
    print(f'| {grid[index][0]} | {grid[index][1]} | {grid[index][2]} |') 

def draw_grid():
    for index in range(board_size):
        draw_horizontal()
        draw_vertical(index)
    draw_horizontal()

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

def play_game():
    i = 0
    count_full_square = 0 # every game starts with an empty board
    winner = 0
    while count_full_square < 9 and winner == 0:
        draw_grid()

        player = input('Enter the grid position: ')
        # split input and get grid coordinates ( - 1 )
        row = int(player.split(',')[0]) - 1
        col = int(player.split(',')[1]) - 1

        if grid[row][col] != 0:
            print('That place is already taken.\n')
        else:
            if i % 2 == 0:
                grid[int(row)][int(col)] = 'X'
            else:
                grid[int(row)][int(col)] = 'O'
            i += 1
            count_full_square += 1

        winner = check_winner(grid)

    draw_grid()
    if winner != 0:
        print(f'{winner} wins!\n') # say player 1 or player 2
    else:
        print(f'The grid is all filled! It\'s a draw!\n')
    return winner

if __name__=='__main__':
    board_size = 3
    win_count = [0, 0] # player 1, player 2
    print('Tic Tac Toe Game\nLook at the board and enter a position.')
    user = 'y'

    while user == 'y': # everything except 'y' exits the game
        grid = [[0, 0, 0] for i in range(3)]
        print(f'Player 1 = {win_count[0]}\nPlayer 2 = {win_count[1]}')
        winner = play_game()
        if winner == 'X':
            win_count[0] += 1
        elif winner == 'O':
            win_count[1] += 1

        user = input('Do you want to play again?(y,n) ')

    print(f'======== Final Score ========\nPlayer 1 = {win_count[0]}\nPlayer 2 = {win_count[1]}\n')
    print('Thanks for playing!')
