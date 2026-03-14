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

if __name__ == "__main__":
    s = "0011"
    print(checkOnesSegment(s))