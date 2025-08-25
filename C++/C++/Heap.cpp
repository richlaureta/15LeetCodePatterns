//
//  Heap.cpp
//  LeetCodeProblems
//
//  Created by Richmond Laureta on 6/12/25.
//

#include "Header.h"

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
    Heap.push_back(value);
    int insertedNumberIndex = ((int)Heap.size()) - 1;
    
    while((Heap[insertedNumberIndex] > Heap[parent(insertedNumberIndex)]) && insertedNumberIndex != 0)
    {
        swap(&Heap[insertedNumberIndex], &Heap[parent(insertedNumberIndex)]);
        insertedNumberIndex = parent(insertedNumberIndex);
    }
}

int MaxHeap::remove()
{
    if(Heap.size() == 0)
    {
        return INT_MIN;
    }
    
    if(Heap.size() == 1)
    {
        int front = Heap.front();
        Heap.pop_back();
        return front;
    }
    
    int currentIndex = ((int)Heap.size()) - 1;
    int poppedValue = Heap[0];
    Heap[0] = Heap[currentIndex];
    
    Heap.pop_back();
    
    sinkDown(0);
    
    return poppedValue;
}

void MaxHeap::swap(int *index1, int *index2)
{
    int temp = *index1;
    *index1 = *index2;
    *index2 = temp;
}

void MaxHeap::sinkDown(int index)
{
    int maxIndex = index;
    
    while(true)
    {
        int leftIndex = leftChildIndex(index);
        int rightIndex = rightChildIndex(index);
        
        if(leftIndex < Heap.size() && Heap[leftIndex] > Heap[maxIndex])
        {
            maxIndex = leftIndex;
        }
        
        if(rightIndex < Heap.size() && Heap[rightIndex] > Heap[maxIndex])
        {
            maxIndex = rightIndex;
        }
        
        if(maxIndex != index)
        {
            swap(&Heap[index], &Heap[maxIndex]);
            index = maxIndex;
        }
        else
        {
            return;
        }
    }
}

void MaxHeap::printHeap()
{
    for(int i = 0; i < Heap.size(); ++i)
    {
        cout << Heap[i] << " ";
    }
    cout << endl;
}

size_t MaxHeap::getSize()
{
    return Heap.size();
}
