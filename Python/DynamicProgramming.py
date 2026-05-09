from collections import defaultdict
from collections import deque

def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    array = [0] * (n + 1)

    array[0] = 0
    array[1] = 1
    for i in range(2, len(array)):
        array[i] = array[i-2] + array[i-1]

    return array[n]

def fib1(n: int) -> int:
    #Problem #509 Fibonacci Number - Easy - Solution Concept by YouTube Channel Greg Hogg - Understanding the Solution
    
    sequenceDictionary = {0: 0, 1:1}
    
    def function(number: int) -> int :
        if number in sequenceDictionary:
            return sequenceDictionary[number]
        else:
            sequenceDictionary[number] = function(number - 1) + function(number - 2)
            return sequenceDictionary[number]
        
    return function(n)

def climbStairs(n: int) -> int:
    #Problem #70 Climbing Stairs - Easy
    
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    previousNumber = 1
    currentNumber = 2
    
    for index in range(n - 2):
        temporaryNumber = previousNumber
        previousNumber = currentNumber
        currentNumber = temporaryNumber + currentNumber
        
    return currentNumber

def climbStairs1(n: int):
    #Problem #70 Climbing Stairs - Easy
    
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    nMinus2 = 1
    nMinus1 = 2
    current = 0
    for i in range(2, n):
        current = nMinus2 + nMinus1
        nMinus2 = nMinus1
        nMinus1 = current
    
    return current
    
def coinChange(coins: list[int], amount: int) -> int:
    #Problem #322 Coin Exchange - Medium - Solution Concept by YouTube Channel NeetCode - Understanding the Solution
    
    numberCoin = [amount + 1] * (amount + 1)
    numberCoin[0] = 0
    
    for amount1 in range(1, amount + 1):
        for coin in coins:
            if amount1 - coin >= 0:
                numberCoin[amount1] = min(numberCoin[amount1], 1 + numberCoin[amount1 - coin])
    
    return numberCoin[amount] if numberCoin[amount] != amount + 1 else -1
 
def coinChange1(coins: list[int], amount: int) -> int:
    #Problem #322 Coin Exchange - Medium - Solution Concept by YouTube Channel Greg Hogg - Understanding the Solution
    
    coins.sort()
    indices = [0] * (amount + 1)
    
    for i in range(1, amount + 1):
        minimum = float('inf')
        
        for coin in coins:
            difference = i - coin
            
            if difference < 0:
                break
            
            minimum = min(minimum, indices[difference] + 1)
        
        indices[i] = minimum
    
    if indices[amount] < float('inf'):
        return indices[amount]
    else:
        return -1

def lengthOfLIS(nums: list[int]) -> int:
    #Problem #300 Longest Increasing Subsequence - Medium - Time Limit Exceeded
    
    indexIncreasingSubsequence = defaultdict(list[int])
    
    for index in range(len(nums)):
        for index1 in range(0, index):
            if nums[index] > nums[index1]:
                indexIncreasingSubsequence[index1].append(index)
    
    longestIncreasingCount = [1]

    def depthFirstSearchIncreasingSubsequence(index2: int, increasingCount: int):
        if indexIncreasingSubsequence[index2] == []:
            return
        
        longestIncreasingCount[0] = max(longestIncreasingCount[0], increasingCount + 1)
        increasingCount += 1
        for index3 in indexIncreasingSubsequence[index2]:
            depthFirstSearchIncreasingSubsequence(index3, increasingCount)
            
        increasingCount -= 1
        
    for index4 in range(len(nums) - 1):
        increasingCount = 1
        depthFirstSearchIncreasingSubsequence(index4, increasingCount)
                         
    return longestIncreasingCount[0]
    
