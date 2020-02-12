# https://www.practicepython.org/exercise/2015/11/01/25-guessing-game-two.htmloard_size = 4
# users thinks of a number and this program guesses it

print(f'Let\'s play a game.\nYou think of a number between 1 and 100 and I will guess it.\nSay c if my guess is correct, l if my guess is lower and h if my guess is high.')

if __name__=='__main__':
    guess_list = list(range(101))
    guess_count = 0
    guess_is_true = False
    while len(guess_list) > 0 and not guess_is_true:
        mid = int((len(guess_list) - 1) / 2)
        # print(guess_list[mid])
        # print(guess_list)
        if mid < 0:
            mid = 0
        user = input(f'{guess_list[mid]} is: ')
        guess_count += 1
        if user == 'c':
            guess_is_true = True
        elif user == 'l':
            guess_list = guess_list[mid+1:]
        elif user == 'h':
            guess_list = guess_list[:mid]

    if guess_is_true:
        print(f'Great! Only {guess_count} guesses. Let\'s play again')
    else:
        print('Sorry, it\'s out of my range. Can you please guess a number from 1 to 100?')
