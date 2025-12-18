def merge(intervals: list[list[int]]) -> list[list[int]]:
    #Problem #56 Merge Intervals
    
    if not intervals:
        return []

    intervals.sort(key = lambda time: time[0])
    merged = [intervals[0]]

    for index in range(1, len(intervals)):
        if intervals[index][0] <= merged[len(merged) - 1][1] and intervals[index][1] > merged[len(merged) - 1][1]:
            merged[len(merged) - 1][1] = intervals[index][1]
        elif intervals[index][0] > merged[len(merged) - 1][1]:
            merged.append(intervals[index])

    return merged

def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    #Problem #57 Insert Interval
    
    intervals.append(newInterval)

    return merge(intervals)

def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
    #Problem #435 Non-Overlapping Intervals - Medium
    
    if len(intervals) == 1:
        return 0
    
    intervals.sort(key = lambda time: time[1])
    
    keepCount = 1

    previousEndTime = intervals[0][1]

    for index in range(1, len(intervals)):
        if intervals[index][0] >= previousEndTime:
            keepCount += 1
            previousEndTime = intervals[index][1]

    return len(intervals) - keepCount

if __name__ == "__main__":
    intervals = [[1, 2], [2, 3]]

    print(eraseOverlapIntervals(intervals))