//
//  SlidingWindows.cpp
//  C++
//
//  Created by Richmond Laureta on 6/4/25.
//

#include "Header.h"

int countKConstraintSubstrings(string s, int k)
{
    //Problem #3258 Count Substrings That Satisfy K-Constraint I - Easy
    vector<int> zeroesAndOnes = {0,0};
    int leftPointer = 0;
    
    int countKConstraints = 0;
    
    for(int rightPointer = 0; rightPointer < (int)s.size(); rightPointer++)
    {
        zeroesAndOnes[(int)s[rightPointer] - 48 ] += 1;
        
        while(min(zeroesAndOnes[0], zeroesAndOnes[1]) > k)
        {
            zeroesAndOnes[(int)s[leftPointer] - 48] -= 1;
            leftPointer++;
        }
        
        countKConstraints += rightPointer - leftPointer + 1;
    }
    
    return countKConstraints;
}

vector<int> decrypt(vector<int> &code, int k)
{
    //Problem #1652 Defuse the Bomb - Easy
    
    vector<int> bombCodeVector;
    
    int sum = 0;
    int count = 0;
    int index = 0;
    
    if(k > 0) index = 1;
    else index = (int)code.size() - 1;
    
    while(count != abs(k))
    {
        if(index == (int)code.size() and k > 0) index = 0;
        else if(index == -1 and k < 0) index = (int) code.size() - 1;
        
        sum += code[index];
        
        if(k > 0) index += 1;
        else index -= 1;
        
        count++;
    }
    
    bombCodeVector.push_back(sum);
    
    int previousIndex = 1;
    if(k < 0) previousIndex = (int)code.size() - abs(k);
    
    int endIndex = previousIndex + abs(k);
    if(k < 0) endIndex = previousIndex + abs(k);
    
    for(int i = 0; i < (int)code.size() - 1; i++)
    {
        if(endIndex == (int)code.size()) endIndex = 0;
        
        if(previousIndex == (int)code.size()) previousIndex = 0;
        
        sum -= code[previousIndex];
        previousIndex++;
        sum += code[endIndex];
        endIndex++;
        
        bombCodeVector.push_back(sum);
    }
    
    return bombCodeVector;
}

int countGoodSubstrings(string s)
{
    //Problem #1876 Substrings of Size Three with Distinct Characters - Easy
    
    int goodCount = 0;
    int index = 0;
    
    while(index + 2 < s.size())
    {
        if(s[index] != s[index + 1] and
           s[index] != s[index + 2] and
           s[index + 1] != s[index + 2])
            goodCount++;
        
        index++;
    }
    
    return goodCount;
}

double findMaxAverage(vector<int> &nums, int k)
{
    //Problem #643 Maximum Average Subarray I - Easy
    
    //Create a variable maxAverage equal to the lowest possible integer. O(1) space complexity.
    double maxAverage = INT_MIN;
    //Create a variable to sum all the contiguous lengths of k. O(1) space complexity.
    double sumAdd = 0;
    
    //Iterate through the length of k and add them. O(k) time complexity.
    for(int i = 0; i < k; i++)
    {
        sumAdd += nums[i];
    }
    
    //Create a variable for the startPointer index equal to 0. O(1) space complexity.
    int startPointer = 0;
    //Take the maximum average between the current maximum average and the new one.
    maxAverage = max(maxAverage, sumAdd/k);
    
    //Iterate through the nums. O(n - k) time complexity.
    for(int i = k; i < nums.size(); i++)
    {
        //Subtract the nums[startPointer] from sumAdd.
        sumAdd -= nums[startPointer];
        //Add the current nums[index] to sumAdd.
        sumAdd += nums[i];
        //Take the maximum average between the current maximum average and the new one.
        maxAverage = max(maxAverage, sumAdd/k);
        //Increment the startPointer by 1.
        startPointer++;
    }
    
    //Return maxAverage.
    return maxAverage;
}

