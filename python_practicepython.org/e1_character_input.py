# Exercise 1 - Character Input
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
#
# Extras:
#
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

import datetime # to get current year

# getting input from user
name = input("Name: ")
age = int(input("Age: "))

# print
# print(f'Hi {name}, you will be turning 100 years old on the year {((2020 - age ) + 100 )}.') # 2020 - age gives the birth year so add 100 to that
print(f'Hi {name}, you will be turning 100 years old on the year {((datetime.datetime.now().year - age ) + 100 )}.')

# extra
favourite_number = int(input("Favourite Number: "))
print(favourite_number * f'Hi {name}, you will be turning 100 years old on the year {((datetime.datetime.now().year - age ) + 100 )}.\n')
