//
//  main.cpp
//  C++
//
//  Created by Richmond Laureta on 6/4/25.
//


#include "Header.h"

#include <iostream>
#include <string>

using namespace std;

int main(int argc, const char * argv[]) {
    string s = "anagram";
    string t = "nagaram";
    
    cout << "The strings " << s << " and " << t << " are ";
    
    if(isAnagram(s, t) == 1)
    {
        cout << "Anagrams!" << endl;
    }
    else
    {
        cout << "not Anagrams!" << endl;
    }
    
    vector<int> arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int k = 4;
    
    cout << findMaxAverage(arr, k) << endl;
    
    return EXIT_SUCCESS;
}
