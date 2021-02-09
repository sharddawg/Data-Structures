def LIS(num):
    temp = [1] * len(num)
    i, j = 1, 0
    while i < len(num) and j < len(num):
        if num[j] < num[i]:
            if temp[j] + 1 > temp[i]:
                temp[i] = temp[j] + 1
        j = j + 1
        if j == i:
            j = 0
            i = i + 1
    return max(temp)


num = [1, 3, 5, 4, 7]
print(LIS(num))
