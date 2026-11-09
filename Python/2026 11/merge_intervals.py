def merge_intervals(intervals):

    if not intervals:
        return []

    intervals = sorted(intervals)
    returnvals = [intervals[0]]

    for i in range(1, len(intervals)):
        if returnvals[-1][1] >= intervals[i][0]:
            returnvals[-1][1] = max(returnvals[-1][1], intervals[i][1])
        else:
            returnvals.append(intervals[i])
        
    return returnvals

print (merge_intervals([[8, 10], [1, 3], [9, 12], [2, 6]]))



