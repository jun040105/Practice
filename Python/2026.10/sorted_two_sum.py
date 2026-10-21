def sorted_twosum(numbers, target):

    start, end = 0, len(numbers)-1

    while start < end:

        if numbers[start] + numbers[end] > target:
            end -= 1
        elif numbers[start] + numbers[end] < target:
            start += 1
        else:
            return [start, end]

    return None

