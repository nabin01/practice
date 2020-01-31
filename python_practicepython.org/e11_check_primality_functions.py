# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.)
# You can (and should!) use your answer to Exercise 4 to help you. Take this
# opportunity to practice using functions, described below.

def isPrime(num):
    for i in range(2, int(num / 2 + 1)):
        if num % i == 0:
            return False

    return True;

num = int(input("Enter a number: "))
if num < 2:
    print(f'By the definition of prime numbers, any number less than 2 is not prime.')
elif isPrime(num):
    print(f'{num} is prime!')
else:
    print(f'{num} is not prime!')
