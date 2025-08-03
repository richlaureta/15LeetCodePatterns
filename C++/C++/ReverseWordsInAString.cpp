//
//  ReverseWordsInAString.cpp
//  C++
//
//  Created by Richmond Laureta on 8/3/25.
//

#include "Header.h"

string reverseWords(string s)
{
    stack<char> myStack;
    string reversedWords = "";
    char letter;
    
    for(int i = (int)s.size() - 1; i > -1; --i)
    {
        if(s[i] != ' ')
        {
            myStack.push(s[i]);
        }
        else
        {
            if(!myStack.empty())
            {
                while(!myStack.empty())
                {
                    letter = myStack.top();
                    myStack.pop();
                    reversedWords += letter;
                }
                reversedWords += ' ';
            }
        }
    }
    
    if(!myStack.empty())
    {
        while(!myStack.empty())
        {
            letter = myStack.top();
            myStack.pop();
            reversedWords += letter;
        }
    }
    
    for(int i = (int)reversedWords.size() - 1; i > - 1; i--)
    {
        if (reversedWords[i] == ' ')
        {
            reversedWords.erase(i);
        }
        else
        {
            break;
        }
    }
    
    return reversedWords;
}
