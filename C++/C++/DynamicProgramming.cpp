//
//  DynamicProgramming.cpp
//  C++
//
//  Created by Richmond Laureta on 8/4/25.
//

#include "Header.h"

int fib(int n)
{
    //Problem #509 Fibonacci Number
    
    //My intuitive solution
    if (n == 0) return 0;
    
    if (n == 1) return 1;
    
    int sum = 0;
    int firstNumber = 0;
    int secondNumber = 1;
    
    for(int i = 0; i < n - 1; ++i)
    {
        sum = firstNumber + secondNumber;
        firstNumber = secondNumber;
        secondNumber = sum;
    }
    
    return sum;
}

int functionNumber(int number, unordered_map<int, int> &sequenceMap)
{
    //Problem #507 Fibonacci Number - Easy - Solution Concept by YouTube Channel Greg Hogg - Understanding the Solution
    
    if(sequenceMap.find(number) != sequenceMap.end())
    {
        return sequenceMap[number];
    }
    else
    {
        sequenceMap[number] = functionNumber(number - 1, sequenceMap) + functionNumber(number - 2, sequenceMap);
        return sequenceMap[number];
    }
}

int fib2(int n)
{
    //Problem #507 Fibonacci Number - Easy - Solution Concept by YouTube Channel Greg Hogg - Understanding the Solution
    
    unordered_map<int, int> sequenceMap;
    sequenceMap[0] = 0;
    sequenceMap[1] = 1;
    
    return functionNumber(n, sequenceMap);
}

int functionNumber1(int number, unordered_map<int, int> &waysMap)
{
    //Problem #70 Climb Stairs - Easy
    
    if(waysMap.find(number) != waysMap.end())
    {
        return waysMap[number];
    }
    else
    {
        waysMap[number] = functionNumber1(number - 2, waysMap) + functionNumber1(number - 1, waysMap);
        return waysMap[number];
    }
}

int climbStairs(int n)
{
    //Problem #70 Climb Stairs - Easy
    
    unordered_map<int, int> waysMap = {{1,1}, {2,2}};
    
    return functionNumber1(n, waysMap);
}

int climbStairs1(int n)
{
    //Problem #70 Climb Stairs - Easy
    
    if(n == 1) return 1;
    else if (n == 2) return 2;
        
    int nMinus2 = 1;
    int nMinus1 = 2;
    int current = 0;
    for(int i = 2; i < n; i++)
    {
        current = nMinus2 + nMinus1;
        nMinus2 = nMinus1;
        nMinus1 = current;
    }
    
    return current;
}

int minimumCoins(vector<int> &coins, unordered_map<int, int> &coinsMap, int numberAmount)
{
    //Problem #322 Coin Change - Medium - Solution Concept by YouTube Channel - Greg Hogg
        
    if(coinsMap.find(numberAmount) != coinsMap.end()) return coinsMap[numberAmount];
    
    int minimum = 10000;
    for(int i = 0; i < coins.size(); i++)
    {
        int difference = numberAmount - coins[i];
        
        if(difference < 0) break;
        
        minimum = min(minimum, 1 + minimumCoins(coins, coinsMap, difference));
    }
    
    coinsMap[numberAmount] = minimum;
    return minimum;
}

int coinChange(vector<int> &coins, int amount)
{
    //Problem #322 Coin Change - Medium - Solution Concept by YouTube Channel - Greg Hogg
    //Top Down Dynamic Programming Approach - Memoization
    
    unordered_map<int, int> coinsMap{{0, 0}};
    
    sort(coins.begin(), coins.end());
    
    int answer = minimumCoins(coins, coinsMap, amount);
    
    if(answer != 10000) return answer;
    
    return -1;
}

int coinChange1(vector<int> &coins, int amount)
{
    //Problem #322 Coin Change - Medium - Solution Concept by YouTube Channel - Greg Hogg
    //Bottom Up Dynamic Programming Approach - Memoization
    
    sort(coins.begin(), coins.end());
    vector<int> coinIndex(amount + 1);
    
    for(int i = 1; i < coinIndex.size(); i++)
    {
        int minimum = 100000;
        
        for(int j = 0; j < coins.size(); j++)
        {
            int difference = i - coins[j];
            
            if(difference < 0)
            {
                break;
            }
            
            minimum = min(minimum , coinIndex[difference] + 1);
        }
        
        coinIndex[i] = minimum;
    }
    
    if(coinIndex[amount] != 100000)
    {
        return coinIndex[amount];
    }
    
    return -1;
}

int lengthOfLIS(vector<int> &nums)
{
    //Problem #300 Longest Increasing Subsequence - Medium - Solution Concept by YouTube Channel Deepti Talesra - Understanding the Solution
    
    vector<int> increasingList = {nums[0]};
    int maxCount = 1;
    
    for(int i = 1; i < nums.size(); i++)
    {
        if(nums[i] > increasingList.back())
        {
            increasingList.push_back(nums[i]);
            maxCount++;
        }
        else
        {
            for(int j = 0; j < increasingList.size(); j++)
            {
                if(increasingList[j] >= nums[i])
                {
                    increasingList[j] = nums[i];
                    break;
                }
            }
        }
    }
    
    return maxCount;
}

int lengthOfLIS1(vector<int> &nums)
{
    //Problem #300 Longest Increasing Subsequence - Medium - Solution Concept by YouTube Channel Deepti Talesra - Understanding the Solution
    
    vector<int> increasingList = {nums[0]};
    int maxCount = 1;
    
    for(int i = 1; i < nums.size(); i++)
    {
        if(nums[i] > increasingList.back())
        {
            increasingList.push_back(nums[i]);
            maxCount++;
        }
        else
        {
            int leftPointer = 0;
            int rightPointer = (int) increasingList.size() - 1;
            
            while(leftPointer < rightPointer)
            {
                int midPointer = floor((leftPointer + rightPointer)/2);
                
                if(increasingList[midPointer] < nums[i])
                {
                    leftPointer = midPointer + 1;
                }
                else
                {
                    rightPointer = midPointer;
                }
            }
            
            increasingList[leftPointer] = nums[i];
        }
    }
    
    return maxCount;
}
