import random
import time


# Naive search - scan entire list and ask if it's equal to the target
# if yes, return the index
# if no, then return -1
def naive_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


# Binary search - divide and conquer
# helps you search through an ordered list faster than scanning iteratively
# list must be ordered
def binary_search(lst, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(lst) - 1

    if high < low:  # can't find the target
        return -1

    midpoint = (low + high) // 2  # divide by 2 and round down

    if lst[midpoint] == target:
        return midpoint
    elif lst[midpoint] > target:
        return binary_search(lst, target, low, midpoint - 1)
    else:  # lst[midpoint] < target
        return binary_search(lst, target, midpoint + 1, high)


if __name__ == '__main__':
    # build sorted list of 10000
    length = 10000
    sorted_list = []
    while len(sorted_list) < length:
        sorted_list.append(random.randint(-3 * length, 3 * length))  # -30000 to 30000
    sorted_list = sorted(sorted_list)

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    naive_search_time = (end - start) / length
    print(f'Naive search took {naive_search_time} seconds')

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    binary_search_time = (end - start) / length
    print(f'Binary search took {binary_search_time} seconds')

    efficiency = (naive_search_time - binary_search_time) / binary_search_time * 100
    print(f'Binary search was {efficiency}% more efficient than naive search')
