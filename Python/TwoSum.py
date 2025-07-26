def twoSum(nums: list[int], target: int) -> list[int]:
    #Problem #1 Two Sum
    
    myDictionary = {}

    for i in range(0, len(nums)):
        difference = target - nums[i]

        if difference in myDictionary and i != myDictionary[difference]:
            return [myDictionary[difference], i]
         
        myDictionary[nums[i]] = i

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    print(twoSum(nums, target))