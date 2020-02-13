# https://www.practicepython.org/exercise/2016/09/24/30-pick-word.html
# define a function that picks a random word from a list
# list of words - http://norvig.com/ngrams/sowpods.txt

import random

def pick_random_word(words):
    return random.choice(words)

if __name__=='__main__':
    with open('sowpods.txt', 'r') as f:
        words = f.read().split('\n')

    print(pick_random_word(words))

