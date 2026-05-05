import copy

def subsets(nums: list[int]) -> list[list[int]]:
    #Problem #78 Subsets - Medium - Solution Concept by YouTube Channel NeetCode - Understanding the Solution
    
    completeSubsets = []
    subset = []
    
    def depthFirstSearchSubsets(index: int):
        if index >= len(nums):
            completeSubsets.append(subset.copy())
            return
        
        subset.append(nums[index])
        depthFirstSearchSubsets(index + 1)
        
        subset.pop()
        depthFirstSearchSubsets(index + 1)
    
    
    depthFirstSearchSubsets(0)
    
    return completeSubsets

def permute(nums: list[int]) -> list[list[int]]:
    #Problem #46 Permutations - Medium - Solution Concept by YouTube Channel Gregg Hogg - Understanding the Solution
    
    solution = []
    partialSolution = []
    numberSet = set()
    
    def backTracking():
        if len(nums) == len(partialSolution):
            solution.append(partialSolution.copy())
            return
        
        for number in nums:
            if number not in numberSet:
                partialSolution.append(number)
                numberSet.add(number)
                backTracking()
                numberSet.remove(partialSolution.pop())
                
    backTracking()
    
    return solution

def solveNQueens(n: int) -> list[list[str]]:
    #Problem #51 N-Queens - Hard - Solution Concept by YouTube Channel NeetCode - Understanding the Solution
    
    columnSet = set()
    positiveDiagonalSet = set()
    negativeDiagonalSet = set()
    
    possibleBoardCombinations = []
    board = [["."] * n for row in range(n)]
    
    def backtrack(row1: int):
        if row1 == n:
            boardCopy = ["".join(row1) for row1 in board]
            possibleBoardCombinations.append(boardCopy)
            return

        for column in range(n):
            if column in columnSet or (row1 + column) in positiveDiagonalSet or (row1 - column) in negativeDiagonalSet:
                continue
            
            columnSet.add(column)
            positiveDiagonalSet.add(row1 + column)
            negativeDiagonalSet.add(row1 - column)
            board[row1][column] = "Q"
            
            backtrack(row1 + 1)
            
            columnSet.remove(column)
            positiveDiagonalSet.remove(row1 + column)
            negativeDiagonalSet.remove(row1 - column)
            board[row1][column] = "."
    
    backtrack(0)
    
    return possibleBoardCombinations

if __name__ == "__main__":
    n = 4
    
    print(solveNQueens(n))