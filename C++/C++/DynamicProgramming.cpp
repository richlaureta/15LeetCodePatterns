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
