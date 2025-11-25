def recursiveAddition(count: int, endCount: int):
    if count == endCount:
        return
    
    print(count)	
    recursiveAddition(count + 1, endCount)

def recursiveLucasSequence(nIndex):
    if nIndex == 0:
        return 2
    elif nIndex == 1:
        return 1
    return recursiveLucasSequence(nIndex - 1) + recursiveLucasSequence(nIndex - 2)

if __name__ == "__main__":
   nIndex = 5
   
   recursiveLucasSequence(nIndex)