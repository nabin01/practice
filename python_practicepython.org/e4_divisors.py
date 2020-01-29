# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

# user input
user_number = int(input("Enter a number: "))
divisors = [1, ] # list to add divisors; 1 is a divisor of any number

for i in range(2, int(user_number/2 + 1)): # no number greater than half is a divisor
    if user_number % i == 0:
        divisors.append(i)

divisors.append(user_number) # a number divides itself evenly
print(divisors)
