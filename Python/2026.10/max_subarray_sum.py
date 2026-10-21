def max_subarray_sum(numbers):

    best = numbers[0]

    for i in range(len(numbers)):

        current_sum = 0 

        for j in range(i, len(numbers)):
            current_sum += numbers[j]

            if current_sum > best:
                best = current_sum

    return best


print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))