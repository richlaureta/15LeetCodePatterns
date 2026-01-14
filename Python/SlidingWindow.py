from collections import defaultdict

def decrypt(code: list[int], k: int) -> list[int]:
    #Problem #1652 Defuse the Bomb - Easy
    
    if k == 0:
        return [0] * len(code)
    
    bombCodeArray = []
    
    for index in range(len(code)):
        if k > 0:
            index2 = index + 1
        else:
            index2 = index - 1
        sum = 0
        for index1 in range(abs(k)):
            if k > 0 and len(code) == index2:
                index2 = 0
            elif k < 0 and index2 == -1:
                index2 = len(code) - 1
            
            sum += code[index2]
            
            if k > 0:
                index2 += 1
            else:
                index2 -= 1
                
        bombCodeArray.append(sum)
        
    return bombCodeArray    
            

def countGoodSubstrings(s: str) -> int:
    #Problem #1876 Substrings if Size Three With Distinct Characters - Easy
    
    index = 0
    goodCount = 0
    
    while index + 2 < len(s):
        if (s[index] != s[index + 1] and 
            s[index] != s[index + 2] and 
            s[index + 1] != s[index + 2]):
            
            goodCount += 1
        
        index += 1

    return goodCount
        
def maxVowels(s: str, k: int) -> int:
    #Problem #1456 Maximum Number of Vowels in a Substring of Given Length - Medium
    
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
    #Problem #76 Minimum Window Substring - Hard - Solution Concept By YouTube Channel Deepti Talesra - Understanding the Solution
    
    #Initialize a dictionary for string t.
    tDictionary = defaultdict(int)
    
    #Iterate through the t letters and count the frequency.
    for index in range(len(t)):
        tDictionary[t[index]] += 1

    #Initialize a leftMostPointer.
    leftMostPointer = 0
    #Initialize a rightMostPointer.
    rightMostPointer = 0
    
    #Initialize a formed variable. We increment this if we satisfy the frequency of a letter.
    formed = 0
    #Initialize a total variable. This is the total amount that we have to meet. 
    total = len(tDictionary)
    
    #Initialize a minimum count of the substring that satisfies the frequency of t.
    minimumSubstring = float('inf')
    #Initialize a leftIndex to keep track of the minimum length index.
    leftIndex = 0
    #Initialize a rightIndex to keep track of the minimum length index.
    rightIndex = 0
    
    #Initialize a while loop whilst rightMostPointer is less than the length of s.
    while rightMostPointer < len(s):
        #If the index character of string s is in the dictionary, decrement it by one.
        if s[rightMostPointer] in tDictionary:
            tDictionary[s[rightMostPointer]] -= 1
            
            #If the dictionary key is equal to 0, then we increment the formed by 1.
            if tDictionary[s[rightMostPointer]] == 0:
                formed += 1
        
        #We initialize another while loop with the condition if formed is equal to the 
        # variable total, and if the leftMostPointer is less than or equal to rightMostPointer.        
        while formed == total and leftMostPointer <= rightMostPointer:
            #If the length of rightMostPointer minus leftMostpointer + 1 is less than the minimumSubstring, 
            # then update the minimumSubstring length and update the leftIndex and rightIndex to take up 
            # the minimum length.
            if rightMostPointer - leftMostPointer + 1 < minimumSubstring:
                minimumSubstring = rightMostPointer - leftMostPointer + 1
                leftIndex = leftMostPointer
                rightIndex = rightMostPointer 
            
            #If the leftMostPointer index s is in the dictionary, then increment the key by 1.
            if s[leftMostPointer] in tDictionary:
                tDictionary[s[leftMostPointer]] += 1
                
                #If it equals 1, decrement the variable "formed" by 1.
                if tDictionary[s[leftMostPointer]] == 1:
                    formed -= 1
                    
            #Increment the leftMostPointer.
            leftMostPointer += 1
            
        #Increment the rightMostPointer.    
        rightMostPointer += 1
    
    #Return an empty no-space string if it is infinity, otherwise return the leftIndex and rightIndex length of s.
    return "" if minimumSubstring == float('inf') else s[leftIndex:rightIndex + 1]
        
if __name__ == "__main__":
    code = [2, 4, 9, 3]
    k = -2
    
    print(decrypt(code, k))