def recursiveAddition(count: int, endCount: int):
    if count == endCount:
        return
    
    print(count)	
    recursiveAddition(count + 1, endCount)

def recursiveLucasSequence(previousValue, sequence, upToIndex, iterationCount = 0):
    if iterationCount == upToIndex:
        return
    
    if iterationCount == 0:
        print(previousValue)
        sequence = 1
    else:
        print(previousValue + sequence)
        previousValue = previousValue + sequence
    
    recursiveLucasSequence(previousValue + 1, sequence + 1, upToIndex, iterationCount + 1)

if __name__ == "__main__":

    howManySequence = 5
    
    recursiveLucasSequence(2, 0, howManySequence)