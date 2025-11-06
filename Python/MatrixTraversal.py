from collections import deque 

def numIslands(grid: list[list[str]]) -> int:
    #Problem #200 Number of Islands - Medium - The concept that I learned the solution from is YouTube Channel named NeetCode
    
    if not grid:
        return 0
    
    visited = set()
    locationQueue = deque()
    
    numberOfIslandsCount = 0
    
    def breadthFirstSearchIslands(index0: int, index1: int):
        visited.add((index0, index1))
        locationQueue.appendleft((index0, index1))
        
        while locationQueue:
            verticalPop, horizontalPop = locationQueue.popleft()
            
            checkDirections = [
                [verticalPop - 1, horizontalPop], 
                [verticalPop, horizontalPop + 1],
                [verticalPop + 1, horizontalPop],
                [verticalPop, horizontalPop - 1]
            ]
            
            for direction in checkDirections:
                if direction[0] > -1 and direction[0] < len(grid) and direction[1] > -1 and direction[1] < len(grid[0]) and grid[direction[0]][direction[1]] == "1" and (direction[0], direction[1]) not in visited:
                    visited.add((direction[0], direction[1]))
                    locationQueue.append((direction[0], direction[1]))
                    
    for index0, value0 in enumerate(grid):
        for index1, value1 in enumerate(value0):
            if grid[index0][index1] == "1" and (index0, index1) not in visited:
                numberOfIslandsCount += 1
                breadthFirstSearchIslands(index0, index1)
    
    return numberOfIslandsCount
            
        
def floodFill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    #Problem #733 Flood Fill - Easy 
    
    colorQueue = deque()
    colorQueue.append((sr, sc))
    visited = set()
    visited.add((sr, sc))
    
    startingValue = image[sr][sc]
    
    image[sr][sc] = color
    while colorQueue:
        poppedColorLocation = colorQueue.popleft()
        
        checkDirections = [[poppedColorLocation[0] - 1, poppedColorLocation[1]], 
                           [poppedColorLocation[0], poppedColorLocation[1] + 1], 
                           [poppedColorLocation[0] + 1, poppedColorLocation[1]],
                           [poppedColorLocation[0], poppedColorLocation[1] - 1]
                           ]
        
        for count in range(0, len(checkDirections)):
            if checkDirections[count][0] < len(image) and checkDirections[count][0] > -1 and checkDirections[count][1] < len(image[0]) and checkDirections[count][1] > -1 and image[checkDirections[count][0]][checkDirections[count][1]] == startingValue and (checkDirections[count][0], checkDirections[count][1]) not in visited:
                image[checkDirections[count][0]][checkDirections[count][1]] = color
                colorQueue.append((checkDirections[count][0], checkDirections[count][1]))
                visited.add((checkDirections[count][0], checkDirections[count][1]))
    
    return image

def solve(board: list[list[str]]) -> None:
    #Problem #130 Surrounded Regions - Medium
    
    visited = set()
    flipOArray = []
    locationQueue = deque()
    
    onBorderFlag = [False]
    
    def breadthFirstSearchRegion(index0: int, index1: int):
        locationQueue.append((index0, index1))
        flipOArray.append([index0, index1])
        
        if index0 == 0 or index0 == len(board) - 1 or index1 == 0 or index1 == len(board[0]) - 1:
            onBorderFlag[0] = True
            
        while locationQueue:
            row, column = locationQueue.popleft()
            
            checkDirections = [[row - 1, column], [row, column + 1], [row + 1, column], [row, column - 1]]
            
            for direction in checkDirections:
                if direction[0] > -1 and direction[0] < len(board) and direction[1] > -1 and direction[1] < len(board[0]) and board[direction[0]][direction[1]] == "O" and (direction[0], direction[1]) not in visited:
                    visited.add((direction[0], direction[1]))
                    locationQueue.append((direction[0], direction[1]))
                    flipOArray.append([direction[0], direction[1]])
                    if direction[0] == 0 or direction[0] == len(board) - 1 or direction[1] == 0 or direction[1] == len(board[0]) - 1:
                        onBorderFlag[0] = True
                    
    for index0, row in enumerate(board):
        for index1, value in enumerate(row):
            if board[index0][index1] == "O" and (index0, index1) not in visited:
                breadthFirstSearchRegion(index0, index1)
                if onBorderFlag[0] == False:
                    for x, y in flipOArray:
                        board[x][y] = "X"
                    flipOArray = []
                    
                else:
                    onBorderFlag[0] = False
                    flipOArray = []
            
if __name__ == "__main__":  
    board = [
        ["O","X","X","O"],
        ["X","O","O","X"],
        ["O","X","O","X"],
        ["X","O","X","O"]
    ]
    
    board = [
        ["X", "X", "X"],
        ["X", "O", "X"],
        ["X", "X", "X"]
    ]
    
    solve(board)
    
    for row in board:
        for value in row:
            print(value, end = " ")
        print()