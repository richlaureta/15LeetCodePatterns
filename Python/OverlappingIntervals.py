import unittest

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

class TestIntervalFunctions(unittest.TestCase):
    def test_merge(self):
        self.assertEqual(merge([[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]])
        self.assertEqual(merge([[1,4],[4,5]]), [[1,5]])
        self.assertEqual(merge([[1,4],[2,3]]), [[1,4]])
        self.assertEqual(merge([]), [])
        self.assertEqual(merge([[1,5]]), [[1,5]])
        self.assertEqual(merge([[1,2],[3,4],[5,6]]), [[1,2],[3,4],[5,6]])

    def test_insert(self):
        self.assertEqual(insert([[1,3],[6,9]], [2,5]), [[1,5],[6,9]])
        self.assertEqual(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]), [[1,2],[3,10],[12,16]])
        self.assertEqual(insert([[3,5],[8,10]], [1,2]), [[1,2],[3,5],[8,10]])
        self.assertEqual(insert([[1,3],[6,9]], [10,12]), [[1,3],[6,9],[10,12]])
        self.assertEqual(insert([], [5,7]), [[5,7]])
        self.assertEqual(insert([[1,5]], [2,3]), [[1,5]])
        self.assertEqual(insert([[1,5]], [2,7]), [[1,7]])

if __name__ == "__main__":
    unittest.main()
