def fib(n: int) -> int:
    #Problem #509 Fibonacci Number

    #My intuitive solution
    # if n == 0:
    #     return 0
    
    # if n == 1:
    #     return 1

    # firstNumber = 0
    # secondNumber = 1

    # for i in range(0, n-1):
    #     sum = firstNumber + secondNumber
    #     firstNumber = secondNumber
    #     secondNumber = sum

    # return sum

    #Recursive solution
    # if n == 0:
    #     return 0
    
    # if n == 1:
    #     return 1
    
    # return fib(n-2) + fib(n-1)

    #Top-Down Approach Dynamic Programming
    # myDictionary = {0:0, 1:1}

    # def f(x):
    #     if x in myDictionary:
    #         return myDictionary[x]
    #     else:
    #         myDictionary[x] = f(x-2) + f(x-1)
    #         return myDictionary[x]
    #     return f(n)
    
    #Bottom up Approach - Tabulation
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    array = [0] * (n + 1)

    array[0] = 0
    array[1] = 1
    for i in range(2, len(array)):
        array[i] = array[i-2] + array[i-1]

    
    return array[n]


if __name__ == "__main__":
    print(fib(8))