import sys

def merge(intervals: list[list[int]]) -> list[list[int]]:
    #Problem #56 Merge Intervals
    
    intervals.sort(key = lambda time: time[0])
    merged = [intervals[0]]

    for index in range(1, len(intervals)):
        if intervals[index][0] <= merged[len(merged) - 1][1] and intervals[index][1] > merged[len(merged) - 1][1]:
            merged[len(merged) - 1][1] = intervals[index][1]
        elif intervals[index][0] > merged[len(merged) - 1][1]:
            merged.append(intervals[index])

    return merged

def main():
    # intervals = [[1,3],[0,2],[2,3],[4,6],[4,5],[5,5],[0,2],[3,3]]
    # intervals = [[1,3],[2,6],[8,10],[15,18]]
    intervals = [[1, 4], [0, 1]]
    print(merge(intervals))

if __name__ == "__main__":
    sys.exit(main())