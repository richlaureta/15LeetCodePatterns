import re
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
    partialList: list[int] = []
    solutionList: list[list[int]] = []
    
    def depthFirstSearchSubsets(index):
        if index == len(nums):
            solutionList.append(partialList.copy())
            return
        
        depthFirstSearchSubsets(index + 1)
        
        partialList.append(nums[index])
        
        depthFirstSearchSubsets(index + 1)
        
        partialList.pop()
        
    depthFirstSearchSubsets(0)
    
    return solutionList

def isPalindrome(s: str) -> bool:
    #Problem #125 Valid Palindrome - Easy
    
    newString = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    
    leftPointer = 0
    rightPointer = len(newString) - 1
        
    while leftPointer < rightPointer:
        if newString[leftPointer] != newString[rightPointer]:
            return False
        leftPointer += 1
        rightPointer -= 1
        
        return True
if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))
    