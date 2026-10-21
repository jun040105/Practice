def max_window_sum(numbers, k):
    best = sum(numbers[0:k])
    temp_sum = sum(numbers[0:k])

    for i in range(1, len(numbers)-k+1):
        temp_sum = temp_sum - numbers[i-1] + numbers[i+k-1]

        if best < temp_sum:
            best = temp_sum

    return best

