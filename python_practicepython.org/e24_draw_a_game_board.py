# This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other 
# exercises are: Part 2, Part 3, and Part 4.
# 
# Time for some fake graphics! Lets say we want to draw game boards that look 
# like this:
# 
#      --- --- --- 
#     |   |   |   | 
#      --- --- ---  
#     |   |   |   | 
#      --- --- ---  
#     |   |   |   | 
#      --- --- --- 
#
# This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes 
# (8x8 for chess, 19x19 for Go, and many more).
# 
# Ask the user what size game board they want to draw, and draw it for them to the 
# screen using Pythons print statement.

def draw_game_board(row, col):
    char_list = ['-','|']
    i = 0
    j = 0
    row_limit = row * 2 + 1
    col_limit = col * 4 + 1
    while i < row_limit:
        j = 0
        while j < col_limit:
            if i % 2 == 0:
                if j % 4 == 0:
                    print(' ', end='')
                else:
                    print('-', end='')
            else:
                if j % 4 == 0:
                    print('|', end='')
                else:
                    print(' ', end='')
            j += 1
        i += 1
        print()

row, col = input("Enter the size of the board:(rowxcol) ").split('x')
draw_game_board(int(row), int(col))
