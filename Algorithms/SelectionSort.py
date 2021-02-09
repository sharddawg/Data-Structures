def selection_sort(lis):
    for i in range(0, len(lis)):
        minimum = lis[i]
        for index in range(i + 1, len(lis)):
            if minimum > lis[index]:
                minimum = lis[index]
                temp = lis[i]
                lis[i] = minimum
                lis[index] = temp
    return lis


numbers = [12, 56, 34, 32, 0, 17, 986, -87, -117]
selection_sort(numbers)
print(numbers)

# Time complexity :-
# Worst case - O(n^2)
# Average - O(n^2)
# Best case - O(n^2)
