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

def recursiveFibonacciSequence(howManySequence: int) -> list[int]:
    sequenceList: list[int] = []
    
    def depthFirstSearchFibonacci(previousValue1: int, previousValue2: int, howManySequence: int, iterationCount: int = 0):        
        if iterationCount == howManySequence:
            return
        
        if iterationCount > 1:
            sequenceList.append(previousValue1 + previousValue2)
            temporaryValue = previousValue1
            previousValue1 = previousValue1 + previousValue2
            previousValue2 = temporaryValue
        else:
            if iterationCount == 0:
                sequenceList.append(0)
            else:
                sequenceList.append(1)
                previousValue1 = 1
                previousValue2 = 0
                  
        depthFirstSearchFibonacci(previousValue1, previousValue2, howManySequence, iterationCount + 1)
        
    depthFirstSearchFibonacci(None, None, howManySequence)
    
    return sequenceList

if __name__ == "__main__":
    howManySequence: int = int(input("How many sequence of numbers do you want to see in the Fibonacci pattern(s)? "))
    
    print(recursiveFibonacciSequence(howManySequence))
    
    