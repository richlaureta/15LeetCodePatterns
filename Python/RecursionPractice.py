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

if __name__ == "__main__":

    howManySequence = 10
    array = []
    recursiveLucasSequence(2, 0, howManySequence, array)
    
    print(array)