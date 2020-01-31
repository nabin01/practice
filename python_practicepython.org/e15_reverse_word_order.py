# Write a program (using functions!) that asks the user for a long string
# containing multiple words. Print back to the user the same string, except with
# the words in backwards order. For example, say I type the string:
#   My name is Michele
#
# Then I would see the string:
#
#   Michele is name My
#
# shown back to me.

def reverse_str(user_str):
    return ' '.join(user_str.split()[::-1])

user_str = input('Enter a line: ')
print(reverse_str(user_str))
