def two_sum(numbers, target):
    
    need = {}
    index = 0
    
    for i in numbers:
        if i in need:
            for j in numbers:
                if j + i == target:
                    return [need[target-j], index]
        if target - i not in need:
            need[target - i] = index

        index += 1

    return False

print(two_sum([3,3,9], 12))