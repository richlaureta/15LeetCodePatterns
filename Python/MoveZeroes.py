def moveZeroes(nums: list[int]) -> None:
    #Problem # 283
    
    #Intuitive Solution

    # newArray = [0] * len(nums)
    # lengthDecrement = len(nums)
    # newArrayIndex = 0
    # for i in range(lengthDecrement):
    #     if nums[i] != 0:
    #         newArray[newArrayIndex] = nums[i]
    #         newArrayIndex += 1
    #     else:
    #         lengthDecrement -= 1

    # nums = newArray

    #Solution for not making a copy in my own code.

    countPreviousZeroes = 0

    for i in range(0, len(nums)):
        if nums[i] == 0:
            countPreviousZeroes += 1
        else:
            if countPreviousZeroes == 0:
                continue
            else:
                nums[i - countPreviousZeroes] = nums[i]
                nums[i] = 0
                if ((i + countPreviousZeroes) == (len(nums))) or  (i + countPreviousZeroes) > len(nums):
                    nums[i] = 0
        
    
if __name__ == "__main__":
    nums = [0, 1, 0]

    moveZeroes(nums)

    print(nums)
