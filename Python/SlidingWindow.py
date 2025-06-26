from typing import List
import sys

def maxVowels(s: str, k: int) -> int:
    #Problem # 1456. Maximum Number of Vowels in a Substring of given length

    # Count = 0
    # left = 0
    # for i in range(k):
    #     if(ord(s[i]) == 97 or  ord(s[i]) == 101 or ord(s[i]) == 105 or ord(s[i]) == 111 or ord(s[i]) == 117):
    #         Count += 1
    # aCount = Count
    # maxCount = Count
    # if Count == k: return k

    # for i in range(k, len(s)):
    #     if(ord(s[left]) == 97 or  ord(s[left]) == 101 or ord(s[left]) == 105 or ord(s[left]) == 111 or ord(s[left]) == 117):
    #         aCount -= 1
        
    #     if(ord(s[i]) == 97 or  ord(s[i]) == 101 or ord(s[i]) == 105 or ord(s[i]) == 111 or ord(s[i]) == 117):
    #         aCount += 1
        
    #     if aCount > maxCount:
    #         maxCount = aCount

    #     left += 1

    #     if maxCount == k : return k
    
    # return maxCount

    count = 0

    for i in range(k):
        if s[i] in 'aeiou':
            count += 1
    
    if count == k: return k
    
    left = 0
    maxCount = count

    for i in range(k, len(s)):
        if s[left] in 'aeiou':
            count -= 1
        if s[i] in 'aeiou':
            count += 1
        
        left += 1

        if count > maxCount:
            maxCount = count
        
        if maxCount == k: return k
    
    return maxCount


def findMaxAverage(nums: List[int], k: int) -> float:
    #Problem #643 Maximum Average Subarray I
    
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
    # nums = [1,12,-5, -6, 50, 3]
    
    # print(findMaxAverage(nums, 4))

    s = "zpuerktejfp"
    k = 3

    print(maxVowels(s, k))

if __name__ == "__main__":
    sys.exit(main())