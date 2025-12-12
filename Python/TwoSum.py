def twoSum(nums: list[int], target: int) -> list[int]:
    #Problem #1 Two Sum - Easy
    numberDictionary = {}
    
    for index, number in enumerate(nums):
        difference = target - number
        if difference in numberDictionary:
            return [numberDictionary[difference], index]
        
        numberDictionary[number] = index

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    print(twoSum(nums, target))