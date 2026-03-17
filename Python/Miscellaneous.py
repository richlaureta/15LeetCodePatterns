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
    patternSet = set()
    orderOfLetter = []
    
    for index0, letter in enumerate(pattern):
        if letter not in patternSet:
            orderOfLetter.append(letter)
            patternSet.add(letter)
        patternFrequencyDictionary[letter].append(index0)
    
    wordsPatternMatch = []
    
    for word in words:
        letterFrequencyDictionary = defaultdict(list[int])
        wordPatternSet = set()
        orderOfLetter1 = []
        for index1, letter1 in enumerate(word):
            if letter1 not in wordPatternSet:
                orderOfLetter1.append(letter1)
                wordPatternSet.add(letter1)
            letterFrequencyDictionary[letter1].append(index1)
        
        if len(orderOfLetter) != len(orderOfLetter1):
            continue
        
        for index2, letter2 in enumerate(orderOfLetter):
            if patternFrequencyDictionary[letter2] != letterFrequencyDictionary[orderOfLetter1[index2]]:
                break
        
        if len(orderOfLetter) - 1 == index2:
            wordsPatternMatch.append(word)  
    
    return wordsPatternMatch

if __name__ == "__main__":
    words = ["a","b","c"]
    pattern = "a"
    
    print(findAndReplacePattern(words, pattern))