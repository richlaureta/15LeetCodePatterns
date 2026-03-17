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
    
    patternFrequencyDictionary = defaultdict(list[int])
    letterToUniqueCount = defaultdict(int)
    uniqueCount = 1
    patternSet = set()
    
    for index0, letter in enumerate(pattern):
        if letter not in patternSet:
            patternSet.add(letter)
            letterToUniqueCount[letter] = uniqueCount
            patternFrequencyDictionary[letterToUniqueCount[letter]].append(index0)
            uniqueCount += 1
        else:
            patternFrequencyDictionary[letterToUniqueCount[letter]].append(index0)
    
    wordsPatternMatch = []
    
    for word in words:
        letterFrequencyDictionary = defaultdict(list[int])
        wordPatternSet = set()
        letterToUniqueCount1 = defaultdict(int)
        uniqueCount1 = 1
        for index1, letter1 in enumerate(word):
            if letter1 not in wordPatternSet:
                wordPatternSet.add(letter1)
                letterToUniqueCount1[letter1] = uniqueCount1
                letterFrequencyDictionary[letterToUniqueCount1[letter1]].append(index1)
                uniqueCount1 += 1
            else:
                letterFrequencyDictionary[letterToUniqueCount1[letter1]].append(index1)
        
        if patternFrequencyDictionary == letterFrequencyDictionary:
            wordsPatternMatch.append(word)
            
    return wordsPatternMatch

if __name__ == "__main__":
    words = ["a","b","c"]
    pattern = "a"
    
    print(findAndReplacePattern(words, pattern))