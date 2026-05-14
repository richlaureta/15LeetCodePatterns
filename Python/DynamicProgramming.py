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
    #Problem #300 Longest Increasing Subsequence - Medium - Solution Concept by YouTube Channel NeetCode - Understanding the Solution
    
    longestIncreaseIndex = [1] * len(nums)
    
    for index in range(len(nums) - 2, -1 , -1):
        for index1 in range(index + 1, len(nums)):
            if nums[index] < nums[index1]:
                longestIncreaseIndex[index] = max(longestIncreaseIndex[index], 1 + longestIncreaseIndex[index1])
    
    return max(longestIncreaseIndex)

def canPartition(nums: list[int]) -> bool:
    #Problem #416 Partition Equal Subset Sum - Medium - Solution Concept by YouTube Channel NeetCode - Understanding the Solution
    
    totalSum = sum(nums)
    
    if totalSum % 2:
        return False
    
    target = totalSum //2
    sumSet = set({0})
    
    for number in nums:
        temporarySumSet = set()
        for number1 in sumSet:
            if (number + number1) == target:
                return True
            temporarySumSet.add(number + number1)
            temporarySumSet.add(number)
        for number2 in temporarySumSet:
            sumSet.add(number2)
    
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
    #Problem #1143 Longest Common Subsequence - Medium - Solution Concept by YouTube Channel NeetCode - Understanding the Solution
    
    LCSMatrix = [[0 for index1 in range(len(text2) + 1)] for index in range(len(text1) + 1)]
    
    for index3 in range(len(text1) - 1, -1, -1):
        for index4 in range(len(text2) - 1, -1, -1):
            if text1[index3] == text2[index4]:
                LCSMatrix[index3][index4] = 1 + LCSMatrix[index3 + 1][index4 + 1]
            else:
                LCSMatrix[index3][index4] = max(LCSMatrix[index3][index4 + 1], LCSMatrix[index3 + 1][index4])
if __name__ == "__main__":
    text1 = "abcde"
    text2 = "ace"
    
    print(longestCommonSubsequence(text1, text2))