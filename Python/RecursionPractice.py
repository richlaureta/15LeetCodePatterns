import math

def recursiveAddition(count: int, endCount: int):
    if count == endCount:
        return
    
    print(count)	
    recursiveAddition(count + 1, endCount)

def recursiveLucasSequence(previousValue, sequence, howManySequence, arrayList: list[int], iterationCount = 0):
    if iterationCount == howManySequence:
        return
    
    if iterationCount == 0:
        arrayList.append(previousValue)
        sequence = 1
    else:
        arrayList.append(previousValue + sequence)
        previousValue = previousValue + sequence
    
    recursiveLucasSequence(previousValue + 1, sequence + 1, howManySequence, arrayList, iterationCount + 1)

def recursiveFibonacciSequence(index: int) -> int:
    sequenceList: list[int] = []
    
    def depthFirstSearchFibonacci(previousValue1: int, previousValue2: int, index: int, iterationCount: int = -1):        
        if iterationCount == index:
            return
        
        if iterationCount > 0:
            sequenceList.append(previousValue1 + previousValue2)
            temporaryValue = previousValue1
            previousValue1 = previousValue1 + previousValue2
            previousValue2 = temporaryValue
        else:
            if iterationCount == -1:
                sequenceList.append(0)
            else:
                sequenceList.append(1)
                previousValue1 = 1
                previousValue2 = 0
                  
        depthFirstSearchFibonacci(previousValue1, previousValue2, index, iterationCount + 1)
        
    depthFirstSearchFibonacci(None, None, index)
    
    return sequenceList[index]

def fibonacciFormula(n: int) -> int:
    return int(((math.pow(((1 + (math.pow(5, 0.5)))/2), n)) - (math.pow(((1-(math.pow(5, 0.5)))/2), n))) / (math.pow(5, 0.5)))

def fib(n: int) -> int:
    #Problem #509 Fibonacci Number - Easy 
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    return fib(n-1) + fib(n-2)

def fib1(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        firstNumber = 0
        secondNumber = 1
        currentNumber = 0
        for i in range(0, n-1):
            currentNumber = firstNumber + secondNumber
            firstNumber = secondNumber
            secondNumber = currentNumber
        return currentNumber

def recurse0(n: int) -> int:
    if n == 1:
        return 3
    
    return recurse0(n - 1) + 2

def recurse1(n: int) -> int:
    if n == 1:
        return 3
    
    return recurse1(n - 1) * 2

def recurse2(n: int) -> int:
    if n == 1:
        return 1
    
    return (1/2) * recurse2(n - 1) 

if __name__ == "__main__":
    n = 5
    
    print(recurse2(n))