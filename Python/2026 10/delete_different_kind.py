from collections import Counter

def del_diff_letters(first, second):
    f, s = Counter(first), Counter(second)
    deletes = 0

    for i in f:
        if i not in s:
            deletes += f[i]

    for i in s:
        if i not in f: 
            deletes += s[i]

    return deletes


print(del_diff_letters("aabbcc", "aabcdef"))