int maxVowels(string s, int k)
{
    //#Problem # 1456. Maximum Number of Vowels in a Substring of Given Length
    
    int count = 0;
    
    for(int i = 0; i < k; i++)
    {
        if(s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u')
        {
            count++;
        }
    }
    
    if(count == k)
    {
        return k;
    }
    
    int left = 0;
    int maxCount = count;
    
    for(int i = k; i < s.size(); i++)
    {
        if(s[left] == 'a' || s[left] == 'e' || s[left] == 'i' || s[left] == 'o' || s[left] == 'u')
        {
            count--;
        }
        
        if(s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u')
        {
            count++;
        }
        
        if(count == k){return k;}
        
        left++;
        if(count > maxCount)
        {
            maxCount = count;
        }
        
    }
    return maxCount;
}

int lengthOfLongestSubstring(string s)
{
    //Problem #3 Longest Substring Without Repeating Characters - Medium
    
    //Create an unordered map to store the key letter to value index. O(n) space complexity.
    unordered_map<char, int> letterIndexMap;
    //Create a startingPoint variable. O(1) space complexity.
    int startingPoint = 0;
    
    //Create a uniqueCount variable. O(1) space complexity.
    int uniqueCount = 0;
    //Create a longestSubstringCount variable. O(1) space complexity.
    int longestSubstringCount = 0;
    
    //Iterate through the string s. O(n) time complexity.
    for(int i = 0; i < s.size(); i++)
    {
        //If the character in s[index] is not in the map.
        if(letterIndexMap.find(s[i]) == letterIndexMap.end())
        {
            letterIndexMap[s[i]] = i;
            uniqueCount++;
        }
        //Else if the s[index] is not in the dictionary.
        else
        {
            //Get the maximum between longestSubstringCount and uniqueCount.
            longestSubstringCount = max(longestSubstringCount, uniqueCount);
            
            //Get the previous starting point.
            int previousStartingPoint = startingPoint;
            //Make the startingPoint equal to the letterIndexDictionary[s[index]] + 1.
            startingPoint = letterIndexMap[s[i]] + 1;
            //Set uniqueCount equal to the index minus the new starting point + 1.
            uniqueCount = i - startingPoint + 1;
            
            //Iterate from the previous StartingPoint to the letterIndexDictionary[s[index]] + 1.
            //O(n) * O(log n) time complexity.
            for(int j = previousStartingPoint; j < letterIndexMap[s[i]] + 1; j++)
            {
                //Erase the previous character that got repeated.
                letterIndexMap.erase(s[j]);
            }
            
            //Create a new character that has the new index.
            letterIndexMap[s[i]] = i;
        }
    }
    
    //Get the maximum between longestSubstringCount and uniqueCount.
    longestSubstringCount = max(longestSubstringCount, uniqueCount);
    
    //Return the longestSubstringCount.
    return longestSubstringCount;
}

string minWindow(string s, string t)
{
    //Problem #76. Minimum Window Substring - Hard - Solution Concept by YouTube Channel Deepti Talesra - Understanding the Solution
    
    //Initialize an unordered_map variable and call it tMap.
    unordered_map<char, int> tMap;
    
    //Count the frequency of letters in string t.
    for(char character: t) tMap[character] += 1;
    
    //Initialize a leftMostPointer variable to 0.
    int leftMostPointer = 0;
    //Initialize a rightMostPointer variable to 0.
    int rightMostPointer = 0;
    
    //Initialize a variable formed to 0. This is the count to satisfy the frequency in tMap so we can find the minimum length.
    int formed = 0;
    //Initialize a variable total to the length of tMap.
    int total = (int)tMap.size();
    
    //Initialize minimumWindowLengthSubstring to the most max according to the constraint.
    int minimumWindowLengthSubstring = 100001;
    //Initialize a leftIndex to 0 that will mark the index of the minimum length.
    int leftIndex = 0;
    //Initialize a rightIndex to 0 that will mark the index of the minimum length.
    int rightIndex = 0;
    
    //Initialize a while loop whilst rightMostPointer is less than the length of s.
    while(rightMostPointer < s.size())
    {
        //If tMap contains the character at s[rightMostPointer], then decrement the tMap key by 1.
        if(tMap.contains(s[rightMostPointer]))
        {
            tMap[s[rightMostPointer]] -= 1;
            //If we satisfy the frequency and it is 0, we increment variable formed by 1.
            if(tMap[s[rightMostPointer]] == 0) formed += 1;
        }
        
        //Initialize another while loop if formed equals total and leftMostPointer is less than or equal to rightMostPointer
        while(formed == total and leftMostPointer <= rightMostPointer)
        {
            //If rightMostPointer minus leftMostPointer + 1 is less than minimumWindowLengthSubstring then update
            //the length of the minimumWindowLengthSubstring and leftIndex and rightIndex.
            if(rightMostPointer - leftMostPointer + 1 < minimumWindowLengthSubstring)
            {
                minimumWindowLengthSubstring = rightMostPointer - leftMostPointer + 1;
                leftIndex = leftMostPointer;
                rightIndex = rightMostPointer;
            }
            
            //If tMap contains s leftMostPointer character index, then increment the key by 1.
            if(tMap.contains(s[leftMostPointer]))
            {
                tMap[s[leftMostPointer]] += 1;
                
                //If it equals 1, then decrement the variable formed by 1.
                if(tMap[s[leftMostPointer]] == 1)
                {
                    formed -= 1;
                }
            }
            
            //Decrement leftMostPointer by 1.
            leftMostPointer++;
        }
        
        //Increment rightMostPointer by 1.
        rightMostPointer++;
    }
    
    //Return an empty no-space string if it is 100001, otherwise return the leftIndex and rightIndex length of s.
    if (minimumWindowLengthSubstring == 100001) return "";
    
    string minimumWindow = "";
    
    for(int i = leftIndex; i < rightIndex + 1; i++)
    {
        minimumWindow += s[i];
    }
        
    return minimumWindow;
}
