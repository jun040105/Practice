def longest_streak(days: list[int]) -> int:

    if not days:
        return 0

    days = sorted(days)

    prev = days[0]
    count = 1
    best = 0

    for i in days:
        if prev != i:

            if i == prev + 1:
                count += 1
            else:
                count = 1

        if best < count:
            best = count

        prev = i

    return best