import sys
import heapq

def findKthLargestElement(nums: list[int], k: int) -> int:
    #Problem #215 Kth Largest Element in an Array
    
    array = []

    for i in range(0, k):
        heapq.heappush(array, nums[i])

    for i in range(k, len(nums)):
        if nums[i] > array[0]:
            heapq.heappop(array)
            heapq.heappush(array, nums[i])
    
    return array[0]

def main():
    nums = [3, 2, 1, 5, 6, 4]
    k = 3

    print(findKthLargestElement(nums, k))


if __name__ == "__main__":
    sys.exit(main())