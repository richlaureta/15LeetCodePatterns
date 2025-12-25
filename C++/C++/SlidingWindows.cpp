//
//  SlidingWindows.cpp
//  C++
//
//  Created by Richmond Laureta on 6/4/25.
//

#include "Header.h"

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
    //Problem #76. Minimum Window Substring - Hard
    
    if((t == "") or (t.size() > s.size()))
    {
        return "";
    }
    
    unordered_map<char, int> tMap;
    unordered_map<char, int> haveMap;
    int have = 0;
    vector<int> rangeOfString;
    int minimumLength = 100001;
    int leftPointer = 0;
    
    for(int i = 0; i < t.size(); i++)
    {
        tMap[t[i]]++;
    }
    
    int need = (int) tMap.size();
    
    for(int rightPointer = 0; rightPointer < s.size(); rightPointer++)
    {
        haveMap[s[rightPointer]]++;
        
        if((tMap.count(s[rightPointer]) > 0) and haveMap[s[rightPointer]] == tMap[s[rightPointer]])
        {
            have++;
        }
        
        while(need == have)
        {
            if(((rightPointer - leftPointer) + 1) < minimumLength)
            {
                minimumLength = (rightPointer - leftPointer) + 1;
                rangeOfString = {leftPointer, rightPointer};
            }
            
            haveMap[s[leftPointer]]--;
            
            if((tMap.count(s[leftPointer]) > 0) and haveMap[s[leftPointer]] < tMap[s[leftPointer]])
            {
                have--;
            }
            
            leftPointer++;
        }
    }
    
    if(minimumLength != 100001)
    {
        string answer;
        for(int i = rangeOfString[0]; i < rangeOfString[1] + 1; i++)
        {
            answer += s[i];
        }
        return answer;
    }
    
    return "";
}
