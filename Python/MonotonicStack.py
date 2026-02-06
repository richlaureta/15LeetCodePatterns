from collections import defaultdict

def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    #Problem 496 Next Greater Element I - Easy
    
    stack = [0]
    increasingList = [-1] * len(nums2)
    
    indexDictionary = defaultdict(int)
    indexDictionary[nums2[0]] = 0
    
    greaterElementList = [0] * len(nums1)
    
    for index in range (1, len(nums2)):
        while stack and nums2[stack[-1]] < nums2[index]:
            increasingList[stack.pop()] = nums2[index]
        
        stack.append(index)
        indexDictionary[nums2[index]] = index
    
    for index1 in range(0, len(greaterElementList)):
        greaterElementList[index1] = increasingList[indexDictionary[nums1[index1]]]
        
    return greaterElementList
    
def dailyTemperatures(temperatures: list[int]) -> list[int]:
    #Problem #739 Daily Temperatures - Medium - not the most efficient
    
    indexStack = [0]
    increasingList = [0] * len(temperatures)
    
    for index in range(1, len(temperatures)):
        while indexStack and temperatures[indexStack[-1]] < temperatures[index]:
            increasingList[indexStack[-1]] = index - indexStack[-1]
            indexStack.pop()
        indexStack.append(index)
    
    return increasingList

def largestRectangleArea(heights: list[int]) -> int:
    #Problem #84 Largest Rectangle in Histogram - Hard - Concept Solution by YouTuber Greg Hogg
    
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
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

    print(dailyTemperatures(temperatures))