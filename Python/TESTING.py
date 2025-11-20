def forLoop(count, endCount, word) -> int:
    if count == endCount:
        return
    
    print(word[count])
       
    count += 1
    
    forLoop(count, endCount, word)

def permutaions(nums: list[int]) -> list[list[int]]:
    partialList: list[int] = []
    solutionList: list[list[int]] = []
    
    def depthFirstSearchPermutaions():
        if len(partialList) == len(nums):
            solutionList.append(partialList.copy())
            return
        
        for numbers in nums:
            if numbers not in partialList:
                partialList.append(numbers)
                depthFirstSearchPermutaions()
                partialList.pop()
                  
    depthFirstSearchPermutaions()
    
    return solutionList

def subsets(nums: list[int]) -> list[list[int]]:
    
if __name__ == "__main__":
    nums = [1, 2, 3]
    
    print(permutaions(nums))
    
