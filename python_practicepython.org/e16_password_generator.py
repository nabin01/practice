# Write a password generator in Python. Be creative with how you generate
# passwords - strong passwords have a mix of lowercase letters, uppercase letters,
# numbers, and symbols. The passwords should be random, generating a new password
# every time the user asks for a new password. Include your run-time code in a
# main method.
#
# Extra:
#
#     Ask the user how strong they want their password to be. For weak passwords,
#     pick a word or two from a list.

import string
import random

def generate_random_password(length = 8, char_sequence = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation):
    password = ''.join(random.choice(char_sequence) for i in range(1, length + 1))
    # password = ''.join(random.sample(char_sequence, length)) # don't use this since it does not allow repitition
    return password

# print(generate_random_password())

# extra
# def generate_password_with_strength(strength = '3'):
#      # by default very strong password
#      char_sequence = {
#      # weak passwords
#      '1': ['password', 'welcome', 'incorrect', 'letmein', 'coding', 'coder'],
#      # strong passwords = lowercase + uppercase + numbers
#      '2': string.ascii_lowercase + string.ascii_uppercase + string.digits,
#      # very strong passwords = add punctuation to 2
#      '3': string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
#      }
#      if strength == '1': # join either 1 or 2 words from the list
#          password = ''.join(i for i in random.sample(char_sequence.get('1'), random.randint(1,2)))
#      elif strength == '2': # 12 characters password
#          password = ''.join(random.choice(char_sequence.get('2')) for i in range(1, 12))
#      elif strength == '3': # 16 character password
#          password = ''.join(random.choice(char_sequence.get('3')) for i in range(1, 16))
#      else:
#          return 'Not valid input!'
#      return password
#
# print(generate_password_with_strength(input("Enter strength level (1,2,3): ")))
