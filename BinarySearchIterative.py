def binary_search(lis, key):
    low = 0
    high = len(lis) - 1
    while high >= low:
        mid = (low + high) // 2
        if lis[mid] == key:
            return mid
        elif key > lis[mid]:
            low = mid + 1
        else:
            high = mid - 1


numbers = [0, 2, 4, 12, 18, 20, 118, 200, 700]
while True:
    value = int(input("What is the value of the element you want to search? - "))
    index = binary_search(numbers, value)
    if index is None:
        print(f'The number {value} is not in the array')
    else:
        print(f'The number {value} is in the array. It is at index {index}')

# Time complexity :-
# Worst case - O(log(n))
# Average - O(log(n))
# Binary search uses the divide and conquer method