def lengthOfLIS1(nums: list) -> int:
    #Problem #300 Longest Increasing Subsequence - Medium - Solution Concept by YouTube Channel Depti Talesra - Understanding the Solution
    
    increasingList = [nums[0]]
    maxCount = 1
    
    for number in nums[1:]:
        if increasingList[-1] < number:
            increasingList.append(number)
            maxCount += 1
        else:
            leftPointer = 0
            rightPointer = len(increasingList) - 1
            
            while leftPointer < rightPointer:
                midPointer = (leftPointer + rightPointer)//2
                
                if increasingList[midPointer] < number:
                    leftPointer = midPointer + 1
                else:
                    rightPointer = midPointer
            
            increasingList[leftPointer] = number
        
    return maxCount 

def canPartition(nums: list[int]) -> bool:
    #Problem #416 Partition Equal Subset Sum - Medium - Solution Concept by YouTube Cahnnel NeetCode - Understanding the Solution
    
    if sum(nums) % 2:
        return False
    
    numberSet = set()
    numberSet.add(0)
    targetNumber = sum(nums) // 2
    
    for number in nums:
        otherSet = set()
        
        for total in numberSet:
            newSum = total + number
            
            if newSum == targetNumber:
                return True
            
            if newSum < targetNumber:
                otherSet.add(newSum)
        
        numberSet.update(otherSet)
            
    if targetNumber in numberSet:
        return True
    
    return False

def maxCoins(nums: list[int]) -> int:
    #Problem #312 Burst Balloons - Hard - Solution Concept by YouTube Channel NeetCode - Understanding the Solution
    
    nums = [1] + nums + [1]
    numberDictionary = {}
    
    def depthFirstSearchCoins(leftPointer, rightPointer):
        if leftPointer > rightPointer:
            return 0

        if (leftPointer, rightPointer) in numberDictionary:
            return numberDictionary[(leftPointer, rightPointer)]
        
        numberDictionary[(leftPointer, rightPointer)] = 0
        
        for index in range(leftPointer, rightPointer + 1):
            totalCoins = nums[leftPointer - 1] * nums[index] * nums[rightPointer + 1]
            totalCoins += depthFirstSearchCoins(leftPointer, index - 1) + depthFirstSearchCoins(index + 1, rightPointer)
            numberDictionary[(leftPointer, rightPointer)] = max(numberDictionary[(leftPointer, rightPointer)], totalCoins)
        
        return numberDictionary[(leftPointer, rightPointer)]
        
    return depthFirstSearchCoins(1, len(nums) - 2)

def maxCoins1(nums: list[int]) -> int:
    #Problem #312 Burst Balloons - Hard - Solution Concept by YouTube Channel Happy Coding - Understanding the Solution
    
    nums = [1] + nums + [1]
    numSize = len(nums)
    coinDictionary = [[0] * numSize for number in range(numSize)]
    
    for i in range(numSize - 2, 0, -1):
        for j in range(i, numSize - 1):
            for k in range(i, j+ 1):
                coinDictionary[i][j] = max(coinDictionary[i][j], nums[k]*nums[i-1] * nums[j+1] + coinDictionary[i][k - 1] + coinDictionary[k + 1][j])
    
    return coinDictionary[1][numSize - 2]

def longestCommonSubsequence(text1: str, text2: str) -> int:
    #Problem #1143 Longest Common Subsequence - Medium - Solution Concept by YouTube Channel Deepti Talesra - Understanding the Solution
    
    textMatrix: list[list[int]] = [[0 for square in range(len(text1) + 1)] for square in range(len(text2) + 1)]
    
    for index0 in range(1, len(textMatrix)):
        for index1 in range(1, len(textMatrix[index0])):
            if text2[index0 - 1] == text1[index1 - 1]:
                textMatrix[index0][index1] = textMatrix[index0 - 1][index1 - 1] + 1
            else:
                textMatrix[index0][index1] = max(textMatrix[index0 -1][index1], textMatrix[index0][index1 - 1])
                
    return textMatrix[len(textMatrix) - 1][len(textMatrix[0]) - 1]     

if __name__ == "__main__":
    nums = [7, 7, 7, 7, 7, 7, 7]
    print(lengthOfLIS(nums))