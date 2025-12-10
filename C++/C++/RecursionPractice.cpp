//
//  RecursionPractice.cpp
//  C++
//
//  Created by Richmond Laureta on 11/26/25.
//

#include "Header.h"

int fib1(int n)
{
    //Problem #507 Fibonacci Number - Easy
    
    if(n == 0) return 0;
    else if (n == 1) return 1;
    
    return fib(n - 1) + fib(n - 2);
}

int fibonacciFormula(int n)
{
    //Problem #507 Fibonacci Number - Easy
    
    return round((pow(((1 + (pow(5, 0.5)))/2), n) - pow(((1 - (pow(5, 0.5)))/2), n))/(pow(5, 0.5)));
}

int recursion0(int n)
{
    if(n == 1) return 3;
    
    return recursion0(n - 1) + 2;
}

int recursion1(int n)
{
    if(n == 1) return 3;
    
    return recursion1(n - 1) * 2;
}
