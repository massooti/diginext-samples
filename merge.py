def mergeIntervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

# Example:
input_intervals = [[1, 3], [2, 6], [8, 10]]
output = mergeIntervals(input_intervals)
print(output)  # Output: [[1, 6], [8, 10]]
