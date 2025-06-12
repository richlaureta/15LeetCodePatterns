//
//  Heap.cpp
//  LeetCodeProblems
//
//  Created by Richmond Laureta on 6/12/25.
//

#include "Header.h"

#include <iostream>
#include <vector>

using namespace std;


int MaxHeap::parent(int index)
{
    return (index - 1) / 2;
}

int MaxHeap::leftChildIndex(int index)
{
    return (2 * index) + 1;
}

int MaxHeap::rightChildIndex(int index)
{
    return (index * 2) +  2;
}

void MaxHeap:: insert(int value)
{
    if(Heap.size() == 0)
    {
        Heap.push_back(value);
        return;
    }
    
    Heap.push_back(value);
    int insertedNumberIndex = ((int)Heap.size()) - 1;
    
    while(true)
    {
        if((Heap[insertedNumberIndex] > Heap[parent(insertedNumberIndex)]) && insertedNumberIndex != 0)
        {
            swap(&Heap[insertedNumberIndex], &Heap[parent(insertedNumberIndex)]);
            insertedNumberIndex = parent(insertedNumberIndex);
        }
        else
        {
            return;
        }
    }
}

void MaxHeap::swap(int *index1, int *index2)
{
    int temp = *index1;
    *index1 = *index2;
    *index2 = temp;
}

void MaxHeap::printHeap()
{
    for(int i = 0; i < Heap.size(); ++i)
    {
        cout << Heap[i] << endl;
    }
}
