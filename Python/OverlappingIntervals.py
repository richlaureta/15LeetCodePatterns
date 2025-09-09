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
    #Problem #435 Non-Overlapping Intervals

    intervals.sort(key = lambda time: time[1])
    
    removalCount = 0
    previousEndTime = 0

    

    return removalCount

if __name__ == "__main__":
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]

    eraseOverlapIntervals(intervals)