# https://www.practicepython.org/exercise/2017/01/02/31-guess-letters.html
# let the player guess one letter until the word is completed

import random

def display_secret_word(secret_word):
    for char in secret_word:
        print(char, end=' ')
    print()

def find_letter(word, char):
    return [i for i, ch in enumerate(word) if ch == char]

if __name__=='__main__':
    with open('sowpods.txt', 'r') as f:
        words = f.read().split('\n')

    # pick a random word
    word = random.choice(words)
    guessed_set = set()
    secret_word = list('_' * len(word))

    while '_' in secret_word:
        display_secret_word(secret_word)
        user = input('Guess your letter: ').upper()
        if user not in guessed_set:
            index = find_letter(word, user)
            guessed_set.add(user)
            if index:
                for i in index:
                    secret_word[i] = user
            else:
                print('Incorrect!')
        else:
            print('Already guessed!')

    print(f'You got it! It\'s {word!r}.')

