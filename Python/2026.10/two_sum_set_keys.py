def two_sum(numbers, target):
    
    need = set()
    
    for i in numbers:
        if i in need:
            return True
        if target - i not in need:
            need.add(target - i)

    return False

print(two_sum([3,3], 6))