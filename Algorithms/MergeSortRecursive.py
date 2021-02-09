def merge(lis1, lis2):
    result = []
    a = len(lis1) - 1
    b = len(lis2) - 1
    c = a + b + 2
    i, j = 0, 0
    while len(result) != c:
        if lis1[i] < lis2[j]:
            result.append(lis1[i])
            i += 1
        else:
            result.append(lis2[j])
            j += 1
        if i > a:
            result.extend(lis2[j:])
        elif j > b:
            result.extend(lis1[i:])
    return result


def mergesort(array):
    if len(array) < 2:
        return array
    mid = len(array)//2
    left = mergesort(array[:mid])
    right = mergesort(array[mid:])
    return merge(left, right)


lis = [11, 2, 7, 99, 0, 14]
print(mergesort(lis))

