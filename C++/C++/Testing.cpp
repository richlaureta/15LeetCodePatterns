//
//  Testing.cpp
//  C++
//
//  Created by Richmond Laureta on 12/8/25.
//
#include "Header.h"

bool isPalindrome(string s)
{
    //Problem #125 Valid Palindrome - Easy
    
    int leftPointer = 0;
    int rightPointer = (int) s.size() - 1;
    
    while(leftPointer < rightPointer)
    {
        if(!isalnum(s[leftPointer]))
        {
            leftPointer++;
            continue;
        }
        
        if(!isalnum(s[rightPointer]))
        {
            rightPointer--;
            continue;
        }
        
        if(tolower(s[leftPointer]) != tolower(s[rightPointer]))
        {
            return false;
        }
        
        leftPointer++;
        rightPointer--;
    }
    
    return true;
}
