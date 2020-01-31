# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to
# guess the number, then tell them whether they guessed too low, too high, or
# exactly right. (Hint: remember to use the user input lessons from the very first
# exercise)
#
# Extras:
#
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends,
# print this out.

import random

secret_num = random.randint(1, 9)
guess = int(input(f'Guess a number: '))
if secret_num == guess:
    print('You win!')
if secret_num < guess:
    print(f'Too High')
else: # secret_num > guess
    print(f'Too Low')

# extra
# guess_count = 0
# guess = input(f'Guess a number (or exit to end the game): ')
# while guess != 'exit':
#     guess_count += 1
#     if secret_num == int(guess):
#         print('You win!')
#         break;
#     if secret_num < int(guess):
#         print(f'Too High')
#     else: # secret_num > int(guess)
#         print(f'Too Low')
#     guess = input(f'Guess a number (or exit to end the game): ')
#
# print(f'You took {guess_count} guesses!')

# allow only 3 guesses
# secret_num = random.randint(1, 9)
# guess_count = 3 # maximum three guesses
# guess = int(input(f'{guess_count} Lives\nGuess a number: '))
# is_correct = True
# guess_count -= 1
#
# print(secret_num)
# while secret_num != guess and guess_count > 0:
#     is_correct = False
#     if secret_num < guess:
#         print(f'Too High')
#     else: # secret_num > guess
#         print(f'Too Low')
#     guess = int(input(f'{guess_count} Lives\nGuess a number: '))
#     if secret_num == guess:
#         is_correct = True
#     guess_count -= 1
#
# if (is_correct):
#     print(f'You win!')
# else:
#     print(f'You lose!')
