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
    #Problem #739 Daily Temperatures - Medium
    
    indexStack = [0]
    increasingList = [0] * len(temperatures)
    
    for index in range(1, len(temperatures)):
        while indexStack and temperatures[indexStack[-1]] < temperatures[index]:
            increasingList[indexStack[-1]] = index - indexStack[-1]
            indexStack.pop()
        indexStack.append(index)
    
    return increasingList

def largestRectangleArea(heights: list[int]) -> int:
    #Problem #84 Largest Rectangle in Histogram - Hard
    
    maxArea = 0
    increasingStack = []
    
    for index, height in enumerate(heights):
        resetingStartingIndex = index 
        while increasingStack and increasingStack[-1][1] > height:
            poppedIndexHeight = increasingStack.pop()
            resetingStartingIndex = poppedIndexHeight[0]
            maxArea = max(maxArea, poppedIndexHeight[1] * (index - poppedIndexHeight[0]))
        
        increasingStack.append([resetingStartingIndex, height])

    for indexHeight in increasingStack:
        maxArea = max(maxArea, indexHeight[1] * (len(heights) - indexHeight[0]))
         
    return maxArea
            
if __name__ == "__main__":
    height = [1,3,2,1,2,1]

    print(largestRectangleArea(height))