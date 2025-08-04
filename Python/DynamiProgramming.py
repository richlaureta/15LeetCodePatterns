def fib(n: int) -> int:
    #Problem #509 Fibonacci Number

    #My intuitive solution
    if n == 0:
        return 0
    
    if n == 1:
        return 1

    firstNumber = 0
    secondNumber = 1

    for i in range(0, n-1):
        sum = firstNumber + secondNumber
        firstNumber = secondNumber
        secondNumber = sum

    return sum

if __name__ == "__main__":
    print(fib(9))