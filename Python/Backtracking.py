def subsets(nums: list[int]) -> list[list[int]]:
    #Problem #78 Subsets - Medium -  Concept by Greg Hogg(Youtuber)
    
    n = len(nums)
    finalAnswer, tracker = [], []

    def backTrack(index: int):
        if index == n:
            finalAnswer.append(tracker[:]) #Return copy of the tracker
            return
        
        #Don't pick nums[index]
        backTrack(index + 1)

        #Pick nums[index]
        tracker.append(nums[index])
        backTrack(index + 1)
        tracker.pop()

    backTrack(0)
    return finalAnswer
if __name__ == "__main__":
    nums = [1, 2, 3]

    print(subsets(nums))