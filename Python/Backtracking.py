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
    #Problem #51 N-Queens - Medium - Solution Concept by YouTube Channel NeetCode - Understanding the Solution
    
    column = set()
    positiveDiagonal = set()
    negativeDiagonal = set()
    
    result = []
    
    board = [["."] * n for i in range(n)]
    
    def depthFirstSearchQueens(row0):
        if row0 == n:
            copy = ["".join(row1) for row1 in board]
            result.append(copy)
            return
        
        for column1 in range(n):
            if column1 in column or (row0 + column1) in positiveDiagonal or (row0 - column1) in negativeDiagonal:
                continue
            
            column.add(column1)
            positiveDiagonal.add(row0 + column1)
            negativeDiagonal.add(row0 - column1)
            board[row0][column1] = "Q"
            
            depthFirstSearchQueens(row0 + 1)
            
            column.remove(column1)
            positiveDiagonal.remove(row0 + column1)
            negativeDiagonal.remove(row0 - column1)
            board[row0][column1] = "."
            
        depthFirstSearchQueens(0)
    
        return result
    
if __name__ == "__main__":
    n = 4
    
    print(solveNQueens(n))