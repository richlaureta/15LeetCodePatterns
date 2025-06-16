import sys

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

def main():
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]

    print(nextGreaterElement(nums1, nums2))

if __name__ == "__main__":
    sys.exit(main())