import random


def quick_sort(lis):
    if len(lis) < 2:
        return lis
    # pivot = lis.pop()
    pivot = random.choice(lis)
    lis.remove(pivot)
    greater = []
    smaller = []
    for element in lis:
        if element > pivot:
            greater.append(element)
        elif element <= pivot:
            smaller.append(element)
    left = quick_sort(smaller)
    right = quick_sort(greater)
    result = left + list([pivot]) + right
    return result


num = [10, 7, 8, 9, 1, 5, 90, 0]
print(quick_sort(num))
