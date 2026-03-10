def merge(intervals: list[list[int]]) -> list[list[int]]:
    #Problem #56 Merge Intervals - Medium
    intervals.sort()
    
    newMergedIntervalsList = [intervals[0]]
    for index in range(len(intervals) - 1):
        previous = [newMergedIntervalsList[len(newMergedIntervalsList) - 1][0], newMergedIntervalsList[len(newMergedIntervalsList) - 1][1]]
        
        if previous[1] >= intervals[index + 1][0]:
            if intervals[index + 1][1] < previous[1]:
                newMergedIntervalsList.pop()
                newMergedIntervalsList.append([previous[0], previous[1]])
            else:
                newMergedIntervalsList.pop()
                newMergedIntervalsList.append([previous[0], intervals[index + 1][1]])
        else:
            newMergedIntervalsList.append([intervals[index + 1][0], intervals[index + 1][1]])
        
    return newMergedIntervalsList

def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    #Problem #57 Insert Interval - Medium
    
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
    intervals = [[1,4],[1,4]]

    print(merge(intervals))