import sys
from typing import List

def prefixSum(numbers: List[int]):
    for i in range(1, len(numbers)):
            numbers[i] += numbers[i - 1]

class NumArray:
    
    def __init__(self, nums: List[int]):
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        self.prefixSumArray = nums

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefixSumArray[right]
        else:
            return (self.prefixSumArray[right] - self.prefixSumArray[left - 1])

def main():
    nums: List[int] = [-2,0,3,-5,2,-1]

    prefixSum(nums)
    
    print(nums)

if __name__ == "__main__":
    sys.exit(main())