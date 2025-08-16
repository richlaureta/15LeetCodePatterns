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

    if t == "":
        return ""
    
    tDictionary = {}
    haveDicionary = {}
    minimumLength = float("infinity")
    arrayRange = []
    leftPointer = 0
    have = 0
    need = len(t)

    for i in t:
        if i not in tDictionary:
            tDictionary[i] = 1
        else:
            tDictionary[i] += 1
      
    
    for rightPointer in range(len(s)):
        if s[rightPointer] not in haveDicionary:
            haveDicionary[s[rightPointer]] = 1
        else:
            haveDicionary[s[rightPointer]] += 1
            

        if s[rightPointer] in tDictionary and haveDicionary[s[rightPointer]] == tDictionary[s[rightPointer]]:
            have += 1
        
        while have == need:
            if (rightPointer - leftPointer + 1) < minimumLength:
                arrayRange = [leftPointer, rightPointer]
                minimumLength = (rightPointer - leftPointer) + 1

            haveDicionary[s[leftPointer]] -= 1
            if s[leftPointer] in tDictionary and haveDicionary[s[leftPointer]] < tDictionary[s[leftPointer]]:
                have -= 1
            leftPointer += 1

    if minimumLength == float("infinity"):
        return ""
    else:
        answer = ""
        for i in range(leftPointer - 1, rightPointer + 1):
            answer += s[i]
        return answer    

if __name__ == "__main__":
    s = "a"
    t = "aa"
    
    print(minWindow(s, t))