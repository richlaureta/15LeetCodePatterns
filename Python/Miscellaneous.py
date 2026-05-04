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
    
    topLeftSet = set()
    topMiddleSet = set()
    topRightSet = set()
    
    middleLeftSet = set()
    middleMiddleSet = set()
    middleRightSet = set()
    
    bottomLeftSet = set()
    bottomMiddleSet = set()
    bottomRightSet = set()
    
    column0Set = set()
    column1Set = set()
    column2Set = set()
    column3Set = set()
    column4Set = set()
    column5Set = set()
    column6Set = set()
    column7Set = set()
    column8Set = set()
    
    for index in range(len(board)):
        numberSeenRow = set()
        for index1 in range(len(board[0])):
            if board[index][index1] != "." and board[index][index1] in  numberSeenRow:
                return False
            else:
                numberSeenRow.add(board[index][index1])
            
            match index1:
                case 0:
                    if board[index][index1] != "." and board[index][index1] in column0Set:
                        return False
                    column0Set.add(board[index][index1])
                case 1:
                    if board[index][index1] != "." and board[index][index1] in column1Set:
                        return False
                    column1Set.add(board[index][index1])
                case 2:
                    if board[index][index1] != "." and board[index][index1] in column2Set:
                        return False
                    column2Set.add(board[index][index1])
                case 3:
                    if board[index][index1] != "." and board[index][index1] in column3Set:
                        return False
                    column3Set.add(board[index][index1])
                case 4:
                    if board[index][index1] != "." and board[index][index1] in column4Set:
                        return False
                    column4Set.add(board[index][index1])
                case 5:
                    if board[index][index1] != "." and board[index][index1] in column5Set:
                        return False
                    column5Set.add(board[index][index1])
                case 6:
                    if board[index][index1] != "." and board[index][index1] in column6Set:
                        return False
                    column6Set.add(board[index][index1])
                case 7:
                    if board[index][index1] != "." and board[index][index1] in column7Set:
                        return False
                    column7Set.add(board[index][index1])
                case 8:
                    if board[index][index1] != "." and board[index][index1] in column8Set:
                        return False
                    column8Set.add(board[index][index1])
            
            if index < 3 and index1 < 3:
                if board[index][index1] != "." and board[index][index1] in topLeftSet:
                    return False
                topLeftSet.add(board[index][index1])
            elif index < 3 and index1 > 2 and index1 < 6:
                if board[index][index1] != "." and board[index][index1] in topMiddleSet:
                    return False
                topMiddleSet.add(board[index][index1])
            elif index < 3 and index1 > 5:
                if board[index][index1] != "." and board[index][index1] in topRightSet:
                    return False
                topRightSet.add(board[index][index1])
            elif index > 2 and index < 6 and index1 < 3 and index1 < 3:
                if board[index][index1] != "." and board[index][index1] in middleLeftSet:
                    return False
                middleLeftSet.add(board[index][index1])
            elif index > 2 and index < 6 and index1 > 2 and index1 < 6:
                if board[index][index1] != "." and board[index][index1] in middleMiddleSet:
                    return False
                middleMiddleSet.add(board[index][index1])
            elif index > 2 and index < 6 and index1 > 5:
                if board[index][index1] != "." and board[index][index1] in middleRightSet:
                    return False
                middleRightSet.add(board[index][index1])
            elif index > 5 and index1 < 3:
                if board[index][index1] != "." and board[index][index1] in bottomLeftSet:
                    return False
                bottomLeftSet.add(board[index][index1])
            elif index > 5 and index1 > 2 and index1 < 6:
                if board[index][index1] != "." and board[index][index1] in bottomMiddleSet:
                    return False
                bottomMiddleSet.add(board[index][index1])
            elif index > 5 and index1 > 5:
                if board[index][index1] != "." and board[index][index1] in bottomRightSet:
                    return False
                bottomRightSet.add(board[index][index1])
    
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