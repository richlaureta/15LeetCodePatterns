#include <iostream>
#include <string>
#include <algorithm>
#include <unordered_map>

using namespace std;

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
    }

    for (int i = 0; i < t.length(); ++i)
    {
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

int main()
{
    string s = "anagran";
    string t = "nagaram";

    cout << isAnagram(s, t) << endl;

    return EXIT_SUCCESS;
}