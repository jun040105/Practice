from collections import Counter

def min_deletion(first, second):
    first = Counter(first)
    second = Counter(second)

    for i in first:
        if i in second:
            while first[i] != 0 and second[i] != 0:
                first[i] -= 1
                second[i] -= 1

    total = 0

    for i in first:
        total += first[i]

    for i in second:
        total += second[i]

    return total

print(min_deletion(str(input()), str((input()))))