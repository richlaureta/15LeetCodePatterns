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
    increasingStack = [] # Stores [start_index, height]
    
    for index, height in enumerate(heights):
        start = index
        while increasingStack and increasingStack[-1][1] > height:
            popped_index, popped_height = increasingStack.pop()
            maxArea = max(maxArea, popped_height * (index - popped_index))
            start = popped_index
        
        increasingStack.append([start, height])
    
    # Process remaining elements in the stack
    for start_index, height in increasingStack:
        maxArea = max(maxArea, height * (len(heights) - start_index))
         
    return maxArea
            
if __name__ == "__main__":
    height = [1,3,2,1,2,1]

    print(largestRectangleArea(height))