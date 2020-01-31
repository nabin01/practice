# Write a program (function!) that takes a list and returns a new list that
# contains all the elements of the first list minus all the duplicates.
#
# Extras:
#
# Write two different functions to do this - one using a loop and constructing a
# list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a
# different function.

import random

# use loop to construct a list
def remove_duplicates_from_list(a_list):
    result = []
    for item in a_list:
        if item not in result:
            result.append(item)

    return result

a_list = sorted([random.choice(range(100)) for i in range(20)])
print(a_list)
print(remove_duplicates_from_list(a_list))

# extra - use sets
def remove_duplicates(a_list):
    return sorted(list(set(a_list)))

print(remove_duplicates(a_list))

# extra - E5 using sets
a_list = sorted([random.choice(range(100)) for i in range(20)])
b_list = sorted([random.choice(range(100)) for i in range(20)])
print(a_list)
print(b_list)
print(sorted(list(set(a_list).intersection(set(b_list)))))
