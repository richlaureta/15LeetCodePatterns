from typing import List
import sys

def findMaxAverage(nums: List[int], k: int) -> float:
    #Problem #643
    leftMostIndex = 0
    rightMostIndex = k
    total = 0
    maxValue = 0

    for i in range(leftMostIndex, k):
        total += nums[i]
    maxValue = total
    
    for i in range(rightMostIndex, len(nums)):
        total += nums[i]
        total -= nums[leftMostIndex]
        leftMostIndex += 1

        if total > maxValue:
            maxValue = total

    return float(maxValue/k)


def main():
    nums = [1,12,-5, -6, 50, 3]
    
    print(findMaxAverage(nums, 4))

if __name__ == "__main__":
    sys.exit(main())