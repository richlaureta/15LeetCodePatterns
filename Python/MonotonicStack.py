import sys

def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    decrementIndex = len(nums2) - 1
    # array = [-1] * len(nums2)
    stack = []
    dictList = {}
    arrayQuery =[]

    for i in reversed(nums2):
        while stack and i >= stack[-1]:
            stack.pop()

        if stack and i < stack[-1]:
            # array[decrementIndex] = stack[-1]
            dictList[i] = stack[-1]
        else:
            dictList[i] = -1

        stack.append(i)
        decrementIndex -= 1

    for i in nums1:
        arrayQuery.append(dictList[i])
        
    return arrayQuery

def main():
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]

    # nums1 = [2, 4]
    # nums2 = [1, 2, 3, 4]
    
    # nums1 = [1, 3, 5, 2, 4]
    # nums2 = [6, 5, 4, 3, 2, 1, 7]

    # nums2 = [2, 1, 2, 4, 3]

    print(nextGreaterElement(nums1, nums2))

if __name__ == "__main__":
    sys.exit(main())