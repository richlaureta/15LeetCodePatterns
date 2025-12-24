from typing import List

def maxVowels(s: str, k: int) -> int:
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
    
    maxAverage = float('-inf')
    sumAdd = 0
    
    for index in range(0, k):
        sumAdd += nums[index]
    
    startPointer = 0
    
    maxAverage = max(maxAverage, sumAdd/k)
    
    for index in range(k, len(nums)):
        if index > len(nums) - 1:
            break
        
        sumAdd -= nums[startPointer]
        sumAdd += nums[index]
        maxAverage = max(maxAverage, sumAdd/k)
        startPointer += 1
        
    return maxAverage
        
        
def lengthOfLongestSubstring(s: str) -> int:
    #Problem #3 Longest Substring Without Repeating

    maxCount = 0
    count = 0
    memoryMap = {}
    pointer = 0
                                                   
    while pointer != len(s):
        if s[pointer] not in memoryMap:
            memoryMap[s[pointer]] = pointer
            count += 1
            if count > maxCount:
                maxCount = count
        else:
            count = 0
            pointer = memoryMap[s[pointer]]
            memoryMap = {}
        
        pointer += 1

    return maxCount

def minWindow(s: str, t: str) -> str:
    #Problem #76 Minimum Window Substring

    if t == "" or len(t) > len(s):
        return ""
    
    leftPointer = 0
    tDictionary = {}
    haveDictionary = {}
    have = 0
    minimumLength = float("infinity")
    rangeOfWindow = []

    for i in t:
        if i not in tDictionary:
            tDictionary[i] = 1
        else:
            tDictionary[i] += 1
    
    need = len(tDictionary)

    for rightPointer in range(len(s)):
        if s[rightPointer] not in haveDictionary:
            haveDictionary[s[rightPointer]] = 1
        else:
            haveDictionary[s[rightPointer]] += 1
        
        if s[rightPointer] in tDictionary and haveDictionary[s[rightPointer]] == tDictionary[s[rightPointer]]:
            have += 1
        
        while have == need:
            if (rightPointer - leftPointer) + 1 < minimumLength:
                minimumLength = (rightPointer - leftPointer) + 1
                rangeOfWindow = [leftPointer, rightPointer]
            
            haveDictionary[s[leftPointer]] -= 1
            if s[leftPointer] in tDictionary and haveDictionary[s[leftPointer]] < tDictionary[s[leftPointer]]:
                have -= 1
            leftPointer += 1

    if minimumLength != float("infinity"):
        answer = ""
        for i in range(rangeOfWindow[0], rangeOfWindow[1] + 1):
            answer += s[i]
    
        return answer
    
    return ""

if __name__ == "__main__":
    nums = [5]
    k = 1
    
    print(findMaxAverage(nums, k))