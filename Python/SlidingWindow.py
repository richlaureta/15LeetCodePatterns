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
    #Problem #76 Minimum Window Substring AI GENERATED SOLUTION GOOGLE CLI GEMINI

    if t == "" or len(t) > len(s):
        return ""
    
    tDictionary = {}
    for char in t:
        tDictionary[char] = 1 + tDictionary.get(char, 0)

    window = {}
    res = [-1, -1]
    resLen = float("infinity")
    
    l = 0
    have = 0
    need = len(tDictionary)
      
    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)

        if c in tDictionary and window[c] == tDictionary[c]:
            have += 1
        
        while have == need:
            # update our result
            if (r - l + 1) < resLen:
                res = [l, r]
                resLen = (r - l + 1)

            # pop from the left of our window
            left_char = s[l]
            window[left_char] -= 1
            if left_char in tDictionary and window[left_char] < tDictionary[left_char]:
                have -= 1
            l += 1

    l, r = res
    
    return s[l:r+1] if resLen != float("infinity") else ""    

if __name__ == "__main__":
    s = "a"
    t = "aa"
    
    print(minWindow(s, t))