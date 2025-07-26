//
//  Anagram.cpp
//  C++
//
//  Created by Richmond Laureta on 6/4/25.
//

#include "Header.h"
#include <iostream>
#include <string>
#include <algorithm>
#include <unordered_map>

bool isAnagram(string s, string t)
{
    if (s.length() != t.length())
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

    for (int i = 0; i < t.length(); ++i)
    {
        if (occurencesS[s[i]] != occurencesT[s[i]])
        {
            return false;
        }
    }

    return true;
}

