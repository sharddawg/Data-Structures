def bubble_sort(lis):
    for i in range(len(lis)):
        for j in range(len(lis)):
            if lis[j] > lis[i]:
                temp = lis[i]
                lis[i] = lis[j]
                lis[j] = temp
    return lis


numbers = [12, 2, 4, 20, 18, 23, 1, 6, -2, -10, 9]
sorted_array = bubble_sort(numbers)
print(sorted_array)

# Time complexity :-
# Worst case - O(n^2)
# Average - O(n^2)
# Best case - O(n)
