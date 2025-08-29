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
    #Problem #739 Daily Temperatures
    
    #My Initial Solution
    # listToReturn = deque()
    # myStack = []
    # decrementingIndex = len(temperatures) - 1
    # myDictionary = {}
    
    # for i in reversed(temperatures):
    #     if len(myStack) == 0:
    #         listToReturn.appendleft(0)
    #         myStack.append(i)
    #         myDictionary[i] = decrementingIndex
    #     else:
    #         flag = False
    #         if i >= myStack[-1]:
    #             while i >= myStack[-1] and flag == False:
    #                 myStack.pop()
    #                 if len(myStack) == 0:
    #                     listToReturn.appendleft(0)
    #                     myStack.append(i)
    #                     myDictionary[i] = decrementingIndex
    #                     flag = True

    #             if flag == True:
    #                 decrementingIndex -= 1
    #                 continue
    #             else:
    #                 listToReturn.appendleft(myDictionary[myStack[-1]] - decrementingIndex)
    #                 myStack.append(i)
    #                 myDictionary[i] = decrementingIndex
    #         else:
    #             listToReturn.appendleft(myDictionary[myStack[-1]] - decrementingIndex)
    #             myStack.append(i)
    #             myDictionary[i] = decrementingIndex
                
    #     decrementingIndex -= 1

    # return list(listToReturn)

    #More Optimized Solution
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
    

if __name__ == "__main__":
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    # temperatures = [30, 40, 50, 60]
    # temperatures = [30, 60, 90]
    # temperatures = [49, 70, 47, 47, 46, 70]

    # temperatures = [89,62,70,58,47,47,46,76,100,70]

    # temperatures = [34,80,80,34,34,80,80,80,80,34]
    
    print(dailyTemperatures(temperatures))
