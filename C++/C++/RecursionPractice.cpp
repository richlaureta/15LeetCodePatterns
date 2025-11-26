//
//  RecursionPractice.cpp
//  C++
//
//  Created by Richmond Laureta on 11/26/25.
//

#include "Header.h"

int fib(int n)
{
    //Problem #507 Fibonacci Number - Easy
    
    if(n == 0) return 0;
    else if (n == 1) return 1;
    
    return fib(n - 1) + fib(n - 2);
}
