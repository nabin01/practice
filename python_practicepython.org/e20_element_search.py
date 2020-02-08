# Write a function that takes an ordered list of numbers (a list where the
# elements are in order from smallest to largest) and another number. The
# function decides whether or not the given number is inside the list and
# returns (then prints) an appropriate boolean.
#
# Extras:
#
#     Use binary search.

def search_a_list(ordered_list, key):
    # return key in ordered_list
    for item in ordered_list:
        if key == item:
            return True
    return False

def binary_search(ordered_list, key):
    start = 0
    end = len(ordered_list) - 1
    mid = int((start + end) / 2)
    while (mid >= start and mid <= end):
        # print(start, mid, end, ordered_list)
        if ordered_list[mid] == key:
            return True
        elif key < ordered_list[mid]:
            end = mid - 1
            mid = int((start + end) / 2)
        # else:
        elif key > ordered_list[mid]:
            start = mid + 1
            mid = int((start + end) / 2)
    return False
    # using recursion
    # mid = int(len(ordered_list) / 2)
    # print(mid, ordered_list)
    # if mid >= len(ordered_list):
    #     return False
    # if key == ordered_list[mid]:
    #     return True
    # elif key < ordered_list[mid]:
    #     return binary_search(ordered_list[:mid], key)
    # else:
    #     return binary_search(ordered_list[mid+1:], key)
    # return False


if __name__=='__main__':
    # print(search_a_list([1,2,3,4,5], 2))
    ordered_list = list(range(1,100))
    print(binary_search(ordered_list, 99))
