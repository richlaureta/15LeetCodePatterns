from collections import deque 

def numIslands(grid: list[list[str]]) -> int:
    #Problem #200 Number of Islands - The concept that I learned the solution from is YouTube Channel named NeetCode
        
    if not grid: 
        return 0
    
    rows, columns = len(grid), len(grid[0]) #Get the dimensions of the grid
    visited = set() #Marking visited squares
    islandCount = 0 #Counting the islands meaning separate "1"'s 

    def breadthFirstSearch(rowNumber: int, columnNumber: int):
        myQueue = deque()
        
        visited.add((rowNumber, columnNumber))
        myQueue.append((rowNumber, columnNumber))

        while myQueue:
            rowNumber, columnNumber = myQueue.popleft()
            directions = [[rowNumber - 1, columnNumber], [rowNumber, columnNumber + 1], [rowNumber + 1, columnNumber], [rowNumber, columnNumber - 1]]

            for rowNumber, columnNumber in directions:
                if (rowNumber in range(rows) and columnNumber in range(columns) and grid[rowNumber][columnNumber] == "1" and (rowNumber, columnNumber) not in visited):
                    myQueue.append((rowNumber, columnNumber))
                    visited.add((rowNumber, columnNumber))
    for row in range(rows):
        for square in range(columns):
            if grid[row][square] == "1" and (row, square) not in visited:
                breadthFirstSearch(row, square)
                islandCount += 1

    return islandCount

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
    image = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]
    ]
    
    sr = 1
    sc = 1
    color = 2
    
    editedImage = floodFill(image, sr, sc, color)
    
    for array in editedImage:
        for value in array:
            print(value, end = " ")
        print()
    
