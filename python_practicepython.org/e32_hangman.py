# https://www.practicepython.org/exercise/2017/01/10/32-hangman.html
# finish Hangman

import random

def display_secret_word(secret_word):
    for char in secret_word:
        print(char, end=' ')
    print()

def find_letter(word, char):
    return [i for i, ch in enumerate(word) if ch == char]

def display_man(incorrect_guesses):
    body_parts = ['       O','\n     --|','--','\n       |','\n      / ','\\']
    dead_body_parts = ['       X','\n     XX|','XX','\n       X','\n      X ','X']
    print('_______')
    print('       |')
    i = 0
    while i < incorrect_guesses:
        print(dead_body_parts[i], end='')
        i += 1
    while i < len(body_parts):
        print(body_parts[i], end='')
        i += 1
    print()

if __name__=='__main__':
    with open('sowpods.txt', 'r') as f:
        words = f.read().split('\n')

    # pick a random word
    word = random.choice(words)
    guessed_set = set()
    secret_word = list('_' * len(word))

    incorrect_guesses = 0
    while '_' in secret_word and incorrect_guesses < 6:
        display_man(incorrect_guesses)
        display_secret_word(secret_word)
        user = input('Guess your letter: ').upper()
        if user not in guessed_set:
            index = find_letter(word, user)
            guessed_set.add(user)
            if index:
                for i in index:
                    secret_word[i] = user
            else:
                incorrect_guesses += 1
        else:
            print('Already guessed!')

    display_man(incorrect_guesses)
    if incorrect_guesses < 6:
        print(f'\nYou got it! It\'s {word!r}.')
    else:
        print(f'\nYou lost! It\'s {word!r}.\nThanks for playing!\nLet\'s play again')

