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

if __name__ == "__main__":
    # words = ["abc","deq","mee","aqq","dkd","ccc"]
    words = ["a","b","c"]
    pattern = "a"
    
    print(findAndReplacePattern(words, pattern))