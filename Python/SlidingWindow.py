from collections import defaultdict
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


def findMaxAverage(nums: list[int], k: int) -> float:
    #Problem #643 Maximum Average Subarray I - Easy
    
    #Create a variable maxAverage equal to the lowest possible integer. O(1) space complexity.
    maxAverage = float('-inf')
    #Create a variable to sum all the contiguous lengths of k. O(1) space complexity.
    sumAdd = 0
    
    #Iterate through the length of k and add them. O(k) time complexity.
    for index in range(0, k):
        sumAdd += nums[index]
    
    #Create a variable for the startPointer index equal to 0. O(1) space complexity.
    startPointer = 0
    #Take the maximum average between the current maximum average and the new one. 
    maxAverage = max(maxAverage, sumAdd/k)
    
    #Iterate through the nums. O(n - k) time complexity.
    for index in range(k, len(nums)):
        #Subtract the nums[startPointer] from sumAdd.
        sumAdd -= nums[startPointer]
        #Add the current nums[index] to sumAdd.
        sumAdd += nums[index]
        #Take the maximum average between the current maximum average and the new one. 
        maxAverage = max(maxAverage, sumAdd/k)
        #Increment the startPointer by 1.
        startPointer += 1
    
    #Return maxAverage.
    return maxAverage
        
def lengthOfLongestSubstring(s: str) -> int:
    #Problem #3 Longest Substring Without Repeating Characters - Medium
    
    #Create a default dictionary variable. O(n) space complexity.
    letterIndexDictionary = defaultdict(int)
    #Create a startingPoint variable. O(1) space complexity.
    startingPoint = 0
    
    #Create a longestSubstringCount variable. O(1) space complexity.
    longestSubstringCount = 0
    #Create a uniqueCount variable. O(1) space complexity.
    uniqueCount = 0
    
    #Iterate through the string s. O(n) time complexity.
    for index in range(0, len(s)):
        #If the character in s[index] is not in the dictionary.
        if s[index] not in letterIndexDictionary:
            #Make the character key equal to the index.
            letterIndexDictionary[s[index]] = index
            #Increment uniqueCount by 1.
            uniqueCount += 1
        #Else if the s[index] is not in the dictionary.
        else:
            #Get the maximum between longestSubstringCount and uniqueCount.
            longestSubstringCount = max(longestSubstringCount, uniqueCount)
            
            #Get the previous starting point.
            previousStartingPoint = startingPoint
            #Make the startingPoint equal to the letterIndexDictionary[s[index]] + 1.
            startingPoint = letterIndexDictionary[s[index]] + 1
            #Set uniqueCount equal to the index minus the new starting point + 1.
            uniqueCount = index - startingPoint + 1
            
            #Iterate from the previous StartingPoint to the letterIndexDictionary[s[index]] + 1. 
            # O(n) * O(log n) time complexity.
            for index1 in range(previousStartingPoint, letterIndexDictionary[s[index]] + 1):
                #Delete the previous character that got repeated.
                del letterIndexDictionary[s[index1]]
            
            #Create a new character that has the new index.
            letterIndexDictionary[s[index]] = index
                        
    #Get the maximum between longestSubstringCount and uniqueCount.
    longestSubstringCount = max(longestSubstringCount, uniqueCount)
    
    #Return the longestSubstringCount.
    return longestSubstringCount

def minWindow(s: str, t: str) -> str:
    #Problem #76 Minimum Window Substring - Hard

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
    s = "abcdefghd"
    
    print(lengthOfLongestSubstring(s))