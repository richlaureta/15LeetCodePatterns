//
//  Anagram.cpp
//  C++
//
//  Created by Richmond Laureta on 6/4/25.
//

#include "Header.h"

bool isAnagram(string s, string t)
{
    //Problem #242 Valid Anagram: Easy 
    
    if(s.length() != t.length())
    {
        return false;
    }
    
    unordered_map<char, int> occurencesS;
    unordered_map<char, int> occurencesT;

    for (int i = 0; i < s.length(); ++i)
    {
        occurencesS[s[i]] += 1;
        occurencesT[t[i]] += 1;
    }
    
    if(occurencesS == occurencesT)
    {
        return true;
    }
    
    return false;
}

