from collections import defaultdict

def checkOnesSegment(s: str) -> bool:
    #Problem #1784 Check if Binary String Has at Most One Segment of Ones
    
	seenSegmentFlag = False
	index = 0
	
	while index < len(s):
		if s[index] == '1' and seenSegmentFlag == False:
			index += 1
			seenSegmentFlag = True
			while index < len(s) and s[index] == '1':
				index += 1
		if index < len(s) and s[index] == '1':
			return False
		index += 1
	
	return True

def findAndReplacePattern(words: list[str], pattern: str) -> list[str]:
    #Problem #890 Find and Replace Pattern - Medium
    
    uniqueLetterIndexDictionary = defaultdict(set)
    letterToUniqueCount = defaultdict(int)
    uniqueCount = 1
    patternSet = set()
    
    for index0, letter in enumerate(pattern):
        if letter not in patternSet:
            patternSet.add(letter)
            letterToUniqueCount[letter] = uniqueCount
            uniqueLetterIndexDictionary[letterToUniqueCount[letter]].add(index0)
            uniqueCount += 1
        else:
            uniqueLetterIndexDictionary[letterToUniqueCount[letter]].add(index0)
    
    wordsPatternMatch = []
    
    for word in words:
        wordPatternSet = set()
        letterToUniqueCount1 = defaultdict(int)
        uniqueCount1 = 1
        for index1, letter1 in enumerate(word):
            if letter1 not in wordPatternSet:
                wordPatternSet.add(letter1)
                letterToUniqueCount1[letter1] = uniqueCount1
                if index1 not in uniqueLetterIndexDictionary[letterToUniqueCount1[letter1]]:
                    index1 -= 1
                    break
                uniqueCount1 += 1
            else:
                if index1 not in uniqueLetterIndexDictionary[letterToUniqueCount1[letter1]]:
                    index1 -= 1
                    break
        
        if index1 == len(word) - 1:
            wordsPatternMatch.append(word)
    
    return wordsPatternMatch

def isValidSudoku(board: list[list[str]]) -> bool:
    #Problem #36 Valid Sudoku - Medium

    for index in range(9):
        numberSeenSet = set()
        for index1 in range(9):
            if board[index][index1] != "." and board[index][index1] in numberSeenSet:
                return False
            numberSeenSet.add(board[index][index1])

    for index2 in range(9):
        numberSeenSet1 = set()
        for index3 in range(9):
            if board[index3][index2] != "." and board[index3][index2] in numberSeenSet1:
                return False
            numberSeenSet1.add(board[index3][index2])

    startingPoints = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0,], [6, 3], [6, 6]]

    for startingPoint in startingPoints:
        numberSeenSet2 = set()
        for index4 in range(startingPoint[0], startingPoint[0] + 3):
            for index5 in range(startingPoint[1], startingPoint[1] + 3):
                if board[index4][index5] != "." and board[index4][index5] in numberSeenSet2:
                    return False
                numberSeenSet2.add(board[index4][index5])
        
    return True
    
if __name__ == "__main__":
    board = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]
    
    print(isValidSudoku(board))