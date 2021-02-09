def LCS(s1, s2):
    result = ''
    index1 = 0
    for j in s2:
        for i in s1[index1:]:
            if j == i:
                result += i
                if index1 == len(s1) - 1:
                    index1 = s1[index1:].index(i) + index1
                else:
                    index1 = s1[index1:].index(i) + index1 + 1
                break
    return result


string1 = "acbgtdfgq"
string2 = "bgfrdeq"
print(LCS(string1, string2))
print(LCS(string2, string1))


