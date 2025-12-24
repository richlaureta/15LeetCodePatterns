//
//  SlidingWindows.cpp
//  C++
//
//  Created by Richmond Laureta on 6/4/25.
//

#include "Header.h"

double findMaxAverage(vector<int> &nums, int k)
{
    //Problem #643 Maximum Average Subarray I
    
    double maxAverage = INT_MIN;
    double sumAdd = 0;
    
    for(int i = 0; i < k; i++)
    {
        sumAdd += nums[i];
    }
    
    int startPointer = 0;
    
    maxAverage = max(maxAverage, sumAdd/k);
    
    for(int i = k; i < nums.size(); i++)
    {
        sumAdd -= nums[startPointer];
        sumAdd += nums[i];
        
        maxAverage = max(maxAverage, sumAdd/k);
        
        startPointer++;
    }
    
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
    //Problem #3 Longest Substring Without Repeating Character
    
    unordered_map<int, int> myMap;
    int count = 0;
    int maxCount = 0;
    int pointer = 0;
    
    while(pointer != s.size())
    {
        if(myMap.count(s[pointer]) == 0)
        {
            myMap[s[pointer]] = pointer;
            count++;
            if(count > maxCount)
            {
                maxCount = count;
            }
        }
        else
        {
            count = 0;
            pointer = myMap[s[pointer]];
            myMap.clear();
        }
        
        pointer++;
    }
    
    return maxCount;
}

string minWindow(string s, string t)
{
    //Problem #76. Minimum Window Substring
    
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
