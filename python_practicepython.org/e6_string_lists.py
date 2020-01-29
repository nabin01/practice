# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

def isPalindrome(str):
    # return str == ''.join(reversed(str))
    return str == str[::-1]


user_string = input("Enter a string: ")
if isPalindrome(user_string):
    print(f'{user_string!r} is palindrome.')
else:
    print(f'{user_string!r} is not palindrome.')
