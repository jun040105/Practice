def find_frequency_above(numbers):
    
    counts = {}

    for x in numbers:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1

    result = 0

    for key, frequency in counts.items():
        if frequency > 1:
            result += 1

    return result