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
    #Problem #1143 Longest Common Subsequence - Medium
    
    longerText = ""
    shorterText = ""
    
    if len(text1) > len(text2):
        longerText = text1
        shorterText = text2
    else:
        longerText = text2
        shorterText = text1
        
    letterIndexes = defaultdict(list[int])
    
    for index in range(len(longerText)):
        letterIndexes[longerText[index]].append(index)
    
    def depthFirstSearchLCS():
        if shorterTextIndex[0] < len(shorterText) and letterIndexes[shorterText[shorterTextIndex[0]]] == []:
            shorterTextIndex[0] += 1
            depthFirstSearchLCS()
            
        if shorterTextIndex[0] == len(shorterText):
            return
        
        for index1 in letterIndexes[shorterText[shorterTextIndex[0]]]:
            if previousIndex[0] < index1:
                previousIndex[0] = index1
            else:
                continue
            
            shorterTextIndex[0] += 1
            LCSCount[0] += 1
            LCSMax[0] = max(LCSMax[0], LCSCount[0])
            
            depthFirstSearchLCS()
            
            shorterTextIndex[0] -= 1
            LCSCount[0] -= 1
            
    previousIndex = [-1]
    shorterTextIndex = [0]
    LCSCount = [0]
    LCSMax = [0]
    
    for index in range(len(shorterText)):
        if letterIndexes[shorterText[index]] == []:
            continue
        
        LCSCount[0] = 0
        previousIndex[0] = -1
        
        shorterTextIndex[0] = index
        
        depthFirstSearchLCS()
        
        if LCSMax[0] == len(shorterText):
            return LCSMax[0]
    
    return LCSMax[0]

if __name__ == "__main__":
    text1 = "pmjghexybyrgzczy"
    text2 = "hafcdqbgncrcbihkd"
    
    print(longestCommonSubsequence(text1, text2))