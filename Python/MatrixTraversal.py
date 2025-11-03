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
        
if __name__ == "__main__":
    grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]

    print(numIslands(grid))