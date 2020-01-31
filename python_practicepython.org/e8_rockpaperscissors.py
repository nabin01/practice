# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using
# input), compare them, print out a message of congratulations to the winner, and
# ask if the players want to start a new game)

def compare(player1, player2):
    if player1 == player2:
        return 'Draw!'
    elif player1 == 'r' and player2 == 's':
        return 'Player 1 wins!'
    elif player1 == 'p' and player2 == 'r':
        return 'Player 1 wins1'
    elif player1 == 's' and player2 == 'p':
        return 'Player 1 wins!'
    else:
        return 'Player 2 wins!'


def compare_with_dict(player1, player2):
    game_dict = {'r': 1, 'p': 2, 's': 3}
    diff = game_dict.get(player1) - game_dict.get(player2)
    if diff == 0:
        return 'Draw!'
    elif diff in [-2, 1]:
        return 'Player 1 wins!'
    else: # diff in [-2, 1]
        return 'Player 2 wins!'


start = input('Do you want to start a new game? (y/n) ')
while start == 'y':
    player1 = 'a'
    player2 = 'a'
    while player1 not in 'rps':
        player1 = input(f'Player 1: Rock | Paper | Scissors (r|p|s): ')
    while player2 not in 'rps':
        player2 = input(f'Player 2: Rock | Paper | Scissors (r|p|s): ')

    print(f'{compare_with_dict(player1, player2)}')

    start = input('Do you want to start a new game? (y/n) ')
