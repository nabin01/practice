# Take a list, say for example this one:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# and write a program that prints out all the elements of the list that are less than 5.
#
# Extras:
#
#     Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
#     Write this in one line of Python.
#     Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for item in a:
    if item < 5:
        print(item)

# # extra
# # create a new list
# new_list = []
# # for item in a:
# #     if item < 5:
# #         new_list.append(item)
#
# # one line
# new_list = [item for item in a if item < 5] # [return] for [item] in [list] if [filter]
# [new_list.append(item) for item in a if item < 5]

# # filtering from user input
# user_number = int(input("Enter a number: "))
# new_list = [item for item in a if item < user_number]
#
# # prin new list
# for item in new_list:
#     print(item)
