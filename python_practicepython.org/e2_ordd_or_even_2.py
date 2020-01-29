# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
#
# Extras:
#
# If the number is a multiple of 4, print out a different message
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

# user input
user_number = int(input("Enter a number: "))

if user_number % 2 == 0: # % gives remainder; 0 is printed as even too; add a condition before this to fix that
    print(f'{user_number} is even.')
else:
    print(f'{user_number} is odd.')

# extra
#  printing different for divisible by 4
if user_number % 4 == 0:
    print(f'{user_number} is divisible by 4.')
elif user_number % 2 == 0: # % gives remainder
    print(f'{user_number} is even.')
else:
    print(f'{user_number} is odd.')

# function style
def check_divisibility(num, check):
    return num % check == 0

num = int(input("Enter dividend: "))
check = int(input("Enter divisor: "))

if check_divisibility(num, check):
    print(f'{num} is evenly divisible by {check}.')
else:
    print(f'{num} is not evenly divisible by {check}.')
