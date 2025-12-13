import sys
from collections import deque

def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    decrementIndex = len(nums2) - 1
    stack = []
    dictList = {}
    arrayQuery =[]

    for i in reversed(nums2):
        while stack and i >= stack[-1]:
            stack.pop()

        if stack and i < stack[-1]:
            dictList[i] = stack[-1]
        else:
            dictList[i] = -1

        stack.append(i)
        decrementIndex -= 1

    for i in nums1:
        arrayQuery.append(dictList[i])
        
    return arrayQuery

def dailyTemperatures(temperatures: list[int]) -> list[int]:
    #Problem #739 Daily Temperatures - Medium 
    
    returnList = [0] * len(temperatures)
    decreasingStack = []

    for index, temperature in enumerate(temperatures):
        if len(decreasingStack) == 0:
            decreasingStack.append(index)
            continue
        
        while temperature > temperatures[decreasingStack[-1]]:
            poppedIndex = decreasingStack.pop()
            returnList[poppedIndex] = index - poppedIndex
        
            if len(decreasingStack) == 0:
                decreasingStack.append(index)
                break

        if temperature <= temperatures[decreasingStack[-1]]:
            decreasingStack.append(index)

    return returnList

def largestRectangleArea(heights: list[int]) -> int:
    #Problem #84 Largest Rectangle in Histogram - Concept Solution by YouTuber Greg Hogg
    
    maxArea = heights[0]
    increasingStack = [(heights[0], 0)]
    
    for index in range(1, len(heights)):
        appendFlag = False

        while increasingStack and (heights[index] < increasingStack[-1][0]):
            heightAndIndex = increasingStack.pop()
            area = heightAndIndex[0] * (index - heightAndIndex[1])

            if area > maxArea:
                maxArea = area

            if (len(increasingStack) == 0) or (heights[index] > increasingStack[-1][0]):
                increasingStack.append((heights[index], heightAndIndex[1]))
                appendFlag = True
        
        if appendFlag == False:
            increasingStack.append((heights[index], index))
    
    while increasingStack:
        poppedValue = increasingStack.pop()
        area = (poppedValue[0]) * (len(heights) - poppedValue[1])
        if area > maxArea:
            maxArea = area

    return maxArea

if __name__ == "__main__":
    # heights = [2, 1, 5, 6, 2, 3]
    heights = [2]

    print(largestRectangleArea(heights))