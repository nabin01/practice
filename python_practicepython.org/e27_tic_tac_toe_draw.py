# https://www.practicepython.org/exercise/2015/11/26/27-tic-tac-toe-draw.html
# tic tac toe game
# ask user for grid position and 
# check if the position is already taken and also check if the squares are filled

def draw_board():
    for i in range(3):
        for j in range(3):
            print(grid[i][j], end=' ')
        print()

def play_game():
    i = 0
    count_full_square = 0 # every game starts with an empty board
    while count_full_square < 9:
        draw_board()

        player = input('Enter the grid position:(1,1) ')
        row = int(player.split(',')[0]) - 1
        col = int(player.split(',')[1]) - 1

        if grid[row][col] != 0:
            print('That place is already taken.')
        else:
            if i % 2 == 0:
                grid[int(row)][int(col)] = 'X'
            else:
                grid[int(row)][int(col)] = 'O'
            i += 1
            count_full_square += 1

    print(f'The grid is all filled!')
    draw_board()

if __name__=='__main__':
    grid = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]
    print('Tic Tac Toe Game:\nLook at the board and enter a position')
    play_game()
    
