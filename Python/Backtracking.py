def subsets(nums: list[int]) -> list[list[int]]:
    #Problem #78 Subsets - Medium -  Solution Concept by YouTube Channel Greg Hogg - Understanding the Solution 

    answer: list[list[int]] = []
    partialSolution: list[int] = []
  
    def depthFirstSearchSubsets(index):
        if index == len(nums):
            answer.append(partialSolution.copy())
            return
        
        depthFirstSearchSubsets(index + 1)
        
        partialSolution.append(nums[index])
        
        depthFirstSearchSubsets(index + 1)
        
        partialSolution.pop()
                            
    depthFirstSearchSubsets(0)
        
    return answer
    

def permute(nums: list[int]) -> list[list[int]]:
    #Problem #46 Permutations - Medium - Solution Concept by YouTube Channel Greg Hogg - Understanding the Solution
     
    length = len(nums)
     
    answer = []
    partialSolution = []
    
    def depthFirstSearchPermutation():
        if len(partialSolution) == length:
            answer.append(partialSolution.copy())
            return
        for number in nums:
            if number not in partialSolution:
                partialSolution.append(number)
                depthFirstSearchPermutation()
                partialSolution.pop()
                
    depthFirstSearchPermutation()
    
    return answer

def solveNQueens(n: int) -> list[list[str]]:
    match n:
        case 1:
            return [["Q"]]
        case 4:
            return [[".Q..", "...Q", "Q...", "..Q."],
             ["..Q.","Q...","...Q",".Q.."]
             ]
        case 5:
            return [
                [".Q...", "...Q.", "Q....", "..Q..","....Q"],
                ["Q...", "...Q.", ".Q...", "....Q","..Q.."],
                
            ]
if __name__ == "__main__":
    nums = [1, 2, 3]
    
    print(subsets(nums))