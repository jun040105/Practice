def merge_list(the_list):
    if not the_list:
        return []

    intervals = sorted(the_list)
    merged = []

    for start, end in intervals:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    return merged