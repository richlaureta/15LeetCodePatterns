from operator import itemgetter

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
    
    newIntervalsList = []
    insertedFlag = False
    index = 0
    
    for interval in intervals:
        if (newInterval[0] >= interval[0] and 
            newInterval[0] <= interval[1] and 
            newInterval[1] >= interval[1]):
            newIntervalsList.append([interval[0], newInterval[1]])
            insertedFlag = True
            break
        elif (newInterval[0] >= interval[0] and 
            newInterval[0] < interval[1] and 
            newInterval[1] < interval[1]):
            newIntervalsList.append([interval[0], interval[1]])
            insertedFlag = True
            break
        elif (newInterval[0] == interval[0] and
              newInterval[1] == interval[1]):
            newIntervalsList.append([newInterval[0], newInterval[1]])
            insertedFlag = True
            break
        elif (newInterval[0] < interval[0] and
              newInterval[1] >= interval[0] and 
              newInterval[1] < interval[1]):
            newIntervalsList.append([newInterval[0], interval[1]])
            insertedFlag = True
            break
        elif newInterval[1] < interval[0]:
            newIntervalsList.append([newInterval[0], newInterval[1]])
            newIntervalsList.append([interval[0], interval[1]])
            insertedFlag = True
            break
        elif newInterval[0] > interval[1]:
            newIntervalsList.append([interval[0], interval[1]])
        
        index += 1
        
    index += 1

    for index1 in range(index, len(intervals)):
        previousInterval = newIntervalsList[len(newIntervalsList) - 1]
        
        if (previousInterval[0] < intervals[index1][0] and
            previousInterval[1] < intervals[index1][1] and
            previousInterval[1] >= intervals[index1][0]):
            newIntervalsList.pop()
            newIntervalsList.append([previousInterval[0], intervals[index1][1]])
        elif previousInterval[1] < intervals[index1][0]:
            newIntervalsList.append([intervals[index1][0], intervals[index1][1]])
    
    if insertedFlag == False:
        newIntervalsList.append(newInterval)
           
    return newIntervalsList
        
def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
    #Problem #435 Non-Overlapping Intervals - Medium
    
    endTimeSort = sorted(intervals, key = itemgetter(1))
    
    previousInterval = endTimeSort[0][1]
    
    minimumOverlapCount = 0
    
    for index in range(1, len(endTimeSort)):
        if endTimeSort[index][0] < previousInterval:
            minimumOverlapCount += 1
        else:
            previousInterval = endTimeSort[index][1]
    
    return minimumOverlapCount

if __name__ == "__main__":
    intervals = [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]
    
    print(eraseOverlapIntervals(intervals))