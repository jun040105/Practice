def find_largest(numbers):
    result = numbers[0]
    for x in numbers:
        if x > result:
            result = x

    return result

print(find_largest([1, 2, 3, 4, 5]))