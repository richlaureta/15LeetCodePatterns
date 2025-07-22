def singleNumber(nums: list[int]) -> int:
    #Problem #136 Single Number
    nums.sort() 
    
    for i in range(0, len(nums), 2):
        if i == len(nums) - 1:
            return nums[i]
        
        if nums[i] != nums[i + 1]:
            return nums[i]

if __name__ == "__main__":
    nums = [1]

    print(singleNumber(nums))