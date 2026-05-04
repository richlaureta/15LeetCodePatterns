//
//  Miscellaneous.c
//  C++
//
//  Created by Richmond Laureta on 5/4/26.
//

#include "Header.h"

bool isValidSudoku(vector<vector<char>> &board)
{
    unordered_set<char> topLeftSet = {};
    unordered_set<char> topMiddleSet = {};
    unordered_set<char> topRightSet = {};

    unordered_set<char> middleLeftSet = {};
    unordered_set<char> middleMiddleSet = {};
    unordered_set<char> middleRightSet = {};

    unordered_set<char> bottomLeftSet = {};
    unordered_set<char> bottomMiddleSet = {};
    unordered_set<char> bottomRightSet = {};

    unordered_set<char> column0Set = {};
    unordered_set<char> column1Set = {};
    unordered_set<char> column2Set = {};
    unordered_set<char> column3Set = {};
    unordered_set<char> column4Set = {};
    unordered_set<char> column5Set = {};
    unordered_set<char> column6Set = {};
    unordered_set<char> column7Set = {};
    unordered_set<char> column8Set = {};
    
    for(int index = 0; index < 9; index++)
    {
        unordered_set<char> numberSeenRow = {};
        for(int index1 = 0; index1 < 9; index1++)
        {
            if(board[index][index1] == '.') continue;
                        
            if (numberSeenRow.find(board[index][index1]) !=  numberSeenRow.end()) return false;
            else numberSeenRow.insert(board[index][index1]);

            switch(index1)
            {
                case 0:
                    if (column0Set.find(board[index][index1]) != column0Set.end()) return false;
                    column0Set.insert(board[index][index1]);
                    break;
                case 1:
                    if (column1Set.find(board[index][index1]) != column1Set.end()) return false;
                    column1Set.insert(board[index][index1]);
                    break;
                case 2:
                    if (column2Set.find(board[index][index1]) != column2Set.end()) return false;
                    column2Set.insert(board[index][index1]);
                    break;
                case 3:
                    if (column3Set.find(board[index][index1]) != column3Set.end()) return false;
                    column3Set.insert(board[index][index1]);
                    break;
                case 4:
                    if (column4Set.find(board[index][index1]) != column4Set.end()) return false;
                    column4Set.insert(board[index][index1]);
                    break;
                case 5:
                    if (column5Set.find(board[index][index1]) != column5Set.end()) return false;
                    column5Set.insert(board[index][index1]);
                    break;
                case 6:
                    if (column6Set.find(board[index][index1]) != column6Set.end()) return false;
                    column6Set.insert(board[index][index1]);
                    break;
                case 7:
                    if (column7Set.find(board[index][index1]) != column7Set.end()) return false;
                    column7Set.insert(board[index][index1]);
                    break;
                case 8:
                    if (column8Set.find(board[index][index1]) != column8Set.end()) return false;
                    column8Set.insert(board[index][index1]);
            }


            if (index < 3 and index1 < 3)
            {
                if (topLeftSet.find(board[index][index1]) != topLeftSet.end()) return false;
                topLeftSet.insert(board[index][index1]);
            }
            else if(index < 3 and index1 > 2 and index1 < 6)
            {
                if (topMiddleSet.find(board[index][index1]) != topMiddleSet.end()) return false;
                topMiddleSet.insert(board[index][index1]);
            }
            else if (index < 3 and index1 > 5)
            {
                if (topRightSet.find(board[index][index1]) != topRightSet.end()) return false;
                topRightSet.insert(board[index][index1]);
            }
            else if (index > 2 and index < 6 and index1 < 3 and index1 < 3)
            {
                if (middleLeftSet.find(board[index][index1]) != middleLeftSet.end()) return false;
                middleLeftSet.insert(board[index][index1]);
            }
            else if (index > 2 and index < 6 and index1 > 2 and index1 < 6)
            {
                if (middleMiddleSet.find(board[index][index1]) != middleMiddleSet.end()) return false;
                middleMiddleSet.insert(board[index][index1]);
            }
            else if (index > 2 and index < 6 and index1 > 5)
            {
                if (middleRightSet.find(board[index][index1]) != middleRightSet.end()) return false;
                middleRightSet.insert(board[index][index1]);
            }
            else if (index > 5 and index1 < 3)
            {
                if (bottomLeftSet.find(board[index][index1]) != bottomLeftSet.end()) return false;
                bottomLeftSet.insert(board[index][index1]);
            }
            else if (index > 5 and index1 > 2 and index1 < 6)
            {
                if (bottomMiddleSet.find(board[index][index1]) != bottomMiddleSet.end()) return false;
                bottomMiddleSet.insert(board[index][index1]);
            }
            else if (index > 5 and index1 > 5)
            {
                if (bottomRightSet.find(board[index][index1]) != bottomRightSet.end()) return false;
                bottomRightSet.insert(board[index][index1]);
            }
        }
    }
    
    return true;
}
