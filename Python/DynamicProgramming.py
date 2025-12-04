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
    #Problem #70 Climbing Stairs - Easy - Solution Concept by Greg Hogg - Understanding the Solution
    
    waysDictionary = {1: 1, 2: 2}
    
    def function(number: int) -> int:
        if number in waysDictionary:
           return waysDictionary[number]
        else:
            waysDictionary[number] = function(number - 2) + function(number - 1)
            return waysDictionary[number]
        
    return function(n)

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
    #Problem #322 Coin Exchange - Medium - Solution Concept by YouTube Channel Greg Hogg - Understanding the Solution
    #Top Down Dynamic Programming (Memoization)
    
    coinsDictionary = {0: 0}
    coins.sort()
    
    def minimumCoins(numberAmount: int):
        if numberAmount in coinsDictionary:
            return coinsDictionary[numberAmount]
        
        minimum = float('inf')
        for coin in coins:
            difference = numberAmount - coin
            if difference < 0:
                break
            
            minimum = min(minimum, 1 + minimumCoins(difference))

        coinsDictionary[numberAmount] = minimum
        return minimum
        
    coinCount = minimumCoins(amount)
    
    if coinCount < float('inf'):
        return coinCount
    
    return -1
 
def coinChange1(coins: list[int], amount: int) -> int:
    #Problem #322 Coin Exchange - Medium - Solution Concept by YouTube Channel Greg Hogg - Understanding the Solution
    #Bottom Up Dynamic Programming (Memoization)
    
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
    #Problem #300 Longest Increasing Subsequence - Medium
    
    greaterList: list[list[int]] = []
    for i in range(0, len(nums)):
        greaterList.append([]) 
    
    for index0 in range(0, len(nums)):
        for index1 in range(index0 + 1, len(nums)):
            if nums[index0] < nums[index1]:
                greaterList[index0].append(index1)
   
    maxCount = 0
    
    for i in range(0, len(greaterList)):
        for j in range(0, len(greaterList[i])):
            count = 1
            while True:
                k = i
                l = j
                if greaterList[greaterList[k][l]] == []:
                    break
                count += 1
            if count > maxCount:
                maxCount = count
    return maxCount
            
if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    
    print(lengthOfLIS(nums))