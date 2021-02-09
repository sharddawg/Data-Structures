def binary_search(lis, low, high, key):
    if low == high:
        if lis[low] == key:
            return low
        else:
            return False
    else:
        mid = (low + high) // 2
        if key > lis[mid]:
            return binary_search(lis, mid + 1, high, key)
        else:
            return binary_search(lis, low, mid, key)


numbers = [1,2,3]
while True:
    value = int(input("Enter value to search - "))
    index = binary_search(numbers, 0, len(numbers) - 1, value)
    if index is False:
        print("Element does not exist in this array")
    else:
        print(f'The element is at position {index} ')
