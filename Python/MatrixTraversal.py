import collections

def numIslands(grid: list[list[str]]) -> int:
    #Problem #200 Number of Islands - The concept that I learned the solution from is YouTube Channel named NeetCode
        
    if not grid: 
        return 0
    
    rows, columns = len(grid), len(grid[0]) #Get the dimensions of the grid
    visited = set() #Marking visited squares
    islandCount = 0 #Counting the islands meaning separate "1"'s 

    #My intuitive solution for this problem
    # if rows == 1:
    #     if grid[0][len(grid[0]) - 1] == "1":
    #             islandCount += 1
    #     for i in range (0, len(grid[0]) - 1):
    #         if grid[0][i] == "1" and grid[0][i + 1] == "0":
    #             islandCount += 1
    #     return islandCount            

    # if columns == 1:
    #     if grid[len(grid) - 1][0] == "1":
    #         islandCount += 1
    #     for i in range(0, rows - 1):
    #         if grid[i][0] == "1" and grid[i + 1][0] == "0":
    #             islandCount += 1
    #     return islandCount

    def breadthFirstSearch(rowNumber: int, columnNumber: int):
        myQueue = collections.deque()
        
        visited.add((rowNumber, columnNumber))
        myQueue.append((rowNumber, columnNumber))

        while myQueue:
            rowNumber, columnNumber = myQueue.popleft()
    
            # up = [rowNumber - 1, columnNumber]
            # right = [rowNumber, columnNumber + 1]
            # down = [rowNumber + 1, columnNumber]
            # left = [rowNumber, columnNumber - 1]
            
            directions = [[rowNumber - 1, columnNumber], [rowNumber, columnNumber + 1], [rowNumber + 1, columnNumber], [rowNumber, columnNumber - 1]]

            for rowNumber, columnNumber in directions:
                if (rowNumber in range(rows) and columnNumber in range(columns) and grid[rowNumber][columnNumber] == "1" and (rowNumber, columnNumber) not in visited):
                    myQueue.append((rowNumber, columnNumber))
                    visited.add((rowNumber, columnNumber))
            
            #My intuitive solution for this problem
            # if up[0] < 0 and left[1] < 0:
            #     if grid[right[0]][right[1]] == "1" and right not in visited:
            #         myQueue.append(right) 
            #     if grid[down[0]][down[1]] == "1" and down not in visited:
            #         myQueue.append(down)
                
            #     if right not in visited:
            #         visited.add(right)
            #     if  down not in visited:
            #         visited.add(down)

            # elif up[0] < 0 and (right[1] > len(grid[0]) - 1):
            #     if grid[down[0]][down[1]] == "1" and down not in visited:
            #         myQueue.append(down)
            #     if grid[left[0]][left[1]] == "1" and left not in visited:
            #         myQueue.append(left)
                
            #     if down not in visited:
            #         visited.add(down)
            #     if  left not in visited:
            #         visited.add(left)

            # elif (down[0] > len(grid) - 1) and left[1] < 0:
            #     if grid[up[0]][up[1]] == "1" and up not in visited:
            #         myQueue.append(up)
            #     if grid[right[0]][right[1]] == "1" and right not in visited:
            #         myQueue.append(right)
                                 
            #     if up not in visited:
            #         visited.add(up)
            #     if  right not in visited:
            #         visited.add(right)

            # elif (down[0] > len(grid) - 1) and right[1] > (len(grid[0]) - 1):
            #     if grid[up[0]][up[1]] == "1" and up not in visited:
            #         myQueue.append(up)
            #     if grid[left[0]][left[1]] == "1" and left not in visited:
            #         myQueue.append(left)

            #     if up not in visited:
            #         visited.add(up)
            #     if  left not in visited:
            #         visited.add(left)

            # elif left[1] < 0:               
            #     if grid[up[0]][up[1]] == "1" and up not in visited:
            #         myQueue.append(up)
            #     if grid[right[0]][right[1]] == "1" and right not in visited:
            #         myQueue.append(right)
            #     if grid[down[0]][down[1]] == "1" and down not in visited:
            #         myQueue.append(down)
                
            #     if up not in visited:
            #         visited.add(down)
            #     if  right not in visited:
            #         visited.add(right)
            #     if down not in visited:
            #         visited.add(down)

            # elif right[1] > (len(grid[0]) - 1):
            #     if grid[up[0]][up[1]] == "1" and up not in visited:
            #         myQueue.append((up))
            #     if grid[down[0]][down[1]] == "1" and down not in visited:
            #         myQueue.append((down))
            #     if grid[left[0]][left[1]] == "1" and left not in visited:
            #         myQueue.append((left))
                
            #     if up not in visited:
            #         visited.add(up)
            #     if  down not in visited:
            #         visited.add(down)
            #     if left not in visited:
            #         visited.add(left)

            # elif up[0] < 0:
            #     if grid[right[0]][right[1]] == "1" and right not in visited:
            #         myQueue.append((right))
            #     if grid[down[0]][down[1]] == "1" and down not in visited:
            #         myQueue.append((down))
            #     if grid[left[0]][left[1]] == "1" and left not in visited:
            #         myQueue.append((left))
                
            #     if right not in visited:
            #         visited.add(right)
            #     if  down not in visited:
            #         visited.add(down)
            #     if left not in visited:
            #         visited.add(left)

            # elif down[0] > (len(grid) - 1):
            #     if grid[up[0]][up[1]] == "1" and up not in visited:
            #         myQueue.append((up))
            #     if grid[right[0]][right[1]] == "1" and right not in visited:
            #         myQueue.append((right))
            #     if grid[left[0]][left[1]] == "1" and left not in visited:
            #         myQueue.append((left))
                
            #     if up not in visited:
            #         visited.add(up)
            #     if  right not in visited:
            #         visited.add(right)
            #     if left not in visited:
            #         visited.add(left)
            # else:
            #     if grid[up[0]][up[1]] == "1" and up not in visited:
            #         myQueue.append((up))
            #     if grid[right[0]][right[1]] == "1" and right not in visited:
            #         myQueue.append((right))
            #     if grid[down[0]][down[1]] == "1" and down not in visited:
            #         myQueue.append((down))
            #     if grid[left[0]][left[1]] == "1" and left not in visited:
            #         myQueue.append((left))

            #     if up not in visited:
            #         visited.add(up)
            #     if right not in visited:
            #         visited.add(right)
            #     if  down not in visited:
            #         visited.add(down)
            #     if left not in visited:
            #         visited.add(left)
             
    for row in range(rows):
        for square in range(columns):
            if grid[row][square] == "1" and (row, square) not in visited:
                breadthFirstSearch(row, square)
                islandCount += 1
            # else:
            #     if (row, square) not in visited:
            #         visited.add((row, square))

    return islandCount

if __name__ == "__main__":
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","1"],
        ["0","0","1","0","1"],
        ["1","0","0","1","1"]
    ]
    
    # grid = [
    #     ["1"],
    #     ["0"],
    #     ["1"],
    #     ["0"],
    #     ["1"],
    #     ["1"]]


    print(numIslands(grid))
