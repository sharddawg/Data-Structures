def insertion_sort(lis):
    for index in range(1, len(lis)):
        current_value = lis[index]
        position = index
        while position > 0 and lis[position - 1] > current_value:
            lis[position] = lis[position - 1]
            position = position - 1
        lis[position] = current_value
    return lis


numbers = [2, 3, 81, 9, 10, 4, 19, -9, -45, 117]
sorted_array = insertion_sort(numbers)
print(sorted_array)

# Time complexity :-
# Worst case - O(n^2)
# Average - O(n^2)
# Best case - O(n)
