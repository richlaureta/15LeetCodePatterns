import collections

def numIslands(grid: list[list[str]]) -> int:
    #Problem #200 Number of Islands - THe concept that I learned the solution from is YouTube Channel named NeetCode

    if grid is None:
        return 0
    
    rows, columns = len(grid), len(grid[0])
    visited = set()
    islandCount = 0

    def breadthFirstSearch(rowNumber: int, squareNumber: int):
        myQueue = collections.deque()
        
        visited.add(rowNumber, squareNumber)
        myQueue.append(rowNumber, squareNumber)

        while myQueue:
            rowNumber, squareNumber = myQueue.popleft()
            

    for row in range(rows):
        for square in range(columns):
            if square == "1" and (row, square) not in visited:
                breadthFirstSearch(row, square)
                islandCount += 1
    
    return islandCount

if __name__ == "__main__":
    grid = [
        ["1","1","1","0","0"],
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","0","1","1"]
    ]

    numIslands(grid)
