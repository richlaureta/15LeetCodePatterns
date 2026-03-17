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
    
    patternFrequencyDictionary = defaultdict(int)
    patternSet = set()
    orderOfLetter = []
    
    for letter in pattern:
        if letter not in patternSet:
            orderOfLetter.append(letter)
            patternSet.add(letter)
        patternFrequencyDictionary[letter] += 1
    
    wordsPatternMatch = []
    
    for word in words:
        letterFrequencyDictionary = defaultdict(int)
        wordPatternSet = set()
        orderOfLetter1 = []
        for letter1 in word:
            pass    
    
    return wordsPatternMatch
if __name__ == "__main__":
    words = ["abc","deq","mee","aqq","dkd","ccc"]
    pattern = "abb"
    
    print(findAndReplacePattern(words, pattern